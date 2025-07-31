from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "success": True,
        "message": "Hello from Vercel Python API!",
        "your_ip": request.remote_addr
    })

# Required for Vercel to recognize the Flask app
def handler(environ, start_response):
    return app(environ, start_response)
