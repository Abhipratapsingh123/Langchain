from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

document=[
    "Delhi is the capital of India",
    "Kolakat is the capital of Westbengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(document)

print(len(result))
print(len(result[0])) 
print(result[0][:10])
