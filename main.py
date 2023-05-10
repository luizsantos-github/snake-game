from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

COLLISION_BOUNDARY_POSITIVE = 280
COLLISION_BOUNDARY_NEGATIVE = -280

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Luiz Snake Game")
screen.tracer(0)

# Initialize Snake
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


# Game Start
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > COLLISION_BOUNDARY_POSITIVE or snake.head.xcor() < COLLISION_BOUNDARY_NEGATIVE or \
            snake.head.ycor() > COLLISION_BOUNDARY_POSITIVE or snake.head.ycor() < COLLISION_BOUNDARY_NEGATIVE:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
