from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpont(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text_generation"
)

model = ChatHuggingFace(llm=llm)

