class InteriorEnv:
    def __init__(self):
        self.state = {}

    def reset(self):
        self.state = {
            "style": "modern",
            "budget": 5000,
            "room_size": 200
        }
        return self.state

    def step(self, action):
        reward = 0

        if action == "add_modern_furniture":
            reward += 10
        elif action == "add_luxury_item":
            reward += 7
        elif action == "add_minimal_design":
            reward += 5

        done = True
        return self.state, reward, done, {}
