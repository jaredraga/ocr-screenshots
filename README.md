# OCR Screenshots Project

# Overview
OCR Screenshots is a computer vision-based project that scans and processes thousands of YouTube comment screenshots and stores the extracted text in a database. It uses image processing techniques to improve text extraction and stores the results in a database. 

It uses Optical Character Recognition (OCR) with `pytesseract` to extract text from images. It also integrates with OpenAI's API for text classification and analysis. 

The application manages data using `duckdb`, allowing for organized storage and easy retrieval of extracted information.

## Features
- **Image Processing**: Uses `PIL` to preprocess images for better OCR results.
- **Optical Character Recognition**: Implements `pytesseract` for extracting text from images.
- **Database Integration**: Utilizes `duckdb` to manage and store OCR results in a SQLite database.
- **OpenAI Integration**: Connects to OpenAI's API for advanced text processing and classification.
- **User Interaction**: Monitors keyboard input for user commands and controls the program flow.

## Functionalities
1. **Image Preprocessing**: Converts images to grayscale and applies Gaussian blur for optimal OCR performance.
2. **Text Extraction**: Extracts text from images using Tesseract OCR.
3. **Database Management**: Creates and manages a database to store topics and content extracted from images.
4. **OpenAI Chat Completion**: Sends prompts to OpenAI's API for text classification and processing.
5. **Keyboard Monitoring**: Allows users to terminate processes using keyboard shortcuts.

## Setup
- Ensure you have the required libraries installed:
  - `PIL`
  - `pytesseract`
  - `duckdb`
  - `openai`
- Set your OpenAI API key in the `constants.py` file.

## Usage
- Run the main script to start the OCR process and follow the prompts to interact with the application.

## Pipeline
- Use [Numind Classification Model](https://numind.ai/models) to classify comment before putting into database.
