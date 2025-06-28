# Langchain RAG-based Chatbot using Gemini

This project is a FastAPI-based chatbot that leverages **Langchain**, **FAISS**, and **Google Gemini** to create a Retrieval-Augmented Generation (RAG) system. It allows users to upload PDF documents and ask questions based on the content of those documents.

---

## 🚀 Features

- Upload PDF files and convert them into vector embeddings
- Store embeddings using **FAISS**
- Chat interface to query uploaded content
- Integration with **Google Gemini API**
- Modular and extensible architecture
- Built with **FastAPI**

---

## 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- Langchain
- FAISS
- Sentence Transformers (`all-MiniLM-L6-v2`)
- Google Generative AI (`gemini-1.5-flash`)
- dotenv for environment variable management

---

## 📂 Project Structure

.
├── main.py # FastAPI entrypoint
├── Upload_file.py # Handles file upload, PDF processing, FAISS creation
├── .env # Stores Gemini API Key (not tracked in Git)
├── .gitignore # Ignores .env, FAISS folder, uploads
├── requirements.txt # Dependencies
├── Uploaded_file/ # Uploaded PDFs (ignored)
├── Faiss_vdb/ # FAISS vector DB storage (ignored)
└── README.md


---

## 📦 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/Nikhilmishra52/Langchain-RAG-based-on-Gemini.git
   cd Langchain-RAG-based-on-Gemini
Create and activate virtual environment

python -m venv venv
venv\Scripts\activate  # On Windows
Install dependencies

pip install -r requirements.txt

Set up your .env file


Gemini_key=your_google_gemini_api_key

Run the app

uvicorn main:app --reload

📬 API Endpoints

POST /upload/

Upload a PDF and create a FAISS index.

POST /chat/

Query the indexed document with a question.

Sample request body:


{
  "query": "What are the technical skills mentioned?"
}

📄 License
This project is licensed under the MIT License.
Feel free to use and customize!

👨‍💻 Author
Nikhil Mishra
GitHub
