from flask_smorest import Blueprint

blp = Blueprint(
    "agent",
    __name__,
    url_prefix="agent",
    description="Route for agent operations"
    )
