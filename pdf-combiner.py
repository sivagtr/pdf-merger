import PyPDF2

# Function to combine multiple PDFs
def combine_pdfs(pdf_paths, output_pdf_path):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf_path in pdf_paths:
        try:
            with open(pdf_path, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                num_pages = len(pdf_reader.pages)
                for i in range(num_pages):
                    pdf_writer.add_page(pdf_reader.pages[i])
                print(f"Added {num_pages} pages from {pdf_path}")
        except Exception as e:
            print(f"Failed to read {pdf_path}: {e}")

    # Write the final combined PDF
    try:
        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)
        print(f"\nCombined PDF saved as {output_pdf_path}")
    except Exception as e:
        print(f"Failed to write output PDF: {e}")

# Example usage
pdf_files = [
    "/Users/siva/Downloads/Algorithms-B6.pdf",
    "/Users/siva/Downloads/Algorithms-B7.pdf",
    "/Users/siva/Downloads/Algorithms-B8.pdf", 
    "/Users/siva/Downloads/Algorithms-B9.pdf",  
    "/Users/siva/Downloads/Algorithms-B10.pdf"
]

output_path = "/Users/siva/Downloads/Algorithms-B.pdf"

combine_pdfs(pdf_files, output_path)
