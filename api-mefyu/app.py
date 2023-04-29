from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def index():
  response = jsonify(
    message = "ok"
  )
  return make_response(response, 200)