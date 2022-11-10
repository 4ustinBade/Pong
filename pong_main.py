from turtle import Screen
from paddles import Paddle
from ball import Ball
import time



# Screen set up
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# Create paddles
paddle_one = Paddle()
paddle_two = Paddle()
paddle_two.goto(375,0)

# Create ball
ball = Ball()

# Establish paddle control
screen.listen()
screen.onkey(paddle_one.move_up, "w")
screen.onkey(paddle_one.move_down, "s")

screen.onkey(paddle_two.move_up, "i")
screen.onkey(paddle_two.move_down, "k")

# Running
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    # Detect collision with walls
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()



# Exit
screen.exitonclick()