from rest_framework import serializers
from .models import FileModel
# from PIL import Image
# from io import BytesIO

class FileConversionSerializer(serializers.Serializer):
    # file = serializers.FileField()
    class Meta:
        models = FileModel
        fields = '__all__'
    # def save(self):
    #     input_file = self.validated_data['file']

    #     # Perform the file conversion
    #     converted_file = self.perform_conversion(input_file)

    #     # Save the converted file in a temporary file
    #     with BytesIO(converted_file) as converted_file_io:
    #         # Save the converted file in the Django model
    #         converted_file_model = FileModel()
    #         converted_file_model.file.save(input_file.name, converted_file_io)
    #         converted_file_model.original_file = input_file
    #         converted_file_model.conversion_type = 'png'  # Replace with your desired conversion type
    #         converted_file_model.save()

    #         return converted_file_model

    # @staticmethod
    # def perform_conversion(input_file):
    #     # File conversion logic using Pillow library
    #     image = Image.open(input_file)
    #     converted_image = image.convert('PNG')
    #     converted_image_io = BytesIO()
    #     converted_image.save(converted_image_io, format='PNG')
    #     converted_image_io.seek(0)

    #     return converted_image_io

    # @staticmethod
    # def perform_conversion(input_file):
    #     # File conversion logic using Pillow library
    #     breakpoint()
    #     image = Image.open(input_file)
    #     print("sssssssssssssssssssssssssss",image)
    #     converted_image = image.convert('jpg')
    #     return converted_image