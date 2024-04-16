from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 180)
        self.write(f"SCORE :{self.score}  LEVEL: {self.level}", align='left', font=('Arial', 10, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.level += 1
        self.write(f"SCORE :{self.score}  LEVEL: {self.level}", align='left', font=('Arial', 10, 'normal'))

