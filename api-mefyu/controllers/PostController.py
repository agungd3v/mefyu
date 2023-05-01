from flask import request, jsonify, make_response
from werkzeug.utils import secure_filename
from services.checkcontent import checkf

def index():
  message = jsonify(message = "PostController OK")
  return make_response(message, 200)

def store():
  content = request.files["content"]
  content.save("static/" + secure_filename(content.filename))
  s = checkf("static/" + secure_filename(content.filename))
  return make_response(jsonify(message = s), 200)
