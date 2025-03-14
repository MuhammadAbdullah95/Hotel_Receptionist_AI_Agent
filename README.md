# 🏨 Hotel Receptionist Chatbot

Welcome to the **Hotel Receptionist Chatbot** project — an AI-powered virtual receptionist designed to handle frequently asked questions (FAQs) from hotel guests. Built with **Haystack** for natural language processing (NLP) and **FastAPI** for backend services, this chatbot offers a seamless and interactive experience for users, mimicking a real hotel concierge.

---

## 📁 Table of Contents

1. [Project Overview](#project-overview)  
2. [Technical Architecture](#technical-architecture)  
3. [Tech Stack](#tech-stack)  
4. [Features](#features)  
5. [Setup and Installation](#setup-and-installation)  
6. [Usage](#usage)  
7. [Contributing](#contributing)  
8. [Acknowledgments](#acknowledgments)  

---

## 🚀 Project Overview

The **Hotel Receptionist Chatbot** uses **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers to user queries. It combines **retrieval** and **generation** techniques for optimal responses.

### Key Components:
- **Hugging Face Embeddings Model**: Generates embeddings from a predefined dataset (`FAQs.txt`) to retrieve relevant information.
- **Gemini Model**: Refines and generates human-like, contextually accurate responses.

This chatbot is designed to be both **intelligent** and **visually appealing**, reflecting the ambiance of a luxurious hotel environment.

---

## 🛠 Technical Architecture

The system is structured as follows:

### 1. **Frontend**:
- Responsive and elegant chat interface using **HTML**, **CSS**, and **JavaScript**.
- **Bootstrap** for responsive UI components.
- **SweetAlert2** for attractive and user-friendly alert messages.

### 2. **Backend**:
- Built on **FastAPI** for high-performance API management.
- Handles chat queries, invokes NLP pipeline, and returns refined answers.

### 3. **AI Pipeline**:
- **Hugging Face Embeddings Model**: Retrieves relevant data from FAQs.
- **Gemini Model**: Generates natural and polished responses.
- **Haystack RAG pipeline** to integrate retrieval and generation seamlessly.

---

## ⚙️ Tech Stack

| Technology      | Description                                     |
|-----------------|-------------------------------------------------|
| **Haystack**    | NLP framework for document retrieval & QA.      |
| **FastAPI**     | High-performance Python backend framework.     |
| **HTML/CSS/JS** | Frontend structure and interactivity.           |
| **Bootstrap**   | Responsive, modern UI components.               |
| **SweetAlert2** | Beautiful and responsive alert modals.          |

---

## ✨ Features

- **Interactive Chat Interface**: Real-time conversations with a chatbot.
- **AI-Powered, Context-Aware Responses**: High-quality, intelligent replies using RAG.
- **Luxurious Design**: Chat interface mimicking hotel lobby ambiance.
- **Error Handling**: Graceful error messages for unrecognized queries.
- **Fully Responsive**: Works seamlessly across devices.

---

## ⚙️ Setup and Installation

### ✅ Prerequisites
- **Python 3.7+**
- **pip** (Python package manager)

---

### 📥 Installation Steps

1. **Clone the Repository**:
```bash
git clone https://github.com/MuhammadAbdullah95/Hotel_Receptionist_AI_Agent.git
cd Hotel_Receptionist_AI_Agent
```

2. **Set Up a Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the FastAPI Server**:
```bash
uvicorn app:app --reload
```

5. **Open the Chatbot Interface**:
- Open `index.html` located in the `templates` folder using any browser.
- Or serve via local server:
```bash
python -m http.server
```
- Visit `http://localhost:8000` in your browser.

---

## 💬 Usage

### 1. **Open the Chatbot Interface**:
- Launch `index.html` or navigate to the hosted URL.

### 2. **Start Chatting**:
- Type your question in the chatbox and hit **Send** or press **Enter**.

### 3. **Sample Queries**:
- "What time is check-in?"
- "Do you offer room service?"
- "Is breakfast included in the stay?"

### 4. **View Responses**:
- AI-generated responses appear instantly in a conversational format.

---

## 🤝 Contributing

We welcome contributions! Follow these steps to contribute:

1. **Fork** the repository.
2. **Create a branch** for your feature or bugfix:
```bash
git checkout -b feature-name
```
3. **Commit** your changes:
```bash
git commit -m "Add feature"
```
4. **Push** your branch:
```bash
git push origin feature-name
```
5. **Open a Pull Request** for review.

---

## 🙏 Acknowledgments

- **Haystack**: NLP framework for retrieval and generation.
- **FastAPI**: Backend API framework.
- **Bootstrap**: Beautiful and responsive UI toolkit.
- **SweetAlert2**: For stunning alert dialogs.

---


**Enjoy a seamless hotel experience with our AI Receptionist!** 🌐✨

