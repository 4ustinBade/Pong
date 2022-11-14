from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle) : 
    
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white") 
        self.goto(0, 240)
        self.p1_score = 0
        self.p2_score = 0
        self.write(f"{self.p1_score}  {self.p2_score}", False, align = ALIGNMENT, font = FONT)

    def move(self, direction):
        self.goto(direction, 240)   
    
    def refresh_p1(self) :
        self.p1_score += 1
        self.clear()
        self.write(f"{self.p1_score}  {self.p2_score}", False, align = ALIGNMENT, font = FONT)
    
    def refresh_p2(self) :
        self.p2_score += 1
        self.clear()
        self.write(f"{self.p1_score}  {self.p2_score}", False, align = ALIGNMENT, font = FONT)

