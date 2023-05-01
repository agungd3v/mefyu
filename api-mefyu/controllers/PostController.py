from pathlib import Path
from uuid import uuid4
from flask import request, jsonify, make_response
from werkzeug.utils import secure_filename
from services.checkcontent import checkf

def index():
  message = jsonify(message = "PostController OK")
  return make_response(message, 200)

def store():
  content = request.files["content"]
  content.filename = str(uuid4()) + Path(secure_filename(content.filename)).suffix

  cs = "static/" + content.filename

  content.save(cs)
  s = checkf(cs)
  return make_response(jsonify(message = s), 200)
