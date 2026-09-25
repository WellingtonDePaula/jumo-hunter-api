from flask.views import MethodView
from flask_smorest import Blueprint
from app import agent
from .schemas import StepSchema, ActionSchema

blp = Blueprint(
    "agent",
    __name__,
    url_prefix="/agent",
    description="Route for agent operations"
)


@blp.route("/step")
class Step(MethodView):
    @blp.arguments(StepSchema)
    @blp.response(200, ActionSchema)
    def post(self, step_data):
        dx, dy = step_data["observation"]
        next_state = agent.discretize(dx, dy)

        # a reward/done que chegaram agora são resultado da ÚLTIMA ação, não da próxima
        if agent.last_state is not None:
            agent.learn(
                agent.last_state,
                agent.last_action,
                step_data["reward"],
                next_state,
                step_data["done"],
            )

        if step_data["done"]:
            # episódio acabou: não escolhe ação nova, só limpa o estado interno
            agent.reset_episode()
            return {"action": 0}  # valor "morto" — Unity não deve usar, vai chamar /reset

        action = agent.choose_action(next_state)
        agent.last_state = next_state
        agent.last_action = action

        return {"action": action}


@blp.route("/reset")
class Reset(MethodView):
    @blp.response(200)
    def post(self):
        agent.reset_episode()
        return {"status": "ok"}