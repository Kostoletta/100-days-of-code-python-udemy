from turtle import Turtle

MOVE_DISTANCE = 20
INITIAL_SIZE = 3

DIRECTION = {
    "right": 0,
    "left": 180,
    "up": 90,
    "down": 270
}


class Snake:

    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[- 1]

    def create_snake(self):
        for i in range(INITIAL_SIZE):
            new_square = Turtle(shape="square")
            new_square.penup()
            new_square.color("white")
            new_square.goto(x=0 - 20 * i, y=0)
            self.snake_body.append(new_square)

    def add_segment(self):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(self.tail.pos())
        self.snake_body.append(new_square)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTION["down"]:
            self.head.setheading(DIRECTION["up"])

    def down(self):
        if self.head.heading() != DIRECTION["up"]:
            self.head.setheading(DIRECTION["down"])

    def left(self):
        if self.head.heading() != DIRECTION["right"]:
            self.head.setheading(DIRECTION["left"])

    def right(self):
        if self.head.heading() != DIRECTION["left"]:
            self.head.setheading(DIRECTION["right"])

    def eats(self, food):
        return True if self.head.distance(food.pos()) < 10 else False

    def has_collided(self):
        for segment in (self.snake_body[1:]):
            if self.head.distance(segment.pos()) < 10:
                return True
        return False

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]



