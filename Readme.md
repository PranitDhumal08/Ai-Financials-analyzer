# AI-Powered Financial Document Analyzer & SQL Pipeline

An enterprise-grade, modular Python application designed to ingest corporate earnings report PDFs, extract structured financial metrics using Large Language Models (LLMs) via Hugging Face, preview them through an interactive **Streamlit Web UI**, and commit the structured data directly into a local PostgreSQL database using Pandas and SQLAlchemy.

---

## Application Demo

Here is a preview of the Streamlit frontend interface processing an earnings report and rendering the extracted structured data:

```
![Streamlit Frontend Demo](demo.png)
```

---

## Key Features

* **Interactive Web Interface:** Built with Streamlit for a seamless drag-and-drop file upload and instant processing experience.
* **LLM-Powered Extraction:** Leverages advanced instruction-tuned models (`meta-llama/Llama-3.3-70B-Instruct`) via Hugging Face to parse unstructured financial text into strict JSON payloads.
* **Modular Architecture:** Cleanly separated concerns across configuration (`config.py`), LLM/PDF extraction (`extractor.py`), database ORM operations (`database.py`), and the UI (`app.py`).
* **Environment Security:** Uses `.env` management to keep API keys and database credentials secure.
* **Database Integration:** Automatically transforms JSON output into a Pandas DataFrame and commits records securely to PostgreSQL.

---

## Project Structure

```text
ai-analyzer/
│
├── .env                 # Environment credentials (API keys & DB URIs)
├── .gitignore           # Excludes virtual environments and cache
├── requirements.txt     # Python project dependencies
├── config.py            # Environment variable loader and validator
├── extractor.py         # PDF text parsing & Hugging Face LLM integration
├── database.py          # SQLAlchemy connection engine & DB commit logic
├── app.py               # Streamlit interactive frontend application
├── demo.png             # UI screenshot for documentation
└── README.md            # Project documentation
```

---

## Setup and Installation

### 1. Clone the Repository & Navigate to Directory
```bash
git clone <repository-url>
cd ai-analyzer
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add your credentials:
```env
HUGGINGFACE_API_KEY=your_actual_huggingface_api_token
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/financial_analyzer
```

### 4. Setup PostgreSQL Database
Ensure your local PostgreSQL server is running and create your target database:
```sql
CREATE DATABASE financial_analyzer;
```

---

## Usage

### Launch the Streamlit Frontend Web App
To start the interactive graphical user interface, run:
```bash
streamlit run app.py
```

### Example Terminal Execution Flow
Behind the scenes, when you upload a PDF via the UI, the pipeline executes the following workflow:

```text
Reading text from PDF: temp_report.pdf...
Sending text to Hugging Face model for extraction...
Successfully extracted data via Hugging Face: {'company_ticker': 'TCS', 'quarter': 'Q3', 'revenue_millions': 67087, 'net_income_millions': 13438, 'ebitda_millions': 18269, 'eps': 37.14}
SUCCESS: Financial data committed to PostgreSQL database.
```

---

## Database Schema (`earnings_data`)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `company_ticker` | VARCHAR | Stock ticker symbol (e.g., TCS) |
| `quarter` | VARCHAR | Financial reporting period (e.g., Q3) |
| `revenue_millions` | NUMERIC | Total reported revenue for the period |
| `net_income_millions`| NUMERIC | Net profit / income after taxes |
| `ebitda_millions` | NUMERIC | Earnings before interest, tax, & depreciation |
| `eps` | NUMERIC | Earnings Per Share |

---

## License

This project is open-source and available under the MIT License for financial data analysis and automation use.