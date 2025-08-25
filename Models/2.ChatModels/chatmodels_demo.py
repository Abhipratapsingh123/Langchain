from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.1)
# temperature --> Decides how creative or random the answer is
# max_tokens param..

p1 = "You are a professional doctor, Now tell me Which medicine I have to take if I have a headache, tell me in less words"

p2 = "Write a 5 line poem on cricket"


response = model.invoke(p2)

print(response.content)
