# from pdf2image import convert_from_path
# from pytesseract import image_to_string
# from PIL import Image
#
#
# def convert_pdf_to_image(pdf_file):
#     return convert_from_path(pdf_file)
#
#
# def convert_image_to_text(file):
#     text = image_to_string(file)
#     return text
#
#
# def get_text_from_any_pdf(pdf_file):
#     images = convert_pdf_to_image(pdf_file)
#     final_text = ""
#     for pg, img in enumerate(images):
#         final_text += convert_image_to_text(img)
#     return final_text
#
#
path_to_pdf = 'sample.pdf'
#
#
# print(get_text_from_any_pdf(path_to_pdf))


import PyPDF2

a = PyPDF2.PdfFileReader(f'{path_to_pdf}')
# print(a.documentInfo)
# print(a.numPages)
for i in range(0, a.numPages):
    text = a.getPage(i).extractText()
    print(text)
