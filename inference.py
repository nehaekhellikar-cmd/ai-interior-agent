 inference.py

from environment import InteriorEnv
from grader import grade_design

class InteriorAgent:
    def _init_(self):
        self.actions = [
            "add_modern_furniture",
            "add_luxury_item",
            "add_minimal_design"
        ]

    def choose_action(self):
        # Simple logic: choose best action based on grading
        best_action = None
        best_score = -1

        for action in self.actions:
            score = grade_design(action)

            if score > best_score:
                best_score = score
                best_action = action

        return best_action


def run_inference():
    env = InteriorEnv()
    state = env.reset()

    print("Initial State:", state)

    agent = InteriorAgent()
    action = a…
