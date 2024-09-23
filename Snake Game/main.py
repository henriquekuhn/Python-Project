from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("Snake Game")
screen.tracer(0)

rosbiff = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(rosbiff.up, "Up")
screen.onkey(rosbiff.down, "Down")
screen.onkey(rosbiff.left, "Left")
screen.onkey(rosbiff.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)    
    rosbiff.move()

    #detect colision with food
    if rosbiff.head.distance(food) < 15:
        food.refresh()
        rosbiff.grow_snake()
        scoreboard.increase_score()
        
    
    #Detect colision with wall
    if rosbiff.head.xcor() > 285 or rosbiff.head.xcor() < -285 or rosbiff.head.ycor() > 285 or rosbiff.head.ycor() < -285:        
        #game_is_on = False        
        #scoreboard.game_over()
        scoreboard.reset_score()
        rosbiff.reset_game()

    #Detect colision with tail. 
    for segment in rosbiff.segments[1:]:
        if rosbiff.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset_score()
            rosbiff.reset_game()


screen.exitonclick()    