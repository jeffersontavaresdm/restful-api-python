from flask import Flask

from src.main.configs.routes_config import routes_config

app: Flask = Flask(__name__)

routes_config(app)

if __name__ == '__main__':
    app.run(debug=True)
