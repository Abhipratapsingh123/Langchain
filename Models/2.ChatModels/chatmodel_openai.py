from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load your .env file (where OPENAI_API_KEY is stored)
load_dotenv()

# Initialize OpenAI model (use cheap and fast model)
model = ChatOpenAI(
    model="gpt-4o-mini",   
    temperature=0.1        
)

# Prompts
p1 = "You are a professional doctor. Tell me which medicine I should take if I have a headache. Keep the answer short."
p2 = "Write a 5 line poem on cricket."

# Choose which prompt to send
response = model.invoke(p2)

# Print the model's reply
print(response.content)
