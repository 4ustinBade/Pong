from turtle import Turtle

MOVE_DISTANCE = 20
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=.6, stretch_len=.6, outline=None)
        self.color("white")
        self.penup()
        self.speed = 10

    # Move ball
    def move_ball_up_r(self):
        new_x = self.xcor() + self.speed
        new_y = self.ycor() + self.speed
        self.goto(new_x, new_y)
    
    def move_ball_down_r(self):
        new_x = self.xcor() + self.speed
        new_y = self.ycor() - self.speed
        self.goto(new_x, new_y)
    
    def move_ball_up_l(self):
        new_x = self.xcor() - self.speed
        new_y = self.ycor() + self.speed
        self.goto(new_x, new_y)
    
    def move_ball_down_l(self):
        new_x = self.xcor() - self.speed
        new_y = self.ycor() - self.speed
        self.goto(new_x, new_y)
        
    def bounce_right(self):
        new_x = self.xcor() + self.speed
        new_y = self.ycor() - self.speed
        self.goto(new_x, new_y)
    
    def bounce_left(self):
        new_x = self.xcor() - self.speed
        new_y = self.ycor() + self.speed
        self.goto(new_x, new_y)
    
    def speed_up(self) :
        self.speed += 4

    def reset_speed(self) :
        self.speed = 10 



    
