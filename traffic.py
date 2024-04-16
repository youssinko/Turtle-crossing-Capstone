from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'yellow', 'orange']
class Traffic:
    def __init__(self):
        self.all_cars = []
        self.speed = 10


    def cars(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            new_y = random.randint(-140, 180)
            car.goto(280, new_y)
            self.all_cars.append(car)
    def moving(self):
        for x in self.all_cars:
            x.backward(self.speed)
            # new_x = x.xcor() - 10
            # x.goto(new_x, x.ycor())
    def faster(self):
        self.speed += 10
