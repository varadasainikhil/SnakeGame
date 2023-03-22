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
        self.highscore = self.get_highscore()
        self.color("white")
        self.write(f"Score : {self.score} HighScore : {self.highscore}", align=ALIGNMENT, font=(FONT, 15, 'normal'))

    def get_highscore(self):
        with open("data.txt") as file:
            x = file.read()
            highscore = int(x)
        return highscore

    def update_highscore(self, score):
        with open("data.txt", mode="w") as file:
            file.write(str(score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.highscore}", align=ALIGNMENT, font=(FONT, 15, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.update_highscore(self.score)
            self.highscore = self.get_highscore()
        self.score = 0
        self.update_scoreboard()
