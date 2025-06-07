import pdfplumber

def extract_clauses_from_pdf(file_buffer):
    clauses = []
    with pdfplumber.open(file_buffer) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                clauses.extend(text.split('\n\n'))  # Adjust split if needed
    return clauses

