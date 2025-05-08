from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np

app = Flask(__name__)


qa_data = [
    {"question": "What is Python?", "answer": "Python is a popular programming language."},
    {"question": "What is AI?", "answer": "AI stands for Artificial Intelligence."},
    {"question": "Who created Python?", "answer": "Guido van Rossum created Python."},
    {"question": "What is machine learning?", "answer": "Machine learning is a subset of AI that allows systems to learn from data."},
    {"question": "What is deep learning?", "answer": "Deep learning is a type of machine learning that uses neural networks with many layers."},
    {"question": "What is Git?", "answer": "Git is a distributed version control system for tracking code changes."},
    {"question": "What is GitHub?", "answer": "GitHub is a cloud-based platform for hosting and collaborating on Git repositories."},
    {"question": "What is a neural network?", "answer": "A neural network is a model inspired by the human brain, used in deep learning."},
    {"question": "What is natural language processing?", "answer": "NLP is a field of AI focused on understanding and generating human language."},
    {"question": "What is the capital of France?", "answer": "The capital of France is Paris."}
]

df = pd.DataFrame(qa_data)
model = SentenceTransformer('all-MiniLM-L6-v2')
question_embeddings = model.encode(df["question"].tolist())


dimension = question_embeddings.shape[1]
faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(np.array(question_embeddings))

def get_answer(query, top_k=1):
    query_embedding = model.encode([query])
    distances, indices = faiss_index.search(query_embedding, top_k)
    result = []
    for idx in indices[0]:
        result.append({
            "question": df.iloc[idx]["question"],
            "answer": df.iloc[idx]["answer"]
        })
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        user_query = request.form["query"]
        results = get_answer(user_query)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
