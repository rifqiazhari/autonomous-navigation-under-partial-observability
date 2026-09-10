class Environment:
    def __init__(self, width=4, height=4, goal=(3, 3)):
        self.width = width
        self.height = height
        self.goal = goal

    def render(self, agent):
        for y in range(self.height):
            row = []

            for x in range(self.width):
                if (x, y) == agent.position:
                    row.append("A")
                elif (x, y) == self.goal:
                    row.append("G")
                else:
                    row.append(".")

            print(" ".join(row))