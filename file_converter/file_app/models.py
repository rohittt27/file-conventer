from django.db import models

# Create your models here.
class FileModel(models.Model):
    file = models.FileField(upload_to='file_converter/media/')
    original_file = models.FileField(upload_to='original_files/')
    conversion_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
