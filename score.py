from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=(FONT, 15, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=(FONT, 15, 'normal'))

    def lost_text(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT, 24, 'normal'))