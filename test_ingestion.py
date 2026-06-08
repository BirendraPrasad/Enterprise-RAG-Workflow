from app.ingestion import extract_pdf_text

text = extract_pdf_text("data/simpl.pdf")

print("Length:", len(text))

print(text[:1000])