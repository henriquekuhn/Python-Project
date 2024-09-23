from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
left = 0
right = 0
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and right == 0:
        right = 1
        left = 0
        ball.paddle_colision()        

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320 and left == 0:
        right = 0
        left = 1
        ball.paddle_colision() 

    if ball.xcor() > 390:
        scoreboard.score(1)
        ball.reset_position()
    elif ball.xcor() < -390:
        scoreboard.score(2)
        ball.reset_position()

    if scoreboard.p1_score == 10:
        game_is_on = scoreboard.game_over(1)
    elif scoreboard.p2_score == 10:
        game_is_on = scoreboard.game_over(2)


screen.exitonclick()