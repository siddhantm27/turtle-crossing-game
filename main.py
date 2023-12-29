import turtle
from turtle import Turtle, Screen
from player import Player
from cars import Car

import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()

CARS = []
screen.update()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_on = True
while game_on:
    new_car = Car()
    CARS.append(new_car)
    for car in CARS:
        car.move_car()
    time.sleep(0.2)
    screen.update()

screen.exitonclick()
