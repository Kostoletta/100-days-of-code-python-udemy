from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("score.txt", mode="r") as f:
                self.high_score = int(f.read())
        except FileNotFoundError:
            with open("score.txt", mode="w") as f:
                f.write(str(0))
                self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
