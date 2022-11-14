from turtle import Turtle

class Net(Turtle):  

    def __init__(self) :
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=.5, stretch_len=1, outline=None)
        self.left(90)
        self.speed("fastest")
        self.color("white")
        self.penup()