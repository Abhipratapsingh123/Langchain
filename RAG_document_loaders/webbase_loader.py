from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# prompt
prompt = PromptTemplate(
    template="Answer the following question \n{question} from the following text- {text}",
    input_variables=['question','text']
)

# parser
parser = StrOutputParser()

url = r"https://en.wikipedia.org/wiki/LangChain"
url2 = r"https://www.makemytrip.com/routeplanner/gurgaon-agra.html"
url3 = r"https://www.rome2rio.com/map/Gurgaon/Agra"
loader = WebBaseLoader( url3)

docs = loader.load()

chain = prompt|model|parser
print(docs)
result = chain.invoke({'question':'What is this information about?','text':docs[0].page_content})
print(result)