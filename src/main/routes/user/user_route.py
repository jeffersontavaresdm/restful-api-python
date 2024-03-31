from typing import Any

from flask import Blueprint, request

from src.main.annotations.exception_handler import exception_handler
from src.main.models.user import User, UserPayload
from src.main.repositories.user_repository import get_users, create_user, update_user, delete_user, get_user_by_id, \
    get_user_by_name
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
        self.user_route.add_url_rule("/<int:user_id>", view_func=self.get_user_by_id, methods=["GET"])
        self.user_route.add_url_rule("/search-by-name", view_func=self.get_user_by_name, methods=["GET"])

    @exception_handler
    def create(self) -> tuple[Any, int]:
        payload = UserPayload(**request.json)
        create_user(payload.name, payload.email)
        return APIResponse.success_response(payload).to_json(), 201

    @exception_handler
    def get_all(self) -> tuple[Any, int]:
        users: list[User] = get_users()
        return APIResponse.success_response(users).to_json(), 200

    @exception_handler
    def update(self, user_id: int) -> tuple[Any, int]:
        payload = UserPayload(**request.json)
        update_user(payload, user_id)
        return APIResponse.success_response(payload).to_json(), 200

    @exception_handler
    def delete(self, user_id: int) -> tuple[Any, int]:
        delete_user(user_id)
        return APIResponse.success_response().to_json(), 200

    @exception_handler
    def get_user_by_id(self, user_id) -> tuple[Any, int]:
        user = get_user_by_id(user_id)
        return APIResponse.success_response(user).to_json(), 200

    @exception_handler
    def get_user_by_name(self) -> tuple[Any, int]:
        user_name = request.args.get('user_name')
        user = get_user_by_name(user_name)
        return APIResponse.success_response(user).to_json(), 200


user_routes = UserRoutes().user_route
