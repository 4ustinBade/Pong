from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle) : 
    
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white") 
        self.goto(0, 950)
        self.p1_score = 0
        self.p2_score = 0
        self.write(f"{self.p1_score}", False, align = ALIGNMENT, font = FONT)
        
    
    def refresh(self) :
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, align = ALIGNMENT, font = FONT)

