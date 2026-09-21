import google.generativeai as genai

# Paste your API key here
MY_API_KEY = "AIzaSyDjCa90qturSqL0wXslQIvsOhXkObyLWYU"

genai.configure(api_key=MY_API_KEY)

print("Checking available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")