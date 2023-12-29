from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-150, 270)
        self.ht()

    def refresh_score(self, level):
        self.clear()
        self.write(f"Level: {level}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write("GAME OVER", align="center", font=("Arial", 16, "normal"))
