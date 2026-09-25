from qLearningAgent import QLearningAgent

agent = QLearningAgent()
state = (1, 0)      # comida à direita
next_state = (0, -1) # ainda à direita (não se moveu o suficiente pra mudar de bucket)

for _ in range(20):
    action = agent.choose_action(state)
    agent.learn(state, action, reward=1.0, next_state=next_state, done=False)
    print(agent.q_table[state])