from langchain_community.document_loaders import CSVLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()


loader = CSVLoader(r'Langhcain_document_loaders\Social_Network_Ads.csv')

docs = loader.lazy_load()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# PromptTemplate

prompt = PromptTemplate(
    template = "Give the summary about the data \n {data}",
    input_variables=['data']
)

chain = prompt|model
result = chain.invoke({"data":docs})
print(result)
