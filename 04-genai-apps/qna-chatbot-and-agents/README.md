# GenAI QnA & AI Agents

A collection of Generative AI applications built using **Python, LangChain, Google Gemini, Groq, Streamlit, and LangGraph**. This repository contains practical implementations of conversational AI, AI agents, web search, streaming responses, and LLM-powered applications.

## 🚀 Projects

### 1. QnA Chatbot — Google Gemini

**File:** `1_qna_bot.py`

A conversational AI chatbot built with **LangChain, Google Gemini, and Streamlit**.

**Features:**

* Interactive chat interface
* Google Gemini LLM integration
* Conversation history using Streamlit session state
* Real-time AI responses
* Simple and user-friendly UI

**Technologies:**

* Python
* LangChain
* Google Gemini
* Streamlit

**Run:**

```bash
python -m streamlit run 1_qna_bot.py
```

---

### 2. Google Search AI Agent

**File:** `2_google_agent.py`

An AI agent that can use a **Google search tool** to retrieve information from the web and provide responses based on the search results.

**Features:**

* Agent-based architecture
* Google search tool integration
* LLM-powered reasoning
* Interactive command-line interface
* Tool calling

**Technologies:**

* Python
* LangChain
* LangGraph
* Google Gemini
* Google Search

**Run:**

```bash
python 2_google_agent.py
```

---

### 3. Groq QnA Chatbot

**File:** `3_qna_bot_with_groq.py`

A conversational AI application using **Groq-powered LLMs** with LangGraph-based conversation handling and streaming responses.

**Features:**

* Groq LLM integration
* Conversational memory
* Streaming AI responses
* LangGraph agent workflow
* Streamlit chat interface

**Technologies:**

* Python
* LangChain
* LangGraph
* Groq
* Streamlit

**Run:**

```bash
python -m streamlit run 3_qna_bot_with_groq.py
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/NidhiMehta1444/GenAI-QnA-Chatbot.git
```

Navigate to the project:

```bash
cd GenAI-QnA-Chatbot
```

Create and activate a virtual environment:

```bash
python -m venv env
```

Windows:

```bash
.\env\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project environment and add your API keys:

```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

**Never commit `.env` or API keys to GitHub.**

---

## 📁 Repository Structure

```text
GenAI-QnA-Chatbot/
│
├── 1_qna_bot.py
├── 2_google_agent.py
├── 3_qna_bot_with_groq.py
├── README.md
├── .gitignore
└── requirements.txt
```

---

## 🎯 Learning Objectives

This repository demonstrates practical implementation of:

* Large Language Models (LLMs)
* Generative AI applications
* LangChain
* LangGraph
* Prompt engineering
* Conversational AI
* AI agents
* Tool calling
* Web search integration
* Streaming responses
* Streamlit applications
* API integration

---

## 🔮 Future Improvements

* Add Retrieval-Augmented Generation (RAG)
* Add document-based question answering
* Add vector database integration
* Add authentication
* Improve conversation memory
* Deploy applications using Streamlit
* Add evaluation and monitoring
* Add additional AI agents and tools

---

## 👩‍💻 Author

**Nidhi Mehta**

This repository is part of my hands-on learning and portfolio work in **Generative AI, Machine Learning, and AI Engineering**.
