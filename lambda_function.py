import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html>
<html>
<head>
    <title>My Lambda Webpage</title>
</head>
<body>
    <h1>You did it!</h1>
    <br> <br>
    <p>This page is served from an AWS Lambda container.</p>
</body>
</html>"""

def lambda_handler(event, context):
    """AWS Lambda handler function"""
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": home()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
