from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint(
    "agent",
    __name__,
    url_prefix="/agent",
    description="Route for agent operations"
    )

@blp.route("/")
class Agent(MethodView):
    
    blp.response(200)
    def get(self):
        return "nice"