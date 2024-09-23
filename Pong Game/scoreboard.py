from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score(0) 

    def score(self, player):
        if player == 1:
            self.p1_score += 1
        elif player == 2:
            self.p2_score += 1
        self.clear()
        self.write(f"{self.p1_score}  x  {self.p2_score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"Player {player} WON!!!", align=ALIGNMENT, font=FONT)
        return False