class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def position(self):
        return self.x, self.y

    def move(self, action, environment):
        new_x = self.x
        new_y = self.y

        if action == "UP":
            new_y -= 1

        elif action == "DOWN":
            new_y += 1

        elif action == "LEFT":
            new_x -= 1

        elif action == "RIGHT":
            new_x += 1

        new_position = (new_x, new_y)

        if environment.is_valid_position(new_position):
            self.x = new_x
            self.y = new_y
            return True
        return False