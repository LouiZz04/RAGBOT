# RAGBot with LangGraph

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangGraph](https://img.shields.io/badge/LangGraph-Powered-blue)](https://langchain-ai.github.io/langgraph/)

**RAGBot** is a robust, self-correcting Retrieval-Augmented Generation (RAG) system designed to chat with complex PDF documents.

Unlike simple RAG bots, this project handles **Multimodal Content**—it reads text, parses tables, and even "sees" images using Vision AI. It uses **LangGraph** to create a smart workflow that checks its own answers, rephrases ambiguous questions, and ensures it doesn't hallucinate.

## 🌟 Key Features

-   **Multimodal PDF Parsing**: Uses `unstructured` to extract text, tables, and images.
-   **Vision Capabilities**: Uses **Llama-4-Scout** to look at diagrams/images in PDFs and describe them for search.
-   **Self-Correcting Pipeline**:
    -   **Query Rephrasing**: Rewrites user questions to be better search terms.
    -   **Relevance Grading**: Checks if retrieved documents actually answer the question.
    -   **Hallucination Check**: Ensures the final answer is grounded in facts.
-   **Vector Search**: Uses **ChromaDB** for finding the right context.

## 🛠️ Technology Stack

This project is built as a full-stack web application:

### Backend (Python)
-   **FastAPI**: High-performance API framework.
-   **LangGraph & LangChain**: For orchestrating the complex AI workflows.
-   **ChromaDB**: Local vector database for semantic search.
-   **Unstructured**: For heavy-duty PDF processing (OCR, partitioning).
-   **Groq API**: For ultra-fast inference with Llama models.

### Frontend (React)
-   **React + Vite**: Fast, modern UI.
-   **Markdown Support**: Beautifully rendered AI answers.

### Infrastructure
-   **Docker & Docker Compose**: Full containerization for easy deployment.

---

## 🚀 Installation & Usage

You don't need to install Python, Node.js, or system libraries (OCR, Poppler) manually. We use Docker to package everything.

### 1. Prerequisites
-   **Docker** & **Docker Compose** installed.
-   A **Groq API Key** (get one [here](https://console.groq.com)).

### 2. Setup
Clone the repository:
```bash
git clone https://github.com/LouiZz04/RAGBOT.git
cd RAGBOT
```

Create a deeply secret file named `.env` in the root folder:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run
Start the entire system with one command:
```bash
docker compose up --build -d
```
*(Note: If you are on Linux and haven't configured user permissions, you might need `sudo docker compose up ...`)*

### 4. Access
-   **Frontend (Chat UI)**: [http://localhost:5174](http://localhost:5174)
-   **Backend (API Docs)**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛑 Stopping
To stop the application:
```bash
docker compose down
```

---

## 🧠 Architecture
The LangGraph workflow visualization:

![Graph Architecture](assets/graph_architecture.png)
