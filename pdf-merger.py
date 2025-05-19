import PyPDF2

# Function to combine pages from two PDFs
def combine_pdfs(pdf1_path, pdf2_path, output_pdf_path):
    # Open the two PDF files
    with open(pdf1_path, "rb") as pdf1_file, open(pdf2_path, "rb") as pdf2_file:
        pdf1_reader = PyPDF2.PdfReader(pdf1_file)
        pdf2_reader = PyPDF2.PdfReader(pdf2_file)
        
        # Create a PDF writer object to write the output file
        pdf_writer = PyPDF2.PdfWriter()

        # Find the total number of pages in both PDFs
        pdf1_pages = len(pdf1_reader.pages)
        pdf2_pages = len(pdf2_reader.pages)
        
        if pdf1_pages != pdf2_pages :
            print("PDF1 Length != PDF2 Length")
            exit()

        # We will alternate between the first page from pdf1 and the last page from pdf2
        # until all pages are added to the new PDF
        for i in range(max(pdf1_pages, pdf2_pages)):
            # Add the first available page from pdf1 (if exists)
            if i < pdf1_pages:
                pdf_writer.add_page(pdf1_reader.pages[i])

            # Add the last available page from pdf2 (if exists)
            if i < pdf2_pages:
                pdf_writer.add_page(pdf2_reader.pages[pdf2_pages - 1 - i])

        # Write the final combined PDF to output
        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)

# Example usage:
pdf1_path = "/Users/siva/Downloads/Solid-A.pdf"  # Path to the first PDF
pdf2_path = "/Users/siva/Downloads/Solid-B.pdf"  # Path to the second PDF
output_pdf_path = "/Users/siva/Downloads/Solid.pdf"  # Path where the combined PDF will be saved

combine_pdfs(pdf1_path, pdf2_path, output_pdf_path)
print(f"Combined PDF saved as {output_pdf_path}")

