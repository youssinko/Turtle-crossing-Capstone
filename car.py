from turtle import Turtle
POSITION = (0, -180)
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color = 'red'
        self.shape('turtle')
        self.penup()
        self.goto(POSITION)
        self.setheading(90)
    def movingUp(self):
        self.forward(10)

