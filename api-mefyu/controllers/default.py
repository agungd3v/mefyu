from flask import jsonify, make_response

def default():
  message = jsonify(message = "OK")
  return make_response(message, 200)