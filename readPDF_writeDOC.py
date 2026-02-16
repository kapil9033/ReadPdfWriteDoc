import os
import PyPDF2
from docx import Document

def pdf_to_docx(pdf_path, docx_path):
    # Create Word document
    document = Document()

    # Open PDF
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        # Loop through pages
        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()

            if text:
                print(f"Processing Page {page_number}")
                
                # Split lines properly
                for line in text.split("\n"):
                    document.add_paragraph(line)
            else:
                print(f"No text found on Page {page_number}")

    # Show exact save location
    print("Saving file to:", os.path.abspath(docx_path))

    # Save document
    document.save(docx_path)
    print("Conversion complete! Saved as", docx_path)


if __name__ == "__main__":
    # IMPORTANT: Use FULL paths
    input_pdf = r"C:\TEMP\ReadPdfWriteDoc\Input.pdf"
    output_docx = r"C:\TEMP\ReadPdfWriteDoc\output.docx"

    pdf_to_docx(input_pdf, output_docx)
