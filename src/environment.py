class Environment:
    def __init__(self, width=4, height=4, goal=(3, 3), obstacles=None):
        self.width = width
        self.height = height
        self.goal = goal
        self.obstacles = obstacles or []

    #Apakah coordinate masih di dalam grid?
    def is_within_bounds(self, position):
        x, y = position

        return 0 <= x < self.width and 0 <= y < self.height

    #Apakah di dalam grid AND bukan obstacle?
    def is_valid_position(self, position):
        return (
        self.is_within_bounds(position)
        and position not in self.obstacles
    )

    def render(self, agent):
        for y in range(self.height):
            row = []

            for x in range(self.width):
                if (x, y) == agent.position:
                    row.append("A")
                elif (x, y) == self.goal:
                    row.append("G")
                elif (x, y) in self.obstacles:
                    row.append("X")
                else:
                    row.append(".")

            print(" ".join(row))