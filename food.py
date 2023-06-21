from turtle import Turtle, Screen
import random

screen = Screen()
screen.addshape("C:/Users/WINDOWS 10/JetBrains/PycharmProjects/SnakeGame/Burger.gif")

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("C:/Users/WINDOWS 10/JetBrains/PycharmProjects/SnakeGame/Burger.gif")
        self.shapesize(0.0005, 0.0005)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

