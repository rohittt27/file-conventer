import json
from PIL import Image
from io import BytesIO
from celery import shared_task
import os
import pandas as pd
# import PyPDF2
from PyPDF2 import PdfReader
from docx import Document
import io
import re
import base64
import tempfile
import pandas as pd
from pdf2docx import Converter

# from celery.result import AsyncResult


@shared_task
def convert_file(pdf_path, doc_path):
    pdf_path = io.BytesIO(base64.b64decode(pdf_path))
    with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
        temp_pdf.write(pdf_path.getbuffer())
        temp_pdf_path = temp_pdf.name

    cv = Converter(temp_pdf_path)
    cv.convert(doc_path)
    cv.close()

    os.remove(temp_pdf_path)


@shared_task
def convert_excel_to_csv(file_path, output_path):
    # with open(file_path, 'rb') as file:
    #     df = pd.read_excel(file)
    #     df.to_csv(output_path, index=False)
    df = pd.read_excel(file_path)
    df.to_csv(output_path, index=False)