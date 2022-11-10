from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
X_LIST = []
Y_LIST =  [] 
DIRECTION = " "

class Ball(Turtle):  

    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=.4, stretch_len=.4, outline=None)
        self.speed("fastest")
        self.color("white")
        self.penup()

    # Move ball
    def move_ball(self) :
        # Move ball based on direction
        if DIRECTION == " " :
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
            X_LIST.append(self.xcor())
        elif DIRECTION == "right":
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
            X_LIST.append(self.xcor())
        elif DIRECTION == "left":
            new_x = self.xcor() - 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)
            X_LIST.append(self.xcor())
        # Determine direction of travel
        if X_LIST[len(X_LIST)-1] > X_LIST[len(X_LIST)-2] :
         DIRECTION = "right"
        elif X_LIST[len(X_LIST)-1] < X_LIST[len(X_LIST)-2] :
         DIRECTION = "left"
        
    # Bounce ball
    def bounce(self) :
        if DIRECTION == "right" :
            new_x = self.xcor() - 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)


        

        