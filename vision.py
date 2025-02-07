# from dotenv import load_dotenv
# load_dotenv() # Load environment variables from .env file

# import streamlit as st
# import os
# import google.generativeai as genai 
# from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # funnctio to load Gemini Pro Model and get response 
# model = genai.GenerativeModel("gemini-1.5-flash")

# def get_gemini_response(input,image):
#     if input !="":
#         response=model.generate_content([input,image])
#     else:
#         response=model.generate_content(image)
#     return response.text

# #setting streamlit app

# st.set_page_config(page_title="Gemini image Demo")
# st.header("Gemini LLm Application")

# input=st.text_input("Input: ",key="input")


# upload_file = st.file_uploader("Choose an image...", type=["jpg", "png","jpeg"])
# image=""
# if upload_file is not None:
#     image = Image.open(upload_file)
#     st.image(image,caption="Upload image.",use_container_width=True)

# submit = st.button("Tell me about the image")

# # Whwn submit is clicked
# if submit:
#     response=get_gemini_response(input,image)
#     st.subheader("The response is: ") 
#     st.write(response)
#from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image

# Load environment variables

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response from Gemini model
def get_gemini_response(input_text, image):
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit Page Configuration
st.set_page_config(page_title="Gemini Vision", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7f7;
    }
    .stButton>button {
        border-radius: 10px;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 24px;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }
    .stFileUploader {
        border: 2px dashed #4CAF50;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📷 GeminiVision - AI-Powered Image Analyzer 🚀 </h1>", unsafe_allow_html=True)

# Input Section
st.subheader("📝 Enter Text (Optional)")
input_text = st.text_input("Describe what you want to know about the image", key="input")

# Upload Image
st.subheader("📤 Upload an Image")
upload_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
image = None

# Display the image if uploaded
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", width=300)

# Submit Button
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit = st.button("🔍 Analyze Image")

# Process when button is clicked
if submit:
    if not upload_file:
        st.error("⚠️ Please upload an image before analyzing.")
    elif not os.getenv("GOOGLE_API_KEY"):
        st.error("⚠️ API Key missing. Please check your environment variables.")
    else:
        with st.spinner("⏳ Processing... Please wait."):
            response = get_gemini_response(input_text, image)
            st.subheader("💡 AI Response:")
            st.write(response)
