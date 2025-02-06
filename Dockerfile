# Use Amazon Linux 2 Lambda base image for Python 3.9
FROM public.ecr.aws/lambda/python:3.12

# Set working directory inside the container
WORKDIR /var/task

# Copy application files
COPY app/ ./app/
COPY lambda_function.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the Lambda handler
CMD ["lambda_function.lambda_handler"]
