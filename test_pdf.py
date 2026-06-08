from pypdf import PdfReader

reader = PdfReader("data/simple.pdf")

for i, page in enumerate(reader.pages):
    text = page.extract_text()

    print(f"\nPage {i+1}")
    print("Length:", len(text) if text else 0)