from dataclasses import dataclass

from flask import jsonify

from src.main.response.internal_code import InternalCode


@dataclass
class APIResponse:
    status: str
    http_status: int
    internal_code: InternalCode
    data: any = None

    @staticmethod
    def build_response(status, http_status, internal_code, data=None):
        return APIResponse(status, http_status, internal_code, data)

    @staticmethod
    def success_response(data=None):
        return APIResponse.build_response("success", 200, InternalCode.SUCCESS, data)

    @staticmethod
    def bad_request_response(data=None):
        return APIResponse.build_response("error", 400, InternalCode.BAD_REQUEST, data)

    @staticmethod
    def not_found_response(data=None):
        return APIResponse.build_response("error", 404, InternalCode.NOT_FOUND, data)

    @staticmethod
    def error_response(data=None):
        return APIResponse.build_response("error", 500, InternalCode.INTERNAL_ERROR, data)

    def to_json(self):
        data: dict = {
            "status": self.status,
            "http_status": self.http_status,
            "internal_code": self.internal_code.value,
            "data": self.data
        }

        return jsonify(data)
