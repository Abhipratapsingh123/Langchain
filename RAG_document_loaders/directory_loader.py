from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader= DirectoryLoader(
    path="Langhcain_document_loaders\\directory_reader",
    glob="*.pdf" ,# to define which files to load, all pdf file in this case
    loader_cls=PyPDFLoader
    
)
docs = loader.load()

print(docs[328].page_content)
print(docs[328].metadata)


# problems = take time to load, Load all pdfs in memory at once
# solution = lazy_load() -> gives a generator of documents(load one by one)