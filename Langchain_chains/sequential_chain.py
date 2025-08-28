from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


prompt1 = PromptTemplate(
    template="Generate detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a 5 point summary from the following text \n{text}",
    input_variables=['text']
)

parser=StrOutputParser()

chain = prompt1|model|parser|prompt2|model|parser

result = chain.invoke({'topic':'Unemployment in India'}) 

print(result)

# visualising chain
chain.get_graph().print_ascii()

