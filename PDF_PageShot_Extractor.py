from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    # Save each image
    for page_num, image in enumerate(images):
        image.save(os.path.join(output_dir, f'output_page_{page_num+1}.jpg'), 'JPEG')


pdf_path = 'replace/path/to/pdf'
output_dir = 'replace/path/to/output.directory'
pdf_to_images(pdf_path, output_dir)
