AI-Powered Medical Image Analyzer 🩺
An advanced AI system designed to assist healthcare professionals in analyzing medical images such as X-rays, CT scans, MRIs, and ultrasounds using Google's Gemini AI.
⚠️ Important Disclaimer
This tool is designed to assist healthcare professionals and is NOT a substitute for certified radiologists or medical doctors. All diagnoses and treatment decisions must be made by qualified healthcare professionals.
Features

🔍 Detailed medical image examination
🧠 AI-powered disease detection and analysis
📋 Structured clinical insights
🔒 Privacy-focused design
⚡ Real-time analysis with confidence levels

Installation

Clone the repository:

bashgit clone https://github.com/yourusername/medical-image-analyzer.git
cd medical-image-analyzer

Install dependencies:

bashpip install -r requirements.txt

Set up your Google API key:

Get a Gemini API key from Google AI Studio
Create a .env file in the project root:



bashGOOGLE_API_KEY="your_api_key_here"
Usage

Run the Streamlit app:

bashstreamlit run main.py

Open your browser to http://localhost:8501
Upload a medical image (PNG, JPEG, JPG formats supported)
Click "Generate Image Analysis" to get AI insights

Supported Image Types

X-rays
CT scans
MRI images
Ultrasound images

Technology Stack

Frontend: Streamlit
AI Model: Google Gemini 2.5 Flash
Image Processing: Pillow
Environment Management: python-dotenv

Security Features

API keys stored in environment variables
No medical data is stored permanently
Privacy-focused design

Contributing
Pull requests are welcome! Please ensure you follow medical AI ethics guidelines.
License
This project is for educational and assistive purposes only.

Note: Always consult qualified medical professionals for actual diagnosis and treatment.