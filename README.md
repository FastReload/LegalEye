
# 🧠 LegalEye: Clause-Level Legal Document Analyzer

**LegalEye** is a layout-aware, explainable system for clause classification and interpretation in legal contracts. It integrates Legal-BERT for classification, FAISS for semantic retrieval, and Google's Gemini API for generating natural language explanations. The tool is built with Streamlit for ease of use and real-time interactivity.

---

## 🚀 Features

- ✅ Extracts individual clauses from uploaded PDF contracts
- ✅ Classifies clauses using fine-tuned Legal-BERT (`nlpaueb/legal-bert-base-uncased`)
- ✅ Retrieves top-5 similar clauses from LEDGAR dataset using FAISS
- ✅ Generates human-readable explanations using Gemini API
- ✅ Interactive and accessible frontend using Streamlit

---

## 📂 Dataset: LEDGAR

We use the publicly available [LEDGAR dataset](https://archive.org/details/LEDGAR), introduced by Tuggener et al. (LREC 2020), for clause-level classification.

To download:

```bash
wget https://archive.org/download/LEDGAR/ledgar.zip
unzip ledgar.zip
```

After downloading, use the provided `prepare_ledgar_index.py` to generate FAISS index and embeddings for retrieval.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/LegalEye.git
cd LegalEye
```

### 2. Install Dependencies

Make sure Python 3.9+ is installed.

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API

Add your API key in a `.env` file or directly in `config.py`:

```bash
export GEMINI_API_KEY="your_key_here"
```

Or set it in Streamlit manually at runtime.

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

---

## 📊 Model Performance

| Model                | Accuracy | Macro-F1 | Weighted-F1 |
|----------------------|----------|----------|-------------|
| Legal-BERT (5-class) | 96.2%    | 93.0%    | 95.8%       |
| BERT base            | 92.1%    | 87.2%    | 91.0%       |
| TF-IDF + SVM         | 65.2%    | 35.8%    | 63.5%       |

---

## 📎 Example

**Input Clause:**

> _"This agreement shall be governed by and construed in accordance with the laws of the State of Delaware."_

**Predicted Label:** Governing Law  
**Top Match:** "This agreement is governed by the laws of California."  
**Generated Explanation:**  
> _"This clause defines the jurisdiction under which the agreement will be interpreted and enforced, which affects how disputes are resolved."_

---

## 📜 Citation

If you use LegalEye in academic work, please cite:

```
@inproceedings{your_paper,
  title={LegalEye: A Layout-Aware Clause Classification, Retrieval, and Explanation System for Legal Documents},
  author={Your Name},
  year={2025},
  booktitle={NeurIPS}
}
```

---

## ⚖️ License

This project is licensed under the MIT License.

---

## 📦 `requirements.txt`

```txt
streamlit>=1.30.0
pdfplumber>=0.10.2
transformers>=4.39.3
sentence-transformers>=2.2.2
faiss-cpu>=1.7.4
scikit-learn>=1.4.2
numpy>=1.26.4
torch>=2.2.2
protobuf<=3.20.3
google-generativeai>=0.3.2
```
