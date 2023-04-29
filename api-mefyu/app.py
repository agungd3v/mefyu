from flask import Flask, jsonify, make_response, send_from_directory

app = Flask(__name__,
  static_url_path = "",
  static_folder = "static"
)

@app.route("/")
def index():
  response = jsonify(
    message = "ok"
  )
  return make_response(response, 200)
