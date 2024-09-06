# Import necessary libraries for the app
import streamlit as st  # type: ignore # Streamlit is used for building the web interface
import google.generativeai as genai  # type: ignore # Google Generative AI (Gemini) API for AI-based content generation
import os  # Provides a way to interact with the operating system for environment variables and file handling
import re  # Regular expressions, used for string pattern matching
from dotenv import load_dotenv  # type: ignore # Loads environment variables from a .env file
from pathlib import Path  # Helps in working with file system paths
import tempfile  # Used for creating temporary files
import base64  # Encodes and decodes data in Base64, often used for image handling

# Step 1: Load environment variables
# Load environment variables from the .env file into the app's environment
load_dotenv()
# Get the API key from environment variables for the Gemini API
api_key = os.getenv("GEMINI_API_KEY")

# Step 2: Configure the Gemini API
# Initialize the Google Gemini AI API with the provided API key
genai.configure(api_key=api_key)

# Step 3: Define a function to sanitize file names
# Function to sanitize file names by removing unsupported characters
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

# Step 4: Define a function to convert an image to Base64 format
# Function to convert an image file to a Base64 string for embedding in HTML
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Step 5: Convert the logo image to Base64
# Path to the logo image used in the app's sidebar

logo_path = "imgs/log.png"


# Convert the logo image to Base64 for embedding in the Streamlit sidebar
logo_base64 = image_to_base64(logo_path)

# Step 6: Create the Streamlit App UI
# Main title for the app displayed at the top of the Streamlit page
st.title("AI Quick SUMMARIES")

# Step 7: Create the Sidebar with the logo and instructions
# Sidebar: Display the logo image centered using HTML and CSS in Streamlit
st.sidebar.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{logo_base64}" width="150" alt="Logo">
    </div>
    """, unsafe_allow_html=True
)

# Sidebar: Instructions for users on how to use the app and supported file types
st.sidebar.markdown("""
This Application Uses For Summarize Types Of Including File And Text To Receive A Concise Summary

**Supported File Types:**
PDF, JPEG, JPG, PNG, TXT

**How To Use:**

1. Choose An Input Method: Upload File Or Input Text.
2. For File Uploads, Select A File Type From The Supported List.
3. Enter The Text Or Upload A File To Get A Summary.
4. View The Generated Summary Or Description.
""")

# Step 8: Create a file upload or text input option
# Sidebar: Allow the user to choose between uploading a file or inputting text
file_option = st.sidebar.radio("**Choose an input method:**", ("Upload File", "Input Text"))

# Step 9: If file upload is selected, process the file
if file_option == "Upload File":
    # If the user selects file upload, allow them to choose a file
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "jpeg", "png", "txt"])
    
    if uploaded_file:
        with st.spinner('Processing your file...'):
            # Create a temporary file to store the uploaded content
            with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                tmp_file.write(uploaded_file.getbuffer())  # Write the uploaded file's buffer to the temp file
                tmp_file_path = tmp_file.name  # Get the path of the temporary file

            # Step 10: Determine the MIME type based on file extension
            file_extension = Path(tmp_file_path).suffix.lower()
            mime_type = {
                ".pdf": "application/pdf",
                ".jpeg": "image/jpeg",
                ".jpg": "image/jpeg",
                ".png": "image/png",
                ".txt": "text/plain"
            }.get(file_extension, "application/octet-stream")

            # Step 11: Handle unsupported file types
            # If file type is unsupported, show an error message
            if mime_type == "application/octet-stream":
                st.error(f"Unsupported file type: {file_extension}")
            else:
                # Step 12: Upload the file to Google Generative AI API (Gemini)
                sample_file = genai.upload_file(path=tmp_file_path, display_name=Path(tmp_file_path).name)
                st.success(f"File '{sample_file.display_name}' uploaded successfully.")
                
                # Initialize the AI model for generating content
                model = genai.GenerativeModel(model_name="gemini-1.5-pro")
                prompt = ""

                # Step 13: Set different prompts based on file type
                if file_extension == ".pdf":
                    prompt = "Summarize this PDF document, providing a brief overview and main points of the PDF. If the response is too brief or too detailed, refine the concise version."
                elif file_extension in [".jpeg", ".jpg", ".png"]:
                    prompt = "Describe or summarize this image, providing a brief overview and main points of the image. If the response is too brief or too detailed, refine the concise version."
                elif file_extension == ".txt":
                    prompt = "Summarize this text file, providing a brief overview and main points of the text. If the response is too brief or too detailed, refine the concise version."

                # Step 14: Generate AI-based content using the provided file and prompt
                response = model.generate_content([sample_file, prompt], request_options={"timeout": 600})
                
                # Step 15: Display the summary or description in the main section
                st.write("### Summary")
                st.write(response.text, language="Markdown")

            # Step 16: Clean up the temporary file after use
            os.remove(tmp_file_path)

# Step 17: If text input is selected, process the text
elif file_option == "Input Text":
    # Allow the user to input text directly
    text_input = st.chat_input("Enter your text here:")
    
    if text_input:
        with st.spinner('Generating summary...'):
            # Initialize the AI model for text summarization
            model = genai.GenerativeModel(model_name="gemini-1.5-pro")
            prompt = "Summarize this text, providing a brief overview and main points. If the response is too brief or too detailed, you might refine the concise version."
            
            # Generate AI-based summary from the input text
            response = model.generate_content([text_input, prompt], request_options={"timeout": 600})
            
            # Display the summary
            st.write("### Summary")
            st.write(response.text, language="Markdown")

# Step 18: Provide fallback message if no input method is selected
else:
    st.write("Please select an input method from the sidebar.")
