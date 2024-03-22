from flask import Blueprint, request

from src.main.models.user import User, UserPayload
from src.main.repositories.user_repository import get_users, create_user, update_user, delete_user
from src.main.response.response import APIResponse

user_route = Blueprint("user", __name__)


@user_route.route("/", methods=["POST"])
def create() -> tuple:
    try:
        payload = UserPayload(**request.json)

        create_user(payload.name, payload.email)

        return APIResponse.success_response(payload).to_json(), 201
    except Exception as exception:
        error_message = str(exception)
        return APIResponse.error_response(error_message).to_json(), 500


@user_route.route("/", methods=["GET"])
def get_all():
    users: list[User] = get_users()
    return APIResponse.success_response(users).to_json(), 200


@user_route.route("/<int:user_id>", methods=["PUT"])
def update(user_id: int):
    try:
        payload = UserPayload(**request.json)

        update_user(payload, user_id)

        return APIResponse.success_response(payload).to_json(), 200
    except Exception as exception:
        error_message = str(exception)
        return APIResponse.error_response(error_message).to_json(), 500


@user_route.route("/<int:user_id>", methods=["DELETE"])
def delete(user_id: int):
    try:
        delete_user(user_id)

        return APIResponse.success_response().to_json(), 200
    except Exception as exception:
        error_message = str(exception)
        return APIResponse.error_response(error_message).to_json(), 500
