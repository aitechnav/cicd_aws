from app.main import app
from awsgi import WSGIMiddleware

def lambda_handler(event, context):
    return WSGIMiddleware(app).handle(event, context)