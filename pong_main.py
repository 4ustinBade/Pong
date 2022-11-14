from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import Scoreboard
import time

change_direction_y = False
change_direction_x = False

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

# Create score board
score = Scoreboard()

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
    # Decide up or down movement
    if not change_direction_y and not change_direction_x : 
        ball.move_ball_up_r()
    elif change_direction_y and not change_direction_x :
        ball.move_ball_down_r()
    elif change_direction_x and  change_direction_y :
        ball.move_ball_down_l()
    elif change_direction_x and not change_direction_y :
        ball.move_ball_up_l()

    # Deal with collision on walls
    if ball.ycor() > 280 :
        ball.bounce_right()
        ball.move_ball_down_r()
        change_direction_y = True
       
    # Bounce left up
    elif ball.ycor() < -280:
        ball.bounce_left()
        ball.move_ball_down_l()
        change_direction_y = False
    
    # Paddle Collision
    if ball.distance(paddle_one) < 20 :
        change_direction_x = False
        ball.speed_up()
   
    elif ball.distance(paddle_two) < 20 :
        change_direction_x = True
        ball.speed_up()
        
    # Handle goals
    if ball.xcor() > 380 : 
        score.refresh_p1()
        time.sleep(2)
        ball.goto(0,0)
        ball.reset_speed()
        
    elif ball.xcor() < -380 :
        score.refresh_p2()
        time.sleep(2)
        ball.goto(0,0)
        ball.reset_speed()
        
# Exit
screen.exitonclick()