import awsgi
from app.main import app

def lambda_handler(event, context):
    return awsgi.response(app, event, context)