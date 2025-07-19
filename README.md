# chatbot
# 🧠 Chatbot with LangChain and Streamlit

This is a simple AI-powered chatbot application built using **LangChain**, **Streamlit**, and custom tools. It leverages large language models (LLMs) for answering questions based on documents.

## 📁 Project Structure

```
chatbot/
├── .env                 # Environment variables (API keys, etc.)
├── main.py              # Main application script
├── tools.py             # Tool definitions for the chatbot
├── chatbot.ipynb        # Notebook for prototyping or testing
└── __pycache__/         # Cached Python bytecode (can be ignored)
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

### 2. Set Up Environment

Install dependencies (preferably in a virtual environment):

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, you can install manually:
```bash
pip install streamlit langchain python-dotenv
```

### 3. Configure `.env`

Create a `.env` file in the root folder with the required keys:

```
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the App

```bash
streamlit run main.py
```

## 📒 Features

- Document-based Q&A
- Modular tools system using LangChain
- Streamlit UI for easy interaction

## 🛠️ Tech Stack

- Python
- LangChain
- Streamlit
- dotenv

## 🧪 Notebook

You can use `chatbot.ipynb` to experiment and test the chatbot’s functionality in an interactive environment.

## 📄 License

This project is licensed under the MIT License.
