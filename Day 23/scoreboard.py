from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=-220, y=260)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def add_point(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(x=-0, y=0)
        self.write(f"GAME OVER", align="center", font=FONT)
