from turtle import Turtle

LENGTH_OF_SNAKE = 3
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_COORDINATES:
            self.add_segment(position)

    def add_segment(self, position):
        new_element = Turtle()
        new_element.penup()
        new_element.shape("square")
        new_element.color("white")
        new_element.goto(position)
        self.snake.append(new_element)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def growth(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for snake_seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_seg - 1].xcor()
            new_y = self.snake[snake_seg - 1].ycor()
            self.snake[snake_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)