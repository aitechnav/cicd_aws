from aws_wsgi_middleware import WSGIMiddleware
from app.main import app

def lambda_handler(event, context):
    return WSGIMiddleware(app).handle(event, context)