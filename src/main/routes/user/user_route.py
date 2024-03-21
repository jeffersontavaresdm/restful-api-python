from flask import Blueprint, request

from src.main.models.user import User
from src.main.repository.user_repository import get_users
from src.main.response.response import APIResponse

user_route = Blueprint("user", __name__)


@user_route.route("/", methods=["POST"])
def create() -> tuple:
    data = request.json

    try:
        user = User(**data)
        return APIResponse.success_response(user).to_json(), 200
    except Exception as exception:
        error_message = str(exception)
        return APIResponse.error_response(error_message).to_json(), 500


@user_route.route("/", methods=["GET"])
def get_all():
    users: list[User] = get_users()
    return APIResponse.success_response(users).to_json(), 200
