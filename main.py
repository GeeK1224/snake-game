from turtle import Screen, register_shape
from snake import Snake
from scoreboard import Scoreboard
from food import Food
from walls import Walls
import time

# SCREEN SETUP
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)

# OBJECTS
snake = Snake()
score = Scoreboard()
food = Food()
walls = Walls()

# GAME CONTROLS
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

# GAME
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Food detection
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.growth()
        score.get_score()
        screen.update()

# Wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
# Tail collision
    for element in snake.snake:
        if element == snake.head:
            pass
        elif snake.head.distance(element) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()
