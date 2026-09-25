from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint(
    "agent",
    __name__,
    url_prefix="/agent",
    description="Route for agent operations"
    )

@blp.route("/step")
class Step(MethodView):
    pass

@blp.route("/reset")
class Step(MethodView):
    pass