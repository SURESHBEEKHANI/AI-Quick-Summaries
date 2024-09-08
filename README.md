## AI Quick Summaries

AI Quick Summaries is a simple web application built using Streamlit that allows users to summarize different types of files and text using Google's Gemini Generative AI. The app supports files such as PDFs, images (JPEG, PNG), and text files.

## Features

- **File Summarization**: Upload PDF, JPEG, PNG, or TXT files for a concise AI-generated summary.
- **Text Summarization**: Input text manually and get a brief summary using Google Generative AI.
- **User-Friendly Interface**: A clean, simple interface powered by Streamlit.
- **Supports Multiple File Types**: Handles PDFs, images (JPEG, PNG), and text files.

## Prerequisites

Before running the app, make sure you have the following installed:

- Python 3.7 or higher
- The required Python libraries (Streamlit, Google Generative AI, dotenv, etc.)

### Example `.env` File

Create a `.env` file in the project root with the following content, replacing `your_gemini_api_key_here` with your actual API key:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
Installation and Setup
Step 1: Clone the Repository
Clone the repository using the following command:


git clone https://github.com/sureshbeekhani/ai-quick-summaries.git
cd ai-quick-summaries
Step 2: Install Dependencies
Install the required Python packages using the requirements.txt file:


pip install -r requirements.txt
Step 3: Set Up the Environment Variables
Create a .env file in the root directory of the project and add your Google Gemini API key as follows:


GEMINI_API_KEY=your_gemini_api_key_here
Step 4: Run the Application
Run the Streamlit app with the following command:


streamlit run app.py
This will launch the app in your browser.

How to Use
Select Input Method: Choose between uploading a file or inputting text via the sidebar.

Upload File: Upload a PDF, JPEG, PNG, or TXT file.
Input Text: Input text directly for summarization.
Get a Summary: Once the file is uploaded or text is entered, the app will generate a summary using Google's Gemini AI.

View the Summary: The AI-generated summary or description will appear in the app's main display area.

Supported File Types
PDF: The app will summarize the main points of the document.
JPEG, JPG, PNG: The app will describe the image.
TXT: The app will provide a summary of the text content.
Project Structure

.
├── app.py              # Main Streamlit app
├── .env                # Environment variables for API keys
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── imgs/               # Directory for storing image assets like the logo
Code Overview
Here’s a high-level overview of the main parts of the code:

Import Libraries:

streamlit: For building the app interface.
google.generativeai: For interacting with the Gemini AI.
dotenv: For loading environment variables.
re: For sanitizing file names.
tempfile, pathlib, os, base64: For file handling.
Set Up Environment Variables:

Load the API key from the .env file using load_dotenv() and configure the Gemini API with genai.configure().
File Handling:

The app processes uploaded files and sanitizes their names.
Depending on the file type, it generates appropriate prompts for the Gemini AI.
Image to Base64 Conversion:

Converts the logo image to Base64 for embedding in the sidebar.
Streamlit UI:

The sidebar includes the logo and instructions.
A radio button lets users choose between file uploads and text input.
AI Content Generation:

Based on the file type (PDF, image, or text), it prompts the AI to generate a summary or description.
Dependencies
The app relies on the following dependencies, which are listed in requirements.txt:

Streamlit: For the web interface.
Google Generative AI (Gemini): To generate summaries based on input.
python-dotenv: For handling environment variables.
pathlib, tempfile, os, base64: For file processing and conversion.
You can install these dependencies using the following command:


pip install -r requirements.txt
Known Issues
The app currently supports only PDF, image, and text files. Other file formats may not work as expected.
API limits may apply based on your usage tier for Google Generative AI.
Future Improvements
More File Types: Adding support for DOCX, PPTX, and other common file types.
Custom Summarization Levels: Allow users to choose the level of detail in the summary.
Multilingual Support: Expand the summarization capabilities to multiple languages.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any issues or questions, feel free to reach out:

GitHub: https://github.com/sureshbeekhani


This `README.md` file includes comprehensive installation instructions, usage details, and additiona

