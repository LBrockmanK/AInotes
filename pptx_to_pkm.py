import os
from pptx import Presentation
from pptx.util import Inches
from PIL import Image
from transformers import AutoTokenizer, AutoModelForSeq2Vec
from transformers import pipeline
import torch
import numpy as np

# Initialize the tokenizer and model for sentence embeddings
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/paraphrase-MiniLM-L6-v2")
model = AutoModelForSeq2Vec.from_pretrained("sentence-transformers/paraphrase-MiniLM-L6-v2")

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

# Function to compute text similarity using sentence embeddings
def similarity(text1, text2):
    # Tokenize the input texts using the pre-trained tokenizer. The tokenizer converts
    # the input texts into a format that can be fed into the pre-trained model.
    # `return_tensors="pt"` specifies that the returned tensors should be PyTorch tensors.
    # `padding=True` ensures that both input tensors have the same length by adding padding tokens.
    # `truncation=True` truncates the input text if it exceeds the model's maximum input length.
    inputs1 = tokenizer(text1, return_tensors="pt", padding=True, truncation=True)
    inputs2 = tokenizer(text2, return_tensors="pt", padding=True, truncation=True)

    # Compute the sentence embeddings for both input texts using the pre-trained model.
    # `with torch.no_grad():` disables gradient calculation to save memory and speed up computation.
    # `model(**inputs1)` feeds the tokenized inputs into the model and computes the embeddings.
    # `.last_hidden_state` retrieves the last hidden state from the model's output.
    # `.mean(dim=1)` calculates the mean of the embeddings along dimension 1 (tokens) to obtain a single embedding vector per input text.
    # `.numpy()` converts the PyTorch tensor to a NumPy array.
    with torch.no_grad():
        embeddings1 = model(**inputs1).last_hidden_state.mean(dim=1).numpy()
        embeddings2 = model(**inputs2).last_hidden_state.mean(dim=1).numpy()

    # Calculate the cosine similarity between the two embeddings.
    # `np.inner(embeddings1, embeddings2)` computes the inner product of the two embedding vectors.
    # `np.linalg.norm(embeddings1)` and `np.linalg.norm(embeddings2)` compute the L2 norms (Euclidean lengths) of the embedding vectors.
    # Dividing the inner product by the product of the norms gives the cosine similarity score.
    similarity_score = np.inner(embeddings1, embeddings2) / (
        np.linalg.norm(embeddings1) * np.linalg.norm(embeddings2)
    )
    # Return the cosine similarity score as a scalar value (the [0][0] element of the resulting array).
    return similarity_score[0][0]

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

# Function to extract text and images from a PPTX file
def extract_content(pptx_file):
    # Read the PPTX file using the python-pptx library and store it in the variable 'prs'.
    prs = Presentation(pptx_file)
    # Initialize an empty list to store the extracted content.
    content = []

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
            if shape.has_image:
                # Store the image object in the variable 'image'.
                image = shape.image
                # Create an image file path using the slide number, shape name, and image file extension.
                image_path = f"slide_{slide_num}_image_{shape.name}.{image.ext}"
                # Write the image binary data (blob) to a new image file with the created file path.
                with open(image_path, "wb") as image_file:
                    image_file.write(image.blob)
                # Append the image file path to the slide_content dictionary.
                slide_content["images"].append(image_path)

        # Append the slide_content dictionary to the content list.
        content.append(slide_content)

    # Return the content list containing text and images from the PPTX file.
    return content

def main():
    # Set the input directory path where the PPTX files are stored.
    input_directory = "Inputs"
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
                content = extract_content(pptx_path)
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

    # TODO: Add code here to create links in obsidian format
    # TODO: Add code here to create Markdown files for Obsidian using final_content

if name == "main":
    main()