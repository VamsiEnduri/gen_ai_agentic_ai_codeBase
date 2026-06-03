# be code with python + fastapi + langchain

from fastapi import FastAPI,UploadFile
import shutil
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
app =FastAPI()

embedding_model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

@app.get("/")
def home():
    return {
        "msg":"welcome to backend"
    }


@app.post("/uploads")
def receive_incoming_file(file:UploadFile):

    #file creation and storing data
    with open(file.filename,"wb") as fi:
        shutil.copyfileobj(file.file,fi)

    #file loading
    loader=PyPDFLoader(file.filename)    
    # pdf load ayyi loader var lo undi 

    # our pdf into mul small docs
    docs=loader.load() 



    #RecursiveCharacterTextSplitter used to create ratio obj for a chunk
    ratio=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    # ALL chunks here
    chunks=ratio.split_documents(docs)

    #embedding model create + Chroma use + embeedingmodel+chunks = vectors chr__ folder store chesam
    Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chr__"
    )

    return {
        "msg":"PDF uploaded and all chunks stored in vectorDb successfully.."
    }
