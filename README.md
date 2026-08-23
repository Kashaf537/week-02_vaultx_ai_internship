# VAULTX AI Internship — Week 02

## Prompt Engineering & Structured LLM Applications

Week 02 focuses on building reliable and reusable LLM-powered tools using **Google Gemini API**, prompt engineering, structured JSON output, validation, classification, extraction, and evaluation.

---

## 🎯 Objectives

This week covers:

1. Core prompt engineering patterns
2. Structured JSON output with Pydantic
3. Customer-support classification
4. Information extraction
5. Prompt evaluation
6. Reusable AI modules

---

## 🛠️ Tech Stack

* **Python**
* **Google Gemini API**
* **google-genai**
* **Pydantic**
* **python-dotenv**
* **Tenacity**
* **Pytest**
* **ReportLab**
* **Git & GitHub**

---

## 📂 Project Structure

```text
week02/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── prompts/
│   ├── prompt_templates.py
│   └── prompt_library.md
│
├── src/
│   ├── config.py
│   ├── gemini_client.py
│   ├── schemas.py
│   ├── structured_output.py
│   ├── classifier.py
│   ├── extractor.py
│   └── evaluator.py
│
├── tests/
│
├── eval/
│
├── outputs/
│
└── reports/
```

---

# 1. Core Prompt Patterns

A reusable prompt library was created covering:

* **Zero-shot prompting**
* **Few-shot prompting**
* **Role/System prompting**
* **Reasoning / Chain-of-Thought prompting**
* **Constrained-output prompting**

Implemented in:

```text
prompts/prompt_templates.py
```

Documentation:

```text
prompts/prompt_library.md
```

---

# 2. Structured JSON Output

Gemini responses are converted into structured JSON and validated using **Pydantic**.

The workflow is:

```text
Input
  ↓
Prompt
  ↓
Gemini
  ↓
JSON
  ↓
Pydantic Validation
  ↓
Valid → Return
Invalid → Retry
```

Invalid responses are automatically retried with a limited number of attempts.

---

# 3. Classification Tool

A customer-support classifier returns:

```json
{
  "category": "billing",
  "priority": "high",
  "sentiment": "negative",
  "needs_human": true
}
```

Supported categories include:

```text
billing
technical
account
shipping
product
refund
other
```

The classifier is tested using **20 realistic support messages**.

---

# 4. Information Extraction

The extraction tool converts messy text such as invoices and emails into structured JSON.

Example fields:

```text
invoice_number
customer_name
email
total_amount
due_date
payment_status
```

Missing information is handled gracefully using `null` rather than causing the application to crash.

---

# 5. Prompt Evaluation

A small evaluation dataset containing **10–20 test cases** is used to measure prompt performance.

The evaluation process:

```text
Test Dataset
     ↓
Run Prompt
     ↓
Compare Expected vs Actual
     ↓
Calculate Accuracy
     ↓
Improve Prompt
     ↓
Evaluate Again
```

Before/after results are recorded in the evaluation reports.

---

# 6. Reusable Module

The final components are packaged as reusable Python functions with:

* Error handling
* Validation
* Limited retries
* Logging
* Modular design

Example:

```python
from src.classifier import classify_message

result = classify_message(
    "My payment was deducted twice."
)
```

---

# ⚙️ Setup

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate on Windows

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit `.env` to GitHub.

---

# ▶️ Run

Run the prompt library:

```bash
python prompts/prompt_templates.py
```

Run tests:

```bash
pytest
```

Run the classifier, extractor, and evaluator after completing their respective tasks.

---

# 📦 Deliverables

| # | Deliverable                          | Output        |
| - | ------------------------------------ | ------------- |
| 1 | Prompt Template Library              | `.py` + `.md` |
| 2 | JSON Schema + Validation + Retry     | `.py`         |
| 3 | Classifier + Evaluation              | `.py` + PDF   |
| 4 | Field Extraction Tool                | `.py`         |
| 5 | Evaluation Harness + Accuracy Report | `.py` + PDF   |
| 6 | Reusable Structured-Output Module    | `.py` + PDF   |

---

# 🔐 API & Rate Limits

The project uses the Google Gemini API. API keys are stored in `.env` and excluded from Git.

Gemini free-tier limits may cause `429` rate-limit errors. API calls and retries are therefore kept limited during testing and evaluation.

---

# ✅ Learning Outcomes

By completing Week 02, the project demonstrates practical skills in:

* Prompt engineering
* Gemini API integration
* Structured LLM outputs
* Pydantic validation
* Automatic retry
* LLM classification
* Information extraction
* Prompt evaluation
* Accuracy measurement
* Python modularization
* Error handling
