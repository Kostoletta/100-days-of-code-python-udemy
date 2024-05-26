from turtle import Turtle

PADDLE_WIDTH = 20 / 20
PADDLE_HEIGHT = 100 / 20
PADDLE_COLOR = "white"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.speed(0)
        self.penup()
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_len=PADDLE_HEIGHT, stretch_wid=PADDLE_WIDTH)
        self.setheading(90)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def go_down(self):
        if self.ycor() > -230:
            self.back(20)
