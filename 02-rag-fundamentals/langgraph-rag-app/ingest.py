import glob
import os

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

DOCS_DIR = os.path.join(os.path.dirname(__file__),"sample_docs")
INDEX_DIR= os.path.join(os.path.dirname(__file__),"faiss_index")
CHUNK_SIZE=500
CHUNK_OVERLAP=50

def load_and_split(docs_dir):
    chunks=[]
    for path in glob.glob(os.path.join(docs_dir, "*.txt")):
        with open(path,"r",encoding="utf-8") as f:
            text=f.read()
        source=os.path.basename(path)
        paragraphs=[p.strip() for p in text.split("\n\n") if p.strip()]
        current=""
        for para in paragraphs:
            if len(current)+len(para)+2 <=500:
                current=(current + "\n\n" + para).strip()
            else:
                if current:
                    chunks.append(Document(page_content=current, metadata={"source":source}))
                current = para
        if current:
            chunks.append(Document(page_content=current,metadata={"source":source}))
    return chunks

def main():
    print("Loading and Splitting documents...")
    chunks=load_and_split(DOCS_DIR)
    print(f"Split into {len(chunks)} chunks")

    print("Embedding and building FAISS index...")
    embeddings=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    vectorstore=FAISS.from_documents(chunks,embeddings)
    vectorstore.save_local(INDEX_DIR)

    print(f"Done! Index saved to {INDEX_DIR}/")
    print(f" Total chunks indexed:{len(chunks)}")

if __name__ =="__main__":
    main()
