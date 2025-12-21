import pdfplumber
import io

def extract_text_from_pdf(upload_file) -> str:
    text = ""

    with pdfplumber.open(io.BytesIO(upload_file.file.read())) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return text