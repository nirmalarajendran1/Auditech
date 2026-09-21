# llm_factory.py
import google.generativeai as genai
import os

# PASTE YOUR GOOGLE API KEY HERE
MY_API_KEY = "AIzaSyDjCa90qturSqL0wXslQIvsOhXkObyLWYU"

# Configure the Google Library
genai.configure(api_key=MY_API_KEY)

def ask_ai(sys_instruction, user_prompt):
    """
    Sends a prompt to Google Gemini (Native) and returns the text.
    """
    try:
        # We use the standard free model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Combine system instruction and user prompt for best results
        full_prompt = f"{sys_instruction}\n\nTask: {user_prompt}"
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error connecting to AI: {e}"