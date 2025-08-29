from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Langhcain_document_loaders\c file submission_2.pdf')
docs=loader.load()

print(docs[0].page_content)