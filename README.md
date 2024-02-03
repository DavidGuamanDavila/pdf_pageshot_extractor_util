# PDF PageShot Extractor
## Overview
PDF PageShot Extractor is a Python tool designed to efficiently convert each page of a PDF document into individual image files. This utility was inspired by a friend who needed to take numerous screenshots for her class. The challenge was that the PDF contained scanned images, making it difficult to extract information directly. This tool simplifies the process, enabling easier access to the content, particularly when used in conjunction with OCR (Optical Character Recognition) technologies for text extraction.

## Requirements
- Python 3.x
- pdf2image
- Poppler

## Installation
### Python Dependencies
1. Ensure that Python 3 is installed on your system. Then, install the required Python package using pip:

2. Install pdf2image
```bash
pip3 install pdf2image
```
3. Install Poppler
```bash
brew install poppler
```
## Usage
To use the script, specify the path to the PDF file and the desired output directory:
```bash
pdf_path = 'replace/path/to/pdf'
output_dir = 'replace/path/to/output.directory'
pdf_to_images(pdf_path, output_dir)
```

## How It Works
The script employs pdf2image to convert each page of the provided PDF into an image. These images are then saved in the specified directory, with each page being saved as a separate image file.

## Acknowledgements
This project was particularly inspired by a friend who faced the challenge of extracting information from scanned documents for her class. It highlights the practical application of scripting in solving real-world problems.


