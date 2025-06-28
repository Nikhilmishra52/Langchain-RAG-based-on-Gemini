from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from fastapi import UploadFile,File
from pydantic import BaseModel

class chat(BaseModel):
    query :str

from dotenv import load_dotenv
import os
from fastapi import FastAPI

from Upload_file import Upload_file

app = FastAPI()

uploader =Upload_file()

load_dotenv('.env')

Gemini_key = os.getenv('Gemini_key')

os.environ["GOOGLE_API_KEY"] = Gemini_key


#loading pdf

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        file_path = uploader.save_file(file)

        # Process and create FAISS index
        faiss_path = uploader.process_file(file_path)

        return {"status": "success", "faiss_index": faiss_path}
    except Exception as e:
        return {"status": "error", "message": str(e)}

#Creating Chain
# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever= retriever,
#     chain_type = "stuff"
#
# )
#
# query = "can you tell me technical skills of nikhil"
# answer = qa_chain.run(query)
#
# print("Answer:", answer)

@app.post("/chat")
async def chat(que:chat):
    llm=ChatGoogleGenerativeAI(model="models/gemini-1.5-flash",temperature = 0.3)
    retriever = FAISS.load_local(
        folder_path="Faiss_vdb/combined_index",
        embeddings=uploader.embeddings,
        allow_dangerous_deserialization=True
    ).as_retriever(search_type="similarity", k=3)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever = retriever,
        chain_type="stuff"
    )
    data= que.query

    answer = qa_chain.run(data)

    return answer




import uvicorn
if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)