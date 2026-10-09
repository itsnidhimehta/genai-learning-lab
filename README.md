# 🧪 GenAI Learning Lab

My hands-on path through Generative AI, from a first LLM call to multi-agent systems. It covers LangChain, RAG, LangGraph and agents.

These are **learning experiments**, organised in the order I built them. My production-style, deployed projects live in separate repos (see [Flagship projects](#-flagship-projects) below).

## 🗺️ Learning path

| Stage | Folder | What I practised |
|---|---|---|
| 1 | [`01-langchain-foundations`](01-langchain-foundations) | LLM calls (OpenAI, Groq, Ollama), prompt templates and chains, chat memory, structured output with Pydantic, streaming, basic tool-using agents, a web-search agent |
| 2 | [`02-rag-fundamentals`](02-rag-fundamentals) | Loading documents, text splitting, embeddings and vector stores, a RAG agent, plus three small RAG apps |
| 3 | [`03-langgraph-agents`](03-langgraph-agents) | LangGraph nodes and state, agentic RAG, human-in-the-loop approval, multi-agent collaboration, a blog-writing agent |
| 4 | [`04-genai-apps`](04-genai-apps) | Streamlit Q&A chatbots and agents (Gemini, Groq, SQL agent, RAG agent, LangGraph bot) |

### Stage 2 – RAG apps
- [`rag-document-qa`](02-rag-fundamentals/rag-document-qa): document Q&A over text and PDF files, with an experiment using Typesense search
- [`langgraph-rag-app`](02-rag-fundamentals/langgraph-rag-app): RAG with FAISS, orchestrated as a LangGraph graph
- [`rag-with-graph`](02-rag-fundamentals/rag-with-graph): a notebook version of graph-based RAG

### Stage 3 – LangGraph agents
1. [`01-langgraph-basics`](03-langgraph-agents/01-langgraph-basics): nodes, edges, state, and a Q&A bot
2. [`02-agentic-rag`](03-langgraph-agents/02-agentic-rag): an agent that decides when to retrieve documents
3. [`03-human-in-the-loop`](03-langgraph-agents/03-human-in-the-loop): pausing the graph for a human decision
4. [`04-multi-agent`](03-langgraph-agents/04-multi-agent): several specialised agents working together
5. [`05-blog-generator-agent`](03-langgraph-agents/05-blog-generator-agent): a multi-step writing agent

## 🚀 Flagship projects

These grew out of the lab and are deployed live:

| Project | What it is | Live demo |
|---|---|---|
| [Enterprise RAG Platform](https://github.com/itsnidhimehta/enterprise-rag-platform) | Document Q&A with source citations | [Open app](https://enterpriserag-platform.streamlit.app/) |
| [AI Email Assistant](https://github.com/itsnidhimehta/ai-email-assistant) | Email writer with human-in-the-loop review (LangGraph) | [Open app](https://nidhi-email-assistant.streamlit.app/) |
| [AI SQL Task Management Agent](https://github.com/itsnidhimehta/AI-SQL-Task-Management-Agent) | Natural-language task management over SQLite | [Open app](https://sql-task-agent.streamlit.app/) |

## ▶️ Running the notebooks

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install langchain langchain-community langgraph langchain-groq langchain-openai python-dotenv jupyter
```

Create a `.env` file with the API keys a notebook uses (for example `GROQ_API_KEY`, `OPENAI_API_KEY`, `GOOGLE_API_KEY`). Some sub-projects have their own `requirements.txt` or `pyproject.toml`; use those when present.

Sample data in the `data/` folders is synthetic and made for practice. Vector-store files are not committed; the notebooks rebuild them.

## 📌 History

This repo consolidates nine earlier repositories (GenAI-LangChain-Notebooks, RAG-document-question-answering, LangGraph-RAG, RAG-Langraph, Agentic-Rag-LangGraph, LangGraph-Human-In-The-Loop, GenAI-Multi-AI-Agent, LangGraph-Blog-Generator-Agent and GenAI-QnA-Chatbot) into one organised learning path.

---
👩‍💻 **Nidhi Mehta** · [GitHub](https://github.com/itsnidhimehta)
