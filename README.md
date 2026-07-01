# AI-code-reviewer mini project
# 🤖 AI Code Reviewer

A simple web application built using **Python** and **Streamlit** that analyzes Python code for style issues, formats the code, and measures code complexity.

## Features

- Paste Python code
- Upload Python (`.py`) files
- Analyze code using **Flake8**
- Format code using **Black**
- Measure code complexity using **Radon**
- View analysis results
- Download the analysis report

## Technologies Used

- Python
- Streamlit
- Flake8
- Black
- Radon

## Project Structure

```
AICodeReviewer/
│
├── app.py
├── sample_code.py
├── requirements.txt
├── reports/
└── temp/
```

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python -m streamlit run app.py
```

## How It Works

1. Enter Python code or upload a `.py` file.
2. Click **Analyze Code**.
3. The application:
   - Checks coding style using Flake8
   - Formats the code using Black
   - Measures complexity using Radon
4. View the results and download the report.

## Author

**Hasini Sainath**
