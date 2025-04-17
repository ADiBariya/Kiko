# ai_response.py

import google.generativeai as genai

genai.configure(api_key="AIzaSyC_LICEcED-w3wuk--p1s_8yqyFuYQLH5g")

model = genai.GenerativeModel("gemini-pro")

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text
