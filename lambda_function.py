from app.main import app

def lambda_handler(event, context):
    """Lambda Entry Point"""
    return {
        "statusCode": 200,
        "body": "Lambda is up and running!"
    }