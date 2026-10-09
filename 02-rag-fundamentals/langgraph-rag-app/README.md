# LangGraph RAG Project

## Overview

This project is a simple Retrieval-Augmented Generation (RAG) application built using LangGraph, FAISS, and Large Language Models.

The application can:

* Answer questions about AI and Machine Learning concepts.
* Perform mathematical calculations using tools.
* Search information from local documents using FAISS vector search.

## Technologies Used

* Python
* LangGraph
* LangChain
* FAISS
* Groq LLM
* Google Gemini Embeddings
* dotenv

## Project Structure

* `agent.py` - Defines the LangGraph agent and tools.
* `ingest.py` - Creates the FAISS vector database from documents.
* `app.py` - Runs the chatbot application.
* `sample_docs/` - Contains text documents used for retrieval.
* `faiss_index/` - Stores the generated vector database.

## Setup

1. Clone the repository:

```bash
git clone <repository_url>
cd langgraph-rag
```

2. Install dependencies:

```bash
uv sync
```

3. Add API keys in `.env`:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

4. Build the FAISS index:

```bash
python ingest.py
```

5. Run the application:

```bash
python app.py
```

## Example Questions

* What are transformers?
* Explain Retrieval-Augmented Generation.
* Add 25 and 30.
* Multiply 12 by 8.

## Author

Nidhi Mehta
