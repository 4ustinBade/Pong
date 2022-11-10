from turtle import Turtle

MOVE_DISTANCE = 25
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle(Turtle):  

    def __init__(self) :
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4, outline=None)
        self.left(90)
        self.goto(-380 , 0)
        self.speed("fastest")
        self.color("white")
        self.penup()

    # Move
    def move_up(self):
        self.seth(UP)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.seth(DOWN)
        self.forward(MOVE_DISTANCE)



    