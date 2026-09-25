from flask import Flask
from flask_smorest import Api
from qLearningAgent import QLearningAgent

agent = QLearningAgent()

app = Flask(__name__)

app.config["API_TITLE"] = "API teste"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"


api = Api(app)

from agent import blp

api.register_blueprint(blp)