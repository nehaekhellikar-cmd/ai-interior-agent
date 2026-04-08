from environment import InteriorEnv
from grader import grade_design

env = InteriorEnv()
state = env.reset()

print("Initial State:", state)

action = "add_modern_furniture"

new_state, reward, done, _ = env.step(action)

score = grade_design(action)

print("Action:", action)
print("Reward:", reward)
print("Score:", score)
