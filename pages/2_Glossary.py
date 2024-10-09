# pages/Glossary.py
import streamlit as st

st.title("Glossary")

glossary = {
    "AI": "Artificial Intelligence (AI) refers to the capability of machines to perform tasks that typically require human intelligence, such as understanding language, recognizing patterns, and making decisions.",
    "API": "An Application Programming Interface (API) is a set of rules that allows different software applications to communicate with each other.",
    "ChatGPT": "ChatGPT is a conversational AI model created by OpenAI that can generate human-like text responses in a dialogue format.",
    "Claude": "Claude is an AI model developed by Anthropic, designed to provide safe and reliable conversational AI capabilities.",
    "Edge AI": "Edge AI refers to the deployment of AI algorithms on local devices rather than in a centralized cloud, allowing for faster data processing and real-time decision-making.",
    "Elo Rating": "The Elo rating system is a method for calculating the relative skill levels of players in two-player games such as chess.",
    "GitHub Copilot": "GitHub Copilot is an AI-powered tool that assists software developers by suggesting code snippets and functions as they write.",
    "GPT-4": "GPT-4 is the fourth generation of the Generative Pre-trained Transformer model developed by OpenAI.",
    "IoT": "The Internet of Things (IoT) refers to a network of physical devices connected to the internet, allowing them to collect and share data.",
    "LLMs": "Large Language Models (LLMs) are advanced AI models trained on extensive text data to understand and generate human-like text.",
    "LLaMA 3": "LLaMA 3 is the third generation of the LLaMA series developed by Meta, designed for efficiency and high performance in language tasks.",
    "Microcontroller": "A microcontroller is a compact integrated circuit designed to govern a specific operation in an embedded system.",
    "NLP": "Natural Language Processing (NLP) is a branch of AI focused on enabling computers to understand, interpret, and respond to human language.",
    "NPU": "A Neural Processing Unit (NPU) is specialized hardware designed to accelerate the processing of machine learning tasks.",
    "OCR": "Optical Character Recognition (OCR) is a technology that converts different types of documents into editable and searchable digital text.",
    "Parameters": "In machine learning models, parameters refer to the weights and biases that the model learns during training.",
    "Proprietary Models": "Proprietary models are AI models owned by a specific company or organization, often requiring licensing fees for use.",
    "RAG": "Retrieval-Augmented Generation (RAG) is a model architecture that combines retrieving information from a database with generating new content.",
    "Rasa": "Rasa is an open-source framework for building conversational AI and chatbots.",
    "SuperGLUE Benchmark": "The SuperGLUE benchmark is a set of challenging tasks used to evaluate the performance of natural language understanding models.",
    "SLMs": "Small Language Models (SLMs) are compact AI models designed for specific tasks, often requiring fewer resources than LLMs.",
    "TensorFlow Lite": "TensorFlow Lite is a lightweight version of TensorFlow designed for mobile and embedded devices.",
    "Token": "A token is a basic unit of text processing in AI language models, representing a word, part of a word, or a single character.",
    "TOPS": "Tera Operations Per Second (TOPS) is a measure of a computer's performance, particularly in AI and machine learning.",
    "VM": "A Virtual Machine (VM) is a software emulation of a physical computer that allows multiple operating systems to run on a single physical machine."
}

search_term = st.text_input("Search Glossary Terms:")

if search_term:
    filtered_glossary = {term: definition for term, definition in glossary.items() if search_term.lower() in term.lower()}
else:
    filtered_glossary = glossary

for term, definition in filtered_glossary.items():
    st.subheader(term)
    st.write(definition)
