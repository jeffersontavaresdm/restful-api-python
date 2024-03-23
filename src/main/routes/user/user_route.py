from flask import Blueprint, request

from src.main.annotations.exception_handler import exception_handler
from src.main.models.user import User, UserPayload
from src.main.repositories.user_repository import get_users, create_user, update_user, delete_user
from src.main.response.response import APIResponse


class UserRoutes:
    def __init__(self):
        self.user_route = Blueprint("user", __name__)
        self.register_routes()

    def register_routes(self):
        self.user_route.add_url_rule("/", view_func=self.create, methods=["POST"])
        self.user_route.add_url_rule("/", view_func=self.get_all, methods=["GET"])
        self.user_route.add_url_rule("/<int:user_id>", view_func=self.update, methods=["PUT"])
        self.user_route.add_url_rule("/<int:user_id>", view_func=self.delete, methods=["DELETE"])

    @exception_handler
    def create(self):
        payload = UserPayload(**request.json)
        create_user(payload.name, payload.email)
        return APIResponse.success_response(payload).to_json(), 201

    @exception_handler
    def get_all(self):
        users: list[User] = get_users()
        return APIResponse.success_response(users).to_json(), 200

    @exception_handler
    def update(self, user_id: int):
        payload = UserPayload(**request.json)
        update_user(payload, user_id)
        return APIResponse.success_response(payload).to_json(), 200

    @exception_handler
    def delete(self, user_id: int):
        delete_user(user_id)
        return APIResponse.success_response().to_json(), 200


user_routes = UserRoutes().user_route
