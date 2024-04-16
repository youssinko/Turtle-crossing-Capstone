import turtle
from turtle import Turtle, Screen
from car import Car
from traffic import Traffic
import time
from scoreboard import Score

screen = Screen()
screen.tracer(0)
screen.setup(600, 400)
car = Car()
traffic = Traffic()
score = Score()
screen.listen()
screen.onkey(car.movingUp, 'Up')

game_on = True
while game_on:
    time.sleep(0.2)
    screen.update()
    traffic.cars()
    traffic.moving()

    for each in traffic.all_cars:
        if each.distance(car) < 20:
            game_on= False
            turtle.color('red')
            turtle.write(f" Game Over", align='center', font=('Arial', 30, 'normal'))
    if car.ycor() > 180:
        car.goto(0, -180)
        score.increase_score()
        traffic.faster()

screen.exitonclick()

