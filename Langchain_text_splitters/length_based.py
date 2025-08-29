from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Langhcain_document_loaders\c file submission_2.pdf')
docs = loader.load()


splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0, # 10-20% considered good
    separator=''
)

result = splitter.split_documents(docs)

print(result[0].page_content)

