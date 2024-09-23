from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, paddle_position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(paddle_position)

    def go_up(self):
        if self.ycor() < 300:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)    

    def go_down(self):
        if self.ycor() > -300:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y) 

    