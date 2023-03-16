from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
game_on = True

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
