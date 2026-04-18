Project Title: AI-Based Road Sign Reflectivity Analyzer

Description:
This application detects the reflectivity of road sign boards, especially during nighttime conditions.

How it Works:
- Detects bright regions (sign boards)
- Extracts region of interest
- Calculates brightness and contrast
- Classifies reflectivity into:
  Good / Moderate / Poor

Technologies Used:
- Python
- OpenCV
- Streamlit

How to Run:
1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   python -m streamlit run app.py

3. Upload an image to test reflectivity.
