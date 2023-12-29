from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def level_up(self):
        if self.ycor() >= 300:
            self.goto(x=0, y=-280)
            return True
