import os

from flask import Flask

from src.main.configs.create_tables import create_user_table
from src.main.routes.health_route import health_route
from src.main.routes.user.user_route import user_routes


def configure_all(app: Flask):
    config_environments()
    routes_config(app)
    create_tables()


def config_environments():
    os.environ['FLASK_DEBUG'] = "1"


def routes_config(app: Flask):
    app.register_blueprint(health_route, url_prefix="/health")
    app.register_blueprint(user_routes, url_prefix="/users")


def create_tables():
    create_user_table()
