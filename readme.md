
# C.A.R.E-LLM-Base

A Streamlit application providing an AI assistant specialized in gestational diabetes management.

## Quick Start Guide

Download and install ollama through the cli through the following command:
'curl -fsSL https://ollama.com/install.sh | sh'

### Install Streamlit and Ollama Packages

Continuing with the following in a virtual environment

```bash
pip3 install streamlit ollama
```

### Install Ollama

Follow the Ollama installation guide:

- Visit [Ollama Installation](https://ollama.ai/docs/installation) for instructions compatible with your system.

### Clone the Repository

```bash
git clone https://github.com/toufiqmusah/C.A.R.E-LLM-Base.git
cd C.A.R.E-LLM-Base
```

### Pull the Ollama Model

Download the required model:

```bash
ollama pull qwen2:0.5b-instruct
```

### Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```
