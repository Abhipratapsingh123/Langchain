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

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt|model|parser

result = chain.invoke({'question':'What is Langchain?','text':docs[0].page_content})
print(result)