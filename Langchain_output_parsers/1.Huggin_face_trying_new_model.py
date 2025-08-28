from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id = "openai/gpt-oss-20b",
#     task="text-generation"
# )

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


#1st prompt
template1 = PromptTemplate(
    template ="Write a detailed report on  {topic}",
    input_variables=['topic']
)
# 2nd prompt
template2 = PromptTemplate(
    template ="Write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)


prompt1 = template1.invoke({'topic':"black hole"})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result2 = model.invoke(prompt2)

print(result2.content)





