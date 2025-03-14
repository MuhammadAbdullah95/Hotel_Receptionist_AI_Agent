# Hotel Receptionist Chatbot

Welcome to the **Hotel Receptionist Chatbot** project! This is a conversational AI chatbot designed to act as a virtual hotel receptionist, answering frequently asked questions (FAQs) from guests. Built using **Haystack** for natural language processing (NLP) and **FastAPI** for the backend, this chatbot provides a seamless and interactive experience for users.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technical Architecture](#technical-architecture)
3. [Tech Stack](#tech-stack)
4. [Features](#features)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [API Endpoints](#api-endpoints)
8. [Contributing](#contributing)
---

## Project Overview

The **Hotel Receptionist Chatbot** is an advanced AI-powered chatbot designed to act as a virtual hotel receptionist. It uses **Retrieval-Augmented Generation (RAG)** to provide accurate and context-aware responses to user queries. The chatbot leverages two state-of-the-art language models:
1. **Hugging Face Embeddings Model**: For creating embeddings from a predefined dataset (`FAQs.txt`) and retrieving relevant information.
2. **Gemini Model**: For refining the retrieved answers and generating human-like, context-aware responses.

Built with **Haystack** for natural language processing (NLP) and **FastAPI** for the backend, this chatbot offers a seamless and interactive experience for hotel guests.

### Key Features:
- **AI-Powered Responses**: Combines retrieval and generation for accurate and context-aware answers.
- **Dynamic Refinement**: Uses Gemini to refine retrieved answers, ensuring high-quality responses.
- **Interactive Chat Interface**: A user-friendly interface for seamless interaction.
- **Luxurious Design**: A visually appealing design inspired by the ambiance of a hotel lobby.

---

## Technical Architecture

The chatbot is built using the following components:
1. **Frontend**:
   - A responsive and interactive chat interface built with **HTML**, **CSS**, and **JavaScript**.
   - Uses **Bootstrap** for styling and **SweetAlert2** for user-friendly alerts.

2. **Backend**:
   - Built with **FastAPI**, a modern and fast web framework for building APIs.
   - Handles user queries, retrieves relevant information, and generates refined responses.

3. **AI Models**:
   - **Hugging Face Embeddings Model**: Creates embeddings from the `FAQs.txt` file and retrieves relevant information.
   - **Gemini Model**: Refines the retrieved answers to generate context-aware and human-like responses.

4. **RAG Implementation**:
   - Combines retrieval (from embeddings) and generation (using Gemini) to provide accurate and dynamic answers.

---

## Tech Stack

The project is built using the following technologies:

- **Haystack**: A framework for building powerful NLP pipelines. It is used for question-answering and document retrieval.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **HTML/CSS/JavaScript**: For the frontend design and interactivity.
- **Bootstrap**: For responsive and modern UI components.
- **SweetAlert2**: For beautiful and user-friendly alert messages.

---

## Features

1. **Interactive Chat Interface**:
   - Users can type their queries in the chatbox and receive instant responses.
   - Messages are displayed in a conversational format, with user messages on the right and bot messages on the left.

2. **Luxurious Design**:
   - The chatbot interface is designed to resemble a hotel lobby, with warm colors and elegant fonts.

3. **Dynamic Responses**:
   - The chatbot uses Haystack's NLP capabilities to provide accurate and context-aware answers.

4. **Error Handling**:
   - Friendly error messages are displayed if the chatbot cannot generate a response.

---

## Setup and Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MuhammadAbdullah95/Hotel_Receptionist_AI_Agent.git
   cd Hotel_Receptionist_AI_Agent

Set Up a Virtual Environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Run the FastAPI Server:

bash
Copy
uvicorn app:app --reload
Open the Chatbot Interface:

Navigate to index.html in the templates folder or serve it using a local server (e.g., python -m http.server).

Open your browser and go to http://localhost:8000.

Usage
Open the Chatbot:

Launch the chatbot interface in your browser.

Ask Questions:

Type your query in the input box and press Send or hit Enter.

Example queries:

"What time is check-in?"

"Do you have room service?"

"Is breakfast included?"

View Responses:

The chatbot will display its response in the chat window.

API Endpoints
The backend exposes the following API endpoint:

POST /get_answer:

Description: Accepts a user query and returns a response generated by the chatbot.

Request Body:

json
Copy
{
  "question": "What time is check-in?"
}
Response:

json
Copy
{
  "answer": "Check-in time is at 3:00 PM."
}
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes.

Push your branch and open a pull request.


Acknowledgments
Haystack: For providing the NLP framework.

FastAPI: For the backend API.

Bootstrap: For the responsive UI components.

SweetAlert2: For the beautiful alert messages.

Enjoy using the Hotel Receptionist Chatbot! If you have any questions or feedback, feel free to open an issue or contact the maintainers.

---
