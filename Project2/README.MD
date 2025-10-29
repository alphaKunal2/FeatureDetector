# 🧠 LLM-RAG Image Filter Project

This project integrates a **Large Language Model (LLM)** with **Retrieval-Augmented Generation (RAG)** to apply different **image filters** based on natural language input.  
Users can describe what they want (e.g., “make the image grayscale” or “apply a blur effect”), and the system automatically selects and executes the right image processing function.

---

## 🚀 Features
- Accepts natural language commands to choose filters.
- Uses RAG to retrieve filter descriptions or usage examples.
- Supports common filters like:
  - Grayscale
  - Blur
  - Sharpen
  - Edge Detection
  - Brightness / Contrast Adjustment
- Modular and easily extendable for new filters.

---

## ⚙️ How It Works
1. User enters a text command (e.g., *"apply a blur filter"*).  
2. The LLM interprets the command and queries the RAG retriever for relevant information.  
3. The orchestrator maps the command to the correct image filter function.  
4. The selected filter is applied to the image, and the processed result is returned.

---

## 🧩 Tech Stack
- **Language Model:** OpenAI / Hugging Face  
- **Retrieval:** FAISS / ChromaDB  
- **Image Processing:** OpenCV / Pillow  
- **Backend Framework:** Python (Flask / FastAPI)

---

## 🛠️ Setup
```bash
git clone https://github.com/yourusername/llm-rag-image-filter.git
cd llm-rag-image-filter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
