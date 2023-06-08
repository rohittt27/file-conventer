from django.urls import path
from .views import PdfToDocConverter,ExcelToCSV,GetFileView

urlpatterns = [
    path('convert-file/', PdfToDocConverter.as_view(), name='file_conversion'),
    path('file/', ExcelToCSV.as_view(), name='file_conversion'),
    path('media/<str:file_name>', GetFileView.as_view(), name='get-file')
]