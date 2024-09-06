# AI Quick Summaries

AI Quick Summaries is a Streamlit-based web application that leverages Google's Gemini Generative AI to provide quick and concise summaries of different types of input files (PDF, images, text) and user-provided text. This app allows users to upload files or input text and get a summary or description using the power of AI.

## Features

- **Summarize Files**: Supports PDF, JPEG, JPG, PNG, and TXT files.
- **Text Summarization**: Users can input raw text to get a concise summary.
- **User-Friendly Interface**: Simple, easy-to-use interface with a sidebar for file uploads or text input.
- **AI-Powered Summaries**: Uses Google Generative AI (Gemini) to generate high-quality summaries or descriptions.
- **File Type Handling**: Automatically detects file type and generates relevant content based on the file format (e.g., summarizing PDFs, describing images).

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.11.9 +
2. **Required Python libraries** (installed via `pip`):
   - `streamlit`
   - `google-generativeai`
   - `python-dotenv`
   - `re`
   - `pathlib`
   - `tempfile`
   - `base64`

You also need to set up a `.env` file to store your API key for Google Generative AI.

### Example `.env` file:


git clone https://github.com/sureshbeekhani/ai-quick-summaries.git
cd ai-quick-summaries

