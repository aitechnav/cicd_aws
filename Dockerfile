# Use Amazon Linux 2 Lambda base image
FROM public.ecr.aws/lambda/python:3.9

# Set working directory
WORKDIR /var/task

# Copy the application files
COPY app/ ./app/
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Command to run the Flask application
CMD ["app.main.app"]
