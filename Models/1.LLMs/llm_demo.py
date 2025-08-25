from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
import os

# Load environment variables
load_dotenv(dotenv_path='C:\\Users\\abhip\\Desktop\\langchain_models\\.env')

llm = GoogleGenerativeAI(model="gemini-1.5-flash")

response = llm.invoke("Write a short poem about the moon")
print(response)
