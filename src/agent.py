class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def position(self):
        return self.x, self.y

    def move(self, action):
        if action == "UP":
            self.y -= 1

        elif action == "DOWN":
            self.y += 1

        elif action == "LEFT":
            self.x -= 1

        elif action == "RIGHT":
            self.x += 1