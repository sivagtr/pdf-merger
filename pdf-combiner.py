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
        
        for i in range(pdf1_pages):
            pdf_writer.add_page(pdf1_reader.pages[i])
        
        for i in range(pdf2_pages):
            pdf_writer.add_page(pdf2_reader.pages[i])

       
        # Write the final combined PDF to output
        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)

# Example usage:
pdf1_path = "/Users/siva/Downloads/Java8/Java8-B1.pdf"  # Path to the first PDF
pdf2_path = "/Users/siva/Downloads/Java8/Java8-E.pdf"  # Path to the second PDF
output_pdf_path = "/Users/siva/Downloads/Java8/Java8-BC.pdf"  # Path where the combined PDF will be saved

combine_pdfs(pdf1_path, pdf2_path, output_pdf_path)
print(f"Combined PDF saved as {output_pdf_path}")

