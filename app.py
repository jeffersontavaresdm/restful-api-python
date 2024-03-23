from flask import Flask

from src.main.configs.routes_config import configure_all

app: Flask = Flask(__name__)

configure_all(app)

if __name__ == '__main__':
    app.run()
