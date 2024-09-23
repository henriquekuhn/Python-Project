from turtle import Turtle

FONT_SCORE = ("Courier", 10, "normal")
FONT_GAME_OVER = ("Courier", 24, "normal")
ALIGNMNENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-240, 270)
        self.score = 0
        self.update_scoreboard()

    def colision(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMNENT, font=FONT_GAME_OVER)
        return False
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align=ALIGNMNENT, font=FONT_SCORE)

    def increase_score(self):        
        self.score += 1
        self.update_scoreboard()

