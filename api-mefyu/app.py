from flask import Flask
from router.api import api

app = Flask(__name__, static_url_path = "", static_folder = "static")
app.register_blueprint(api)

if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = 8000, debug = True)
