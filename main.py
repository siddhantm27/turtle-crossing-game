from turtle import Turtle, Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)
screen.onkeypress(key="Down", fun=player.move_down)

CARS = []
screen.update()

score = Scoreboard()

level = 1
t = 0

game_on = True
while game_on:

    score.refresh_score(level)

    if t % 6 == 0:  # reduces frequency of generation of cars
        new_car = Car(level)
        CARS.append(new_car)
    t += 1

    for car in CARS:
        car.move_car()
        if car.check_collision(player):
            game_on = False
            score.game_over()
            break

    if player.level_up():
        score.refresh_score(level)
        time.sleep(1)
        level += 1

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
