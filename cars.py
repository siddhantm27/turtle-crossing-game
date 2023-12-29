from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "blue", "purple", "brown", "green", "cyan", "coral", "navy"]


class Car(Turtle):

    def __init__(self, level):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.speed("fastest")
        self.goto(x=300, y=random.randrange(-250, 250, step=10))
        self.car_speed = 5 * level

    def move_car(self):
        self.forward(self.car_speed)

    def check_collision(self, player):
        return abs(self.xcor()) <= 30 and abs(self.ycor() - player.ycor()) <= 20
