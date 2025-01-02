import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    with open(output_path, 'wb') as output_pdf:
        merger.write(output_pdf)
    merger.close()
    print(f"Compiled PDF: {output_path}")

# Loop through the folders and call the function
folder_path = '/home/herman/Downloads/Compressed/PAC-2025/PAC'
compiled_folder_path = os.path.join(folder_path, 'PAC-2025/CompiledPDF')

# Create the CompiledPDF directory if it doesn't exist
if not os.path.exists(compiled_folder_path):
    os.makedirs(compiled_folder_path)

for root, dirs, files in os.walk(folder_path):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        print(f"Processing directory: {dir_path}")
        try:
            dir_files = os.listdir(dir_path)
            print(f"Files in directory: {dir_files}")
            pdf_files = [os.path.join(dir_path, f) for f in dir_files if f.lower().endswith('.pdf')]
            print(f"Found PDF files: {pdf_files}")
            if pdf_files:
                # Replace spaces with underscores and remove special characters for the output file name
                output_file_name = dir_name.replace(' ', '_').replace('/', '_') + '.pdf'
                output_path = os.path.join(compiled_folder_path, output_file_name)
                merge_pdfs(pdf_files, output_path)
        except Exception as e:
            print(f"Error processing directory {dir_path}: {e}")