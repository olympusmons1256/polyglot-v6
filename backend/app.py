import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
GITHUB_API_URL = "https://api.github.com"
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
REPO_OWNER = "olympusmons1256"
REPO_NAME = "polyglot-v6"

@app.route('/api/directory', methods=['GET'])
def get_directory_contents():
    path = request.args.get('path', '')
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

@app.route('/api/file', methods=['GET'])
def get_file_contents():
    path = request.args.get('path', '')
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    content = response.json()['content']
    return jsonify({"content": content})

@app.route('/api/file', methods=['PUT'])
def update_file_contents():
    path = request.json['path']
    content = request.json['content']
    message = request.json['message']
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {
        "message": message,
        "content": content,
        "branch": "main"
    }
    response = requests.put(url, headers=headers, json=data)
    return jsonify(response.json())

@app.route('/api/claude', methods=['POST'])
def ask_claude():
    prompt = request.json['prompt']
    headers = {
        "Content-Type": "application/json",
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01"
    }
    data = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    response = requests.post(CLAUDE_API_URL, headers=headers, json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)