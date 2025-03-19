# LLM RAG Chatbot (OpenAI / Ollama + ChromaDB)

This project is a **local AI chatbot** that retrieves and generates answers based on a knowledge base.  
It supports **two AI model options**:
- ✅ **OpenAI GPT (API-based)**
- ✅ **Mistral 7B via Ollama (Free, runs locally)**

## 🚀 Features
- 🔹 **Flexible**: Choose **OpenAI GPT** (API) or **Ollama** (Local)
- 🔹 Uses **ChromaDB** for Retrieval-Augmented Generation (RAG)
- 🔹 No OpenAI API required when using **Ollama**
- 🔹 Works on **macOS (M1/M2), Linux**

---

## 🛠 Installation
### **1️⃣ Clone the repo**
```bash
git clone https://github.com/Laihu08/llm-rag-chatbot.git
cd llm-rag-chatbot
```

### **2️⃣ Set up Python environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **3️⃣ Install a Model (Choose One)**
#### **Option 1: OpenAI GPT (API-based)**
1. Get an API key from [OpenAI](https://platform.openai.com/)
2. Set your API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```
3. Install OpenAI SDK:
   ```bash
   pip install openai
   ```

#### **Option 2: Ollama (Local & Free)**
1. Install **Ollama**:
   ```bash
   brew install ollama
   ```
2. Download the **Mistral 7B model**:
   ```bash
   ollama pull mistral
   ```
3. Start Ollama in the background:
   ```bash
   ollama serve
   ```

---

## 💬 Usage
### **Run the chatbot (Choose One)**

#### **Option 1: OpenAI GPT**
```bash
python generate_answer_openai.py
```

#### **Option 2: Ollama (Mistral 7B)**
```bash
python generate_answer_local.py
```

---

## 🎯 Future Improvements
- ✅ Streamlit Web UI
- ✅ Better retrieval accuracy with chunking
- ✅ Deploy as an API for easy integration

