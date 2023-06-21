from turtle import Turtle

class Walls(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-290, 290)
        self.pendown()
        self.forward(580)
        self.setheading(270)
        self.forward(580)
        self.setheading(180)
        self.forward(580)
        self.setheading(90)
        self.forward(580)
