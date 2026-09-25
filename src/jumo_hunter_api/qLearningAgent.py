import random

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}          # estado (tupla) -> [valor_cima, valor_baixo, valor_esquerda, valor_direita]
        self.alpha = alpha         # taxa de aprendizado
        self.gamma = gamma         # o quanto valoriza recompensa futura
        self.epsilon = epsilon     # chance de explorar em vez de usar o melhor conhecido
        self.last_state = None
        self.last_action = None

    def discretize(self, dx, dy):
        def sign(v):
            if v > 0:
                return 1
            elif v < 0:
                return -1
            return 0
        return (sign(dx), sign(dy))

    def _ensure_state(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0.0, 0.0, 0.0, 0.0]

    def choose_action(self, state):
        self._ensure_state(state)
        if random.random() < self.epsilon:
            return random.randint(0, 3)
        values = self.q_table[state]
        return values.index(max(values))

    def learn(self, state, action, reward, next_state, done):
        self._ensure_state(state)
        self._ensure_state(next_state)
        current_value = self.q_table[state][action]
        next_max = 0.0 if done else max(self.q_table[next_state])
        target = reward + self.gamma * next_max
        self.q_table[state][action] += self.alpha * (target - current_value)

    def reset_episode(self):
        self.last_state = None
        self.last_action = None