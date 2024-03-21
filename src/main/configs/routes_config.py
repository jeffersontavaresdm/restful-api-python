from flask import Flask

from src.main.routes.health_route import health_route
from src.main.routes.user.user_route import user_route


def routes_config(app: Flask):
    app.register_blueprint(health_route, url_prefix="/health")
    app.register_blueprint(user_route, url_prefix="/users")
