from turtle import Turtle

BALL_HEIGHT = 20 / 20
BALL_WIDTH = 20 / 20
BALL_COLOR = "white"
BALL_SPEED = 4
BALL_DIRECTION = 45


class Ball(Turtle):
    def __init__(self, scoreboard, position=(0, 0)):
        super().__init__()
        self.scoreboard = scoreboard
        self.penup()
        self.color(BALL_COLOR)
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_WIDTH, stretch_len=BALL_HEIGHT)
        self.goto(position)

        self.direction = BALL_DIRECTION
        self.ball_speed = BALL_SPEED
        self.setheading(BALL_DIRECTION)

    def move(self):
        self.forward(self.ball_speed)

    def check_collide_with_wall(self):
        if self.ycor() > 280 or self.ycor() < - 280:
            self.bouncey()
        elif self.xcor() > 380:
            self.goto((0, 0))
            self.ball_speed *= -1
            self.scoreboard.l_point()
        elif self.xcor() < -380:
            self.goto((0, 0))
            self.ball_speed *= -1
            self.scoreboard.r_point()

    def bouncey(self):
        self.setheading(-self.heading())

    def bouncex(self):
        self.ball_speed *= -1.1
