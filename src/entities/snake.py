from src.settings import GRID_SIZE

class Snake:
    def __init__(self, resource_manager):
        self.image = resource_manager.images.get('block')
        self.direction = 'down'
        self.length = 1
        # Start the snake in the middle of the screen
        self.x = [GRID_SIZE * 5]
        self.y = [GRID_SIZE * 5]

    def move_left(self):
        if self.direction != 'right': self.direction = 'left'

    def move_right(self):
        if self.direction != 'left': self.direction = 'right'

    def move_up(self):
        if self.direction != 'down': self.direction = 'up'

    def move_down(self):
        if self.direction != 'up': self.direction = 'down'

    def walk(self):
        # Shift body parts
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # Move head
        if self.direction == 'left':
            self.x[0] -= GRID_SIZE
        elif self.direction == 'right':
            self.x[0] += GRID_SIZE
        elif self.direction == 'up':
            self.y[0] -= GRID_SIZE
        elif self.direction == 'down':
            self.y[0] += GRID_SIZE

    def increase_length(self):
        self.length += 1
        # FIX: Append the exact position of the last tail piece!
        self.x.append(self.x[-1])
        self.y.append(self.y[-1])

    def draw(self, surface):
        for i in range(self.length):
            surface.blit(self.image, (self.x[i], self.y[i]))