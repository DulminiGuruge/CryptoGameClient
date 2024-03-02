# Use an official Python runtime as a parent image
FROM python:3.11-slim

ADD . /app
# Set the working directory to /app
WORKDIR /app

# install requirements
RUN pip3 install -r requirements.txt

# running port
EXPOSE 7655


# Run the command when the container starts
CMD ["python3",  "manage.py", "runserver", "0.0.0.0:8000"]