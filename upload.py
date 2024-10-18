import streamlit as st
import io
from PIL import Image
from openai import OpenAI
import os
import base64



# Initialize OpenAI client
client = OpenAI(api_key=os.environ['GPT'])

st.markdown("# Upload or Capture")


def save_image(image, filename):
    image.save(filename)
    st.write(f"Image saved as {filename}")
    
# Convert PIL image to base64-encoded string
def image_to_base64(image):
    try:
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    except Exception as e:
        st.error(f"Error converting image to base64: {str(e)}")
        return None


# Interpret sign language from an image file
def interpret_sign_language(image_path):
    try:
        # Open the image file in binary mode and send to OpenAI API
        with open(image_path, 'rb') as img_file:
            response = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                      "role": "user",
                      "content": [
                        {"type": "text", "text": "interprete the ASL sign into english"},
                        {
                          "type": "image_url",
                          "image_url": {
                            "url": "asl_sign_image.png",
                          },
                        },
                      ],
                    }
                  ],
                max_tokens=300
            )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error in sign language interpretation: {str(e)}")
        return None


# Translate text to a target language
def translate_text(text, target_language):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Translate the following text to {target_language}: {text}"}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return None


# Image upload or capture with non-empty labels
uploaded_file = st.file_uploader("Choose an image to upload...", type=["jpg", "jpeg", "png"], label_visibility='visible')
camera_input = st.camera_input("Or capture an image using your camera", label_visibility='visible')

# Process the uploaded or captured image
image = None
image_path = "asl_sign_image.png"  # File path to save the image

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    save_image(image, image_path)  # Save uploaded image to file

elif camera_input is not None:
    image = Image.open(camera_input)
    st.image(image, caption='Captured Image.', use_column_width=True)
    save_image(image, image_path)  # Save captured image to file

else:
    st.write("Please upload an image or capture one using your camera.")
    st.stop()

# Interpret the sign language gesture
if st.button('Interpret Sign Language'):
    if image is not None:
        interpretation = interpret_sign_language(image_path)  # Pass file path to the function
        if interpretation:
            st.write("Interpretation:", interpretation)

            # Translation to a selected language
            target_language = st.selectbox(
                "Select the target language for translation:",
                ["Spanish", "French", "German", "Japanese"]
            )
            if st.button("Translate to Target Language"):
                translated_text = translate_text(interpretation, target_language)
                if translated_text:
                    st.write(f"Translated to {target_language}:", translated_text)
    else:
        st.error("No image found. Please upload or capture an image.")
