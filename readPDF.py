import PyPDF2

def read_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            number_of_pages = len(reader.pages)

            print(f"Total Pages: {number_of_pages}\n")

            for page_num in range(number_of_pages):
                page = reader.pages[page_num]
                text = page.extract_text()

                print(f"--- Page {page_num + 1} ---")
                print(text)
                print("\n")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error reading PDF: {e}")


if __name__ == "__main__":
    pdf_path = r"C:\TEMP\ReadPdfWriteDoc\Input.pdf"  # Replace with your PDF file path
    read_pdf(pdf_path)
