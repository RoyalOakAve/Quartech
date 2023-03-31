import os
import pytesseract
from pdfminer.high_level import extract_text

# Path to the folder containing PDF files to be converted
pdf_folder = r'C:\Users\graysonl\Documents\code\pythonStuff\inputDocs\pdf'

# Path to the folder where the text files will be saved
txt_folder = r'C:\Users\graysonl\Documents\code\pythonStuff\inputDocs\text'

# Loop through each PDF file in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        # Extract the text from the PDF file
        page_text = extract_text(os.path.join(pdf_folder, filename))

        # Create a text file with the same name as the PDF file
        # and save it in the output folder
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        with open(os.path.join(txt_folder, txt_filename), 'w', encoding='utf-8') as txt_file:
            txt_file.write(page_text)
