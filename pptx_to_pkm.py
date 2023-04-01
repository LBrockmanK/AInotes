import os
import shutil
import collections 
import collections.abc
from pptx import Presentation
from pptx.util import Inches
from PIL import Image
from transformers import AutoTokenizer, AutoModel
from transformers import pipeline
import torch
import numpy as np
from pptx.shapes.picture import Picture
import errno

# Initialize the tokenizer and model for sentence embeddings
tokenizer = AutoTokenizer.from_pretrained("t5-small", model_max_length=512)
model = AutoModel.from_pretrained("sentence-transformers/paraphrase-MiniLM-L6-v2")

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

# Function to compute text similarity using sentence embeddings
def similarity(text1, text2):
    inputs = tokenizer([text1, text2], return_tensors="pt", padding=True, truncation=True)

    # Filter out unknown tokens
    filtered_input_ids = [
        inputs["input_ids"][i, inputs["input_ids"][i] < model.config.vocab_size] for i in range(inputs["input_ids"].shape[0])
    ]

    # Find the maximum length after filtering
    max_length = max([len(ids) for ids in filtered_input_ids])

    # Pad the filtered input tensors to the same length
    padded_input_ids = torch.stack([torch.cat((ids, torch.zeros(max_length - len(ids), dtype=torch.long))) for ids in filtered_input_ids])

    inputs["input_ids"] = padded_input_ids

    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1).numpy()

    similarity_score = np.inner(embeddings[0], embeddings[1]) / (
        np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])
    )
    return similarity_score

# Find likely links between subject
def link_slides(content,similarity_threshold):
    # We're going to want to take each title line, and search the text of other slides for similarities and link those back to the working slide
    # Link every slide to its predecessor and follower
    return content

# Function to process and merge similar slides in a content list
def process_slides(content, similarity_threshold, length):
    # Summarization and other operations
    processed_content = []
    for slide in content:
        # Replace square braces (these are used by obsidian for linking so we don't want have them for other purposes)
        slide["text"] = slide["text"].replace("[", "{").replace("]", "}")

        # TODO: Maybe remove Susan's name

        # Summarize the text in the slide
        slide["text"] = summarizer(slide["text"], max_length=length, do_sample=False)[0]["summary_text"]

        processed_content.append(slide)

    return processed_content

def merge_slides(content, similarity_threshold):
    merged_content = []

    # Merging similar slides
    while content:
        current_slide = content.pop(0)
        found_similar_slide = False

        for i, slide in enumerate(content):
            if similarity(current_slide["subject"], slide["subject"]) > similarity_threshold:
                merged_slide = {"subject": current_slide["subject"],"text": current_slide["text"] + "\n" + slide["text"],"images": current_slide["images"] + slide["images"]}
                merged_content.append(merged_slide)
                content.pop(i)
                found_similar_slide = True
                break

        if not found_similar_slide:
            merged_content.append(current_slide)

    return merged_content

# Reset output directory
def clear_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# Function to extract text and images from a PPTX file
def extract_content(pptx_file, output_dir):
    # Read the PPTX file using the python-pptx library and store it in the variable 'prs'.
    prs = Presentation(pptx_file)
    # Initialize an empty list to store the extracted content.
    content = []
    previous_subject = "UNKNOWN"

    # Iterate through the slides in the presentation using their index and value.
    for slide_num, slide in enumerate(prs.slides):
        # Initialize a dictionary to store the text and images for each slide.
        slide_content = {"subject": "", "text": "", "images": []}
        text_boxes = []

        # Iterate through the shapes in each slide.
        for shape in slide.shapes:
            # Check if the shape has a text frame and append its text to the text_boxes list.
            if shape.has_text_frame:
                text_boxes.append(shape.text)

            # Check if the shape has an image.
            if isinstance(shape, Picture):
                # Filter out audio images by checking if "Audio" is in the shape name.
                if "Audio" not in shape.name:
                    # Store the image object in the variable 'image'.
                    image = shape.image
                    # Create an image file path using the slide number, shape name, and image file extension.
                    image_path = f"slide_{slide_num}_image_{shape.name}.{image.ext}"
                    # Create the full image path, including the output directory.
                    full_image_path = os.path.join(output_dir, image_path)
                    # Write the image binary data (blob) to a new image file with the created file path.
                    with open(full_image_path, "wb") as image_file:
                       image_file.write(image.blob)
                    # Append the image file path to the slide_content dictionary.
                    slide_content["images"].append(image_path)

        # Add notes text to text_boxes
        if slide.has_notes_slide:
            notes_slide = slide.notes_slide
            for shape in notes_slide.shapes:
                if shape.has_text_frame:
                    text_boxes.append(shape.text)

        # Assign the first text box as the subject, and join the rest of the text boxes with a newline.
        if text_boxes:
            slide_content["subject"] = text_boxes[0]
            slide_content["text"] = "\n".join(text_boxes[1:])
        else:
            slide_content["subject"] = previous_subject

        # Update the previous_subject variable with the current slide's subject.
        previous_subject = slide_content["subject"]

        # Append the slide_content dictionary to the content list.
        content.append(slide_content)

    # Return the content list containing text and images from the PPTX file.
    return content

def check_directory_writable(directory):
    try:
        test_file = os.path.join(directory, "test_write.txt")
        with open(test_file, "w") as file:
            file.write("test")
        os.remove(test_file)
        return True
    except IOError as e:
        if e.errno == errno.EACCES:
            return False
        else:
            raise

def create_markdown_files(content, output_dir):
    for slide_num, slide in enumerate(content):
        body_text = slide["text"]
        subject_line = slide["subject"]

        # Replace invalid characters in the subject line for creating a file
        valid_subject_line = "".join(c if c.isalnum() or c == ' ' else '_' for c in subject_line).rstrip()
        md_filename = f"{valid_subject_line}.md"
        md_filepath = os.path.join(output_dir, md_filename)

        with open(md_filepath, "w", encoding="utf-8-sig") as md_file:
            md_file.write(body_text)

            if slide["images"]:
                md_file.write("\n\n")
                for image in slide["images"]:
                    md_file.write(f"![[{image}]]\n")

def main():
    # Set the input directory path where the PPTX files are stored.
    input_directory = "Inputs"
    base_output_dir = "pptx_to_obsidian"
    os.makedirs(base_output_dir, exist_ok=True)
    figures_output_dir = os.path.join(base_output_dir, "Figures")
    os.makedirs(figures_output_dir, exist_ok=True)
    clear_directory(figures_output_dir)
    notes_output_dir = os.path.join(base_output_dir, "Notes")
    os.makedirs(notes_output_dir, exist_ok=True)

    # Check if the figures_output_dir is writable
    if not check_directory_writable(figures_output_dir):
        print(f"Error: The directory '{figures_output_dir}' is not writable. Aborting.")
        return

    # Check if the notes_output_dir is writable
    if not check_directory_writable(notes_output_dir):
        print(f"Error: The directory '{notes_output_dir}' is not writable. Aborting.")
        return

    # Initialize an empty list to store the content extracted from each PPTX file.
    contents = []

    # Iterate through the files in the input directory using os.walk.
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            # Check if the file has a '.pptx' extension (case-insensitive).
            if file.lower().endswith(".pptx"):
                # Create the full path of the PPTX file by joining the root directory and the file name.
                pptx_path = os.path.join(root, file)
                # Extract the content (text and images) from the PPTX file using the extract_content function.
                content = extract_content(pptx_path, figures_output_dir)
                # Append the extracted content to the 'contents' list.
                contents.append(content)

    # Combine all slide decks into one
    contents = [slide for slide_deck in contents for slide in slide_deck]

    # # Merge slides based on subject similarity
    # contents = merge_slides(contents, 0.8)

    # # Summarize slide content
    # contents = process_slides(contents, 0.8, 10000)

    # # Find likely links between subjects and other note contents
    # contents = link_slides(contents,0.8)

    # Save slide contents into markdown files
    create_markdown_files(contents, notes_output_dir)

if __name__ == "__main__":
    main()
    print("Done")