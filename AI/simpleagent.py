class SimpleAgent:
    def __init__(self, start, goal):
        self.position = start
        self.goal = goal

    def perceive(self):
        # Get the current position of the agent
        return self.position

    def act(self):
        # Decide the best action to take based on the goal
        if self.position < self.goal:
            self.position += 1  # Move right
        elif self.position > self.goal:
            self.position -= 1  # Move left
        return self.position

    def is_goal_reached(self):
        # Check if the agent has reached the goal
        return self.position == self.goal
start_position = 0
goal_position = 5
agent = SimpleAgent(start_position, goal_position)
steps = 0
while not agent.is_goal_reached():
    print(f"Step {steps}: Agent is at position {agent.perceive()}")
    agent.act()
    steps += 1

print(f"Goal reached at position {agent.perceive()} in {steps} steps.")
