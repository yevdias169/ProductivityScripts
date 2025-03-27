import fitz  # PyMuPDF
from pathlib import Path

def extract_text_from_pdf(pdf_path, output_txt_path):
    doc = fitz.open(pdf_path)
    extracted_text = []

    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            extracted_text.append(f"\n=== Slide {i + 1} ===\n{text}")

    Path(output_txt_path).write_text("\n".join(extracted_text), encoding='utf-8')
    print(f"✅ Extracted content saved to: {output_txt_path}")

# Run it on your file
extract_text_from_pdf(
    "/Users/yevin/Downloads/ElecWK5.pdf",
    "ElecWK5Stripped.txt"
)


