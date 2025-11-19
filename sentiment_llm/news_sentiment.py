import google.generativeai as genai 
import os 
from dotenv import load_dotenv 
load_dotenv() 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 
llm = genai.GenerativeModel("gemini-2.5-flash-lite") 
prompt = "Hello, how r u" 
response = llm.generate_content(prompt)
print(response)