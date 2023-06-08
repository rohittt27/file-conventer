import base64
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import convert_excel_to_csv, convert_file
import os
import pandas as pd
import io
import docx2txt

class PdfToDocConverter(APIView):
    def post(self, request):
        if request.method == 'POST' and 'file' in request.FILES:
            pdf_file = request.FILES['file']
            doc_path = 'file_converter/media/media.docx'
            pdf_data = io.BytesIO(pdf_file.read())
            pdf_data_base64 = base64.b64encode(pdf_data.getvalue()).decode('utf-8')
            
            convert_file.delay(pdf_data_base64, doc_path)

            return JsonResponse({'message': f'file_converter/media/media.docx'})
        else:
            return JsonResponse({'message': 'Invalid request.'}, status=400)



class ExcelToCSV(APIView):
    def post(self, request):
        excel_file = request.FILES['file']
        file_name = excel_file.name
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        output_path = os.path.join(settings.MEDIA_ROOT, 'media.csv')

        with open(file_path, 'wb+') as destination:
            for chunk in excel_file.chunks():
                destination.write(chunk)

        task = convert_excel_to_csv.delay(file_path, output_path)

        return Response({'status': f'file_converter/media/media.csv'})


class GetFileView(APIView):
    def get(self, request,file_name):
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        
        if os.path.exists(file_path):
            if file_name.endswith('.csv'):
                with open(file_path, 'r') as file:
                    csv_data = file.read()
                response = HttpResponse(csv_data, content_type='text/csv')
                return response
            
            else:
                text_content = docx2txt.process(file_path)
                response = HttpResponse(text_content, content_type='text/plain')
                return response
        
        else:
            return HttpResponse("File not found", status=404)