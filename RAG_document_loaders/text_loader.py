from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# prompt
prompt = PromptTemplate(
    template="Write a summary for the folliwinf poem \n{poem}",
    input_variables=['poem']
)

parser = StrOutputParser()


loader = TextLoader("Langhcain_document_loaders\\cricket.txt",encoding='utf-8')

docs = loader.load()

chain = prompt|model|parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)

