from turtle import Turtle
import os 

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
DIRECTORY = os.getcwd()+"/Snake Game"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        os.chdir(DIRECTORY)
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        #self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT) 
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1 
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} // High score: {self.high_score}", align=ALIGNMENT, font=FONT) 


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.save()
        self.update_scoreboard()

    def save(self):
        with open("score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

        