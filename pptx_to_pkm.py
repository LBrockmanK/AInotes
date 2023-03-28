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


# Function to merge and summarize two slides
def merge_and_summarize_slides(slide1, slide2):
    # Combine the text content of both slides by concatenating them with a space in between.
    combined_text = slide1["text"] + " " + slide2["text"]

    # Summarize the combined text using the pre-trained summarization model.
    # `summarizer(combined_text)` feeds the combined text to the summarization pipeline.
    # `max_length=100` sets the maximum length of the generated summary (in tokens).
    # `do_sample=False` ensures that the model generates the most likely summary
    # rather than sampling from the probability distribution of possible summaries.
    # The summarizer returns a list of dictionaries, with each dictionary containing the
    # generated summary text under the key "summary_text".
    # `[0]["summary_text"]` retrieves the summary text from the first dictionary in the list.
    summary = summarizer(combined_text, max_length=100, do_sample=False)[0]["summary_text"]

    # Create a new slide dictionary with the summarized text and merged image list.
    # The merged image list is created by concatenating the image lists of both input slides.
    merged_slide = {"text": summary, "images": slide1["images"] + slide2["images"]}

    # Return the merged and summarized slide.
    return merged_slide

# Function to process and merge similar slides in a content list
def process_slides(content, similarity_threshold):
    # Initialize an empty list to store the merged content.
    merged_content = []

    # Loop through the content list until it's empty.
    while content:
        # Pop the first slide from the content list and set it as the current slide.
        current_slide = content.pop(0)
        # Initialize a flag to indicate if a similar slide has been found.
        found_similar_slide = False

        # Iterate through the remaining slides in the content list using their index and value.
        for i, slide in enumerate(content):
            # Calculate the similarity between the current slide and the slide from the content list.
            # If the similarity score is greater than the specified threshold, the slides are considered similar.
            if similarity(current_slide["text"], slide["text"]) > similarity_threshold:
                # Merge and summarize the similar slides using the merge_and_summarize_slides function.
                merged_slide = merge_and_summarize_slides(current_slide, slide)
                # Append the merged slide to the merged_content list.
                merged_content.append(merged_slide)
                # Remove the similar slide from the content list to avoid duplicate processing.
                content.pop(i)
                # Set the found_similar_slide flag to True to indicate that a similar slide has been found and processed.
                found_similar_slide = True
                # Break out of the loop since a similar slide has been found and there's no need to check the remaining slides.
                break

        # If no similar slide has been found, append the current slide to the merged_content list as-is.
        if not found_similar_slide:
            merged_content.append(current_slide)

    # Return the processed and merged content list.
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

    # Create the output directory and Figures subdirectory if they don't exist.
    

    # Iterate through the slides in the presentation using their index and value.
    for slide_num, slide in enumerate(prs.slides):
        # Initialize a dictionary to store the text and images for each slide.
        slide_content = {"text": "", "images": []}

        # Iterate through the shapes in each slide.
        for shape in slide.shapes:
            # Check if the shape has a text frame and append its text to the slide_content dictionary.
            if shape.has_text_frame:
                slide_content["text"] += shape.text

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


    # Set a similarity threshold for merging slides.
    similarity_threshold = 0.8
    # Initialize an empty list to store the processed content after merging similar slides.
    processed_contents = []

    # Process and merge similar slides in each PPT using the process_slides function.
    for content in contents:
        processed_content = process_slides(content, similarity_threshold)
        # Append the processed content to the 'processed_contents' list.
        processed_contents.append(processed_content)

    # Check if there is more than one PPTX file processed.
    if len(processed_contents) > 1:
        # Combine the processed content from all PPTX files into a single list.
        combined_content = [slide for content in processed_contents for slide in content]
        # Process and merge similar slides in the combined content list.
        final_content = process_slides(combined_content, similarity_threshold)
    else:
        # If there's only one PPTX file processed, set the final content to its processed content.
        final_content = processed_contents[0]

    print(final_content)
    # TODO: Add code here to create links in obsidian format
    # TODO: Add code here to create Markdown files for Obsidian using final_content

if __name__ == "__main__":
    #TODO: Need to clean out the leftovers of the previous attempt before we start and make sure they all go into a sub folder
    main()
    print("Done")