import os
import fitz

DATA_FOLDER = "data"

total_pages = 0
total_files = 0

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(DATA_FOLDER, file)

        try:
            doc = fitz.open(pdf_path)

            pages = len(doc)

            total_pages += pages
            total_files += 1

            print(f"{file} -> {pages} pages")

        except Exception as e:

            print(f"Error reading {file}: {e}")

print("\n====================")
print(f"Total PDFs: {total_files}")
print(f"Total Pages: {total_pages}")
print("====================")