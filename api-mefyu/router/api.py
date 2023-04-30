from flask import Blueprint, jsonify, make_response
from controllers.default import default

api = Blueprint("", __name__)

api.route("/")(default)