from flask import request, jsonify, make_response
from werkzeug.utils import secure_filename

def index():
  message = jsonify(message = "PostController OK")
  return make_response(message, 200)

def store():
  content = request.files["content"]
  content.save("static/" + secure_filename(content.filename))
  return make_response(jsonify(message = "OK"), 200)
