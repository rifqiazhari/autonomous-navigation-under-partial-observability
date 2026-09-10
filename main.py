from src.agent import Agent
from src.environment import Environment


agent = Agent(x=0, y=0)
env = Environment(width=4, height=4, goal=(3, 3))

print("Initial state:")
env.render(agent)

agent.move("RIGHT")

print("\nAfter RIGHT:")
env.render(agent)

agent.move("DOWN")

print("\nAfter DOWN:")
env.render(agent)