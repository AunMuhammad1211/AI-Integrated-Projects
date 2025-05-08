# 🤖 QnA Bot with FAISS and Sentence Transformers
This is a simple Question Answering Bot that uses semantic search powered by Sentence Transformers and FAISS. A lightweight Flask web app with a clean HTML/CSS UI allows users to interact with the bot.

## 🚀 Features
Semantic search using sentence embeddings (not keyword matching)

Fast vector-based similarity search using FAISS

Simple HTML/CSS frontend for user-friendly interaction

Easily extendable QnA dataset

## 🧠 Technologies Used
Technology	Purpose
Flask	Web framework for backend
Sentence Transformers	To generate question embeddings
FAISS	Fast Approximate Nearest Neighbor Search
HTML, CSS	Frontend UI
Pandas & NumPy	Data handling

## 📁 Project Structure
```bash
qna-bot/
│
├── app.py                  
├── templates/
│   └── index.html          
├── static/
│   └── style.css          
└── README.md     
```          
## 🛠️ Setup Instructions

Clone the repo
```bash
cd https://github.com/AunMuhammad1211/AI-Integrated-Projects
git clone https://github.com/AunMuhammad1211/QNA-Bot.git
```
## Install required packages
```bash
pip install flask sentence-transformers faiss-cpu pandas
```
## Run the app
```bash
python app.py
```
## ✍️ Example Questions
Try asking:

Who created Python?

Tell me about AI.

What is deep learning?