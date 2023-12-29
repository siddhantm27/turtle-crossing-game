from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "purple", "brown", "green", "cyan", "coral", "navy"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.speed("fastest")
        self.goto(x=300, y=random.randrange(-285, 285,step=50))

    def move_car(self):
        self.forward(10)