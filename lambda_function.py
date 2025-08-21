import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Workshop demo</title>
</head>
<body>
    <h1>The best way to predict the future is to deploy it!</h1>
    <br> <br>
    <p>This page is served from an AWS Lambda.</p>
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
