from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_text = Score()
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

    # Detect collision with the food
    if food.distance(snake.head) < 15:
        score_text.increase_score()
        food.go_to_new_location()

    # Detect collision with Wall
    if snake.head.xcor() == -280 or snake.head.xcor() == 280 or snake.head.ycor() == 280 or snake.head.ycor() == -280:
        print("you bumped the wall")
        score_text.lost_text()
        game_on = False

screen.exitonclick()
