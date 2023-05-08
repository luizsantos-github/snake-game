from turtle import Screen
from snake import Snake
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Luiz Snake Game")
screen.tracer(0)

# Initialize Snake
snake = Snake()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


# Game Start
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

screen.exitonclick()
