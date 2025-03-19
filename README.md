# LLM RAG Chatbot (OpenAI / Ollama + ChromaDB)

This project is a **local AI chatbot** that retrieves and generates answers based on a knowledge base.  
It supports **two AI model options**:
- ✅ **OpenAI GPT (API-based)**
- ✅ **Mistral 7B via Ollama (Free, runs locally)**

## 🚀 Features
- 🔹 **Flexible**: Choose **OpenAI GPT** (API) or **Ollama** (Local)
- 🔹 Uses **ChromaDB** for Retrieval-Augmented Generation (RAG)
- 🔹 No OpenAI API required when using **Ollama**
- 🔹 **Streamlit Web UI** for easy interaction
- 🔹 Works on **macOS (M1/M2), Linux**

---
## 🔄 Complete Chatbot Workflow (RAG + LLM)

```mermaid
graph TD;
    A[User Inputs Query] --> B[Convert Query to Embedding <br> (Using Sentence Transformers)];
    B --> C[Search Vector Database <br> (Retrieve Relevant Docs from ChromaDB)];
    
    C --> D[Prepare Context <br> (Combine Retrieved Docs + User Query)];
    D --> E{Choose AI Model};
    
    E -- OpenAI GPT --> F[Send Context to OpenAI API];
    E -- Ollama Mistral --> G[Process Locally with Ollama];

    F --> H[Generate AI Response <br> (LLM Analyzes and Generates Output)];
    G --> H;
    
    H --> I[Return Processed Response];
    I --> J[Display Response in Streamlit UI];

    style A fill:#FFDDC1,stroke:#000,stroke-width:1px;
    style B fill:#FFABAB,stroke:#000,stroke-width:1px;
    style C fill:#FFC3A0,stroke:#000,stroke-width:1px;
    style D fill:#FFB6C1,stroke:#000,stroke-width:1px;
    style E fill:#D3D3D3,stroke:#000,stroke-width:2px;
    style F fill:#D4A5A5,stroke:#000,stroke-width:1px;
    style G fill:#D4A5A5,stroke:#000,stroke-width:1px;
    style H fill:#85E3FF,stroke:#000,stroke-width:1px;
    style I fill:#85E3FF,stroke:#000,stroke-width:1px;
    style J fill:#85E3FF,stroke:#000,stroke-width:1px;


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
### **Run the chatbot (Streamlit Web UI)**

1. Activate your virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Launch Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

- ✅ **Choose your model** (OpenAI GPT or Ollama).
- ✅ **Interact easily** via the web interface.

---

## 🎯 Future Improvements
- ✅ Better retrieval accuracy with chunking
- ✅ Deploy as an API for easy integration

