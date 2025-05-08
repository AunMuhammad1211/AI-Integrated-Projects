import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
from datasets import load_metric

# Load the model and tokenizer
model_name = 't5-small'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Summarization function
def summarize(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

text = """ We are hiring an LLM Developer to develop and fine-tune Large 
Language Models for various enterprise applications such as chatbots, content generation, 
summarization, and intelligent search. This role requires deep knowledge of transformer-based 
architectures and modern NLP pipelines."""

summary = summarize(text)
print(summary)


iface = gr.Interface(fn=summarize, inputs="text", outputs="text", title="Text Summarization with T5", description="Enter text to get a summarized version using the T5 model.")
iface.launch()