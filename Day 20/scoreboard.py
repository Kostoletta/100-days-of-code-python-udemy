from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
