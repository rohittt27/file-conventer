# Base image
FROM python:3.8-slim


ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /code/

# Expose the port for the Django server
EXPOSE 8000

# Define the command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
