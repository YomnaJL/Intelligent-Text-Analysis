# 🧠 Intelligent Text Analysis with Ollama

<p align="center">
  <img src="assets/ollama-text-analysis-banner.png" alt="Banner" width="85%">
</p>

This project provides...

This project provides a unified Python function to process natural language input using [Ollama](https://ollama.com/) and the `llama3.2` model.

It supports multiple tasks such as summarization, keyword extraction, sentiment analysis, text simplification, and more — all in **English**, **French**, or **Arabic**.

---

## ✅ Features

- 🌍 Multilingual support (`en`, `fr`, `ar`)
- 🧩 Multi-task processing using a single interface
- 🤖 Powered by `llama3.2` via Ollama
- 🔁 Easy to integrate into Flask, Streamlit, or CLI apps

---

## ⚙️ Function Overview

### `process_text(text: str, lang_choice: str, task: str) -> str`

Processes text using a selected NLP task and target language.

| Parameter     | Type   | Description                                                  |
|---------------|--------|--------------------------------------------------------------|
| `text`        | `str`  | The input text to process.                                   |
| `lang_choice` | `str`  | Target language: `"en"`, `"fr"`, or `"ar"`.                  |
| `task`        | `str`  | Task name: see [Supported Tasks](#-supported-tasks).         |

### Returns:
A `str` containing the processed output (summary, keywords, sentiment, etc.).

---

## 🧪 Supported Tasks

| Task Name             | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| `summary`             | Generate a summary of the input text                         |
| `keywords`            | Extract key themes or keywords                               |
| `category`            | Classify text into a topic                                   |
| `simplify`            | Rewrite text in simpler language                             |
| `facts`               | Extract factual info (names, numbers, dates)                 |
| `title`               | Generate a short, informative title                          |
| `rewrite`             | Rewrite in journalistic tone                                 |
| `tone`                | Analyze tone and potential bias                              |
| `sentiment`           | Determine sentiment (positive/negative/neutral)              |
| `question_generation` | Generate quiz questions and answers                          |
| `text_to_speech`      | Convert text to phonetic transcription                       |
| `grammar_correction`  | Fix grammar and spelling issues                              |
| `text_completion`     | Complete a partial sentence or paragraph                     |
| `code_generation`     | Generate code from a plain-language description              |

---

## 🚀 Example Usage

```python
from your_module import process_text

text = "Generative AI is transforming industries..."
lang = "fr"
task = "summary"

result = process_text(text, lang, task)
print(result)
