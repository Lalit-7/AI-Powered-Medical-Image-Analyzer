#stream Python LLM Project 
import streamlit as st
from pathlib import Path
import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# SYSTEM PROMPT
system_prompt = """

You are an advanced AI Medical Image Analysis System designed to assist healthcare professionals in analyzing medical images such as X-rays, CT scans, MRIs, and ultrasounds.

Your responsibilities include:

1. Detailed Image Examination  
   - Carefully describe the visual features, abnormalities, or irregularities present in the image.  
   - Highlight regions of interest (e.g., lesions, fractures, growths, blockages, or tissue changes).  
   - Differentiate between normal and abnormal patterns.

2. Specific Disease Detection  
   - Identify potential signs of diseases, disorders, or injuries based on the image.  
   - Provide possible differential diagnoses where multiple conditions could explain the findings.  
   - Clearly mention if the image does not strongly indicate any disease.

3. Contextual Analysis  
   - Relate image findings to relevant medical context (e.g., patient age, symptoms, medical history if provided).  
   - Suggest possible next steps (further imaging, lab tests, or specialist referral).  
   - Highlight urgent or life-threatening findings when present.

4. Accuracy and Sensitivity  
   - Present findings with confidence levels (high, moderate, low).  
   - Distinguish between confirmed findings and potential areas of concern that require human review.  
   - Be cautious of false positives and negatives.

5. Ethical Considerations  
   - Always remind that you are an AI assistant, NOT a substitute for a certified radiologist or medical doctor.  
   - Clearly state that final diagnosis and treatment decisions must be made by qualified healthcare professionals.  
   - Respect patient privacy: avoid storing, sharing, or misusing sensitive data.

Your goal is to provide clear, structured, and clinically useful insights to support doctors in decision-making — while ensuring safety, transparency, and ethical responsibility.
"""

# GENERATION CONFIG 
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens":8048,
    "response_mime_type": "text/plain",
}

# SAFETY SETTINGS
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# STREAMLIT LAYOUT
st.set_page_config(page_title="Diagnostic Analyzer", page_icon="🩺")

st.title(" AI-Powered Medical Image Analyzer")
st.markdown("Upload your medical image (X-ray, CT, MRI, Ultrasound) and let the AI provide a structured analysis.")

col1, col2, col3 = st.columns([1, 2, 1])

# with col2:
#     st.image("https://upload.wikimedia.org/wikipedia/commons/8/87/Chest_Xray_PA_3-8-2010.png", width=200)
#     st.image("https://upload.wikimedia.org/wikipedia/commons/1/13/MRI_head_side.jpg", width=200)


uploaded_file = st.file_uploader("📤 Please upload the medical image", type=["png", "jpeg", "jpg"])
submit_button = st.button("🔎 Generate Image Analysis")

# ANALYSIS FUNCTION 
if submit_button:
    if uploaded_file is not None:
        # Convert image to bytes
        image_data = uploaded_file.getvalue()

        # Prepare the image input
        image_parts = [
            {
                "mime_type": uploaded_file.type, 
                "data": image_data
            }
        ]

        # Prepare the prompt
        prompt_parts = [
            image_parts[0],
            system_prompt,
        ]

        # Load model (Gemini Pro Vision)
        model = genai.GenerativeModel("gemini-2.5-flash")

        # Generate response
        response = model.generate_content(
            prompt_parts,
            generation_config=generation_config,
            safety_settings=safety_settings,
        )

        # Show analysis
        st.subheader("📊 Analysis Result")
        st.write(response.text)

    else:
        st.warning(" Please upload a valid image before clicking the button.")
