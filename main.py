from src.agent import Agent
from src.environment import Environment


agent = Agent(x=0, y=0)

env = Environment(
    width=4,
    height=4,
    goal=(3, 3),
    obstacles=[(1, 1), (1, 2)]
)

print("Initial state:")
env.render(agent)

success = agent.move("RIGHT", env)
print("\nAfter RIGHT:")
print("Movement success:", success)
env.render(agent)

success = agent.move("DOWN", env)
print("\nAfter DOWN:")
print("Movement success:", success)
env.render(agent)

agent.move("UP", env)
agent.move("LEFT", env)
agent.move("LEFT", env)

print("\nAfter trying to cross LEFT boundary:")
env.render(agent)

print("\nBoundary tests:")
print(env.is_within_bounds((2, 2)))
print(env.is_within_bounds((3, 3)))
print(env.is_within_bounds((-1, 0)))
print(env.is_within_bounds((4, 2)))