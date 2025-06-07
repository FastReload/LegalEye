#  LegalEye: Clause-Level Legal Document Analyzer

**LegalEye** is a layout-aware, explainable system for clause classification and interpretation in legal contracts. It integrates Legal-BERT for classification, FAISS for semantic retrieval, and Google's Gemini API for generating natural language explanations. The tool is built with Streamlit for ease of use and real-time interactivity.

---

##  Features

- ✅ Extracts individual clauses from uploaded PDF contracts
- ✅ Classifies clauses using fine-tuned Legal-BERT (`nlpaueb/legal-bert-base-uncased`)
- ✅ Retrieves top-5 similar clauses from LEDGAR dataset using FAISS
- ✅ Generates human-readable explanations using Gemini API
- ✅ Interactive and accessible frontend using Streamlit

---

##  Dataset: LEDGAR

We use the publicly available LEDGAR dataset, introduced by Tuggener et al. ([LREC 2020 Paper](https://aclanthology.org/2020.lrec-1.155.pdf)), for clause-level classification.


You can also find a zip version of the dataset already uploaded in the repository for convenience.

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/FastReload/LegalEye.git
cd LegalEye
```

### 2. Install Dependencies

Make sure Python 3.9+ is installed.

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API

Add your API key directly in `explanation_generator.py`:

```bash
export GEMINI_API_KEY="your_key_here"
```

---

##  Running the Application

```bash
streamlit run app.py
```

---

##  Model Performance

| Model                  | Accuracy | Macro-F1 | Weighted-F1 |
|------------------------|----------|----------|-------------|
| Legal-BERT (5-class)   | 96.2%    | 93.0%    | 95.8%       |
| BERT base (5-class)    | 92.1%    | 87.2%    | 91.0%       |
| TF-IDF + SVM (68-class)| 65.2%    | 35.8%    | 63.5%       |
| Legal-BERT (68-class)  | 79.5%    | 58.3%    | 78.6%       |

---

##  Example

**Input Clause:**

> _"This agreement shall be governed by and construed in accordance with the laws of the State of Delaware."_

**Predicted Label:** Governing Law  
**Top Match:** "This agreement is governed by the laws of California."  
**Generated Explanation:**  
> _"This clause defines the jurisdiction under which the agreement will be interpreted and enforced, which affects how disputes are resolved."_

---

##  License

This project is licensed under the MIT License.
