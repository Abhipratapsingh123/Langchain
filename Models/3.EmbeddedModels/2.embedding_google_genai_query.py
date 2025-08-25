from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

# no dimension paramtern, return 768 by default
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

result = embedding.embed_query("Delhi is the capital of India")

print(len(result))

print(result[:10])