import json
import pdfplumber
from huggingface_hub import InferenceClient
from config import HF_API_KEY

hf_client = InferenceClient(api_key=HF_API_KEY)

def read_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_financials_hf(pdf_text):
    prompt = (
        "Extract the financial metrics from this report text and return ONLY a valid JSON object "
        "with these exact keys: company_ticker, quarter, revenue_millions, net_income_millions, "
        f"ebitda_millions, eps.\n\nReport Text:\n{pdf_text}"
    )
    
    response = hf_client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=500
    )
    
    response_text = response.choices[0].message.content.strip()
    if response_text.startswith("```json"):
        response_text = response_text[7:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]
        
    return json.loads(response_text.strip())