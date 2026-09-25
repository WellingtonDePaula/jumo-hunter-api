class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {}          # estado (tupla) -> lista de valores por ação
        self.alpha = alpha         # taxa de aprendizado
        self.gamma = gamma         # quanto valoriza recompensa futura
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

    def choose_action(self, state):
        # epsilon-greedy: às vezes ação aleatória, às vezes a de maior valor em self.q_table[state]
        pass

    def learn(self, state, action, reward, next_state, done):
        # atualização de Bellman em self.q_table
        pass