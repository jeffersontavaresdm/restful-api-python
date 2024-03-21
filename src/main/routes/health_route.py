from flask import Blueprint, jsonify

health_route = Blueprint("health", __name__)


@health_route.route("/", methods=["GET"])
def health() -> tuple:
    return jsonify({"health": "up"}), 200
