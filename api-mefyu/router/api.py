from flask import Blueprint
from controllers.default import default
from controllers.PostController import index, store

api = Blueprint("", __name__)

api.route("/")(default)
api.route("/post")(index)
api.route("/post", methods = ["POST"])(store)