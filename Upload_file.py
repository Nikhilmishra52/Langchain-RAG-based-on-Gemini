import os
from langchain_community.vectorstores import FAISS  # updated import
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader

class Upload_file:
    def __init__(self, upload_dir="Uploaded_file", faiss_dir="Faiss_vdb", faiss_index_name="combined_index"):
        self.upload_dir = upload_dir
        self.faiss_dir = faiss_dir
        self.faiss_index_name = faiss_index_name
        self.faiss_path = os.path.join(self.faiss_dir, self.faiss_index_name)

        os.makedirs(self.upload_dir, exist_ok=True)
        os.makedirs(self.faiss_dir, exist_ok=True)

        self.embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    def save_file(self, file):
        file_path = os.path.join(self.upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return file_path

    def process_file(self, file_path):
        # Load and split PDF
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
        chunks = splitter.split_documents(documents)

        # Create new vector store from chunks
        new_store = FAISS.from_documents(chunks, self.embeddings)

        # If index already exists, load and merge
        if os.path.exists(self.faiss_path):
            existing_store = FAISS.load_local(
                folder_path=self.faiss_path,
                embeddings=self.embeddings,
                allow_dangerous_deserialization=True
            )
            existing_store.merge_from(new_store)
            existing_store.save_local(self.faiss_path)
        else:
            new_store.save_local(self.faiss_path)

        return self.faiss_path







