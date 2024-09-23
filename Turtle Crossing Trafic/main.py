import time
from turtle import Screen
from car_manager import CarManager
from player import Player 
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

rosbiff_the_turtle = Player()
scoreboard = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkey(rosbiff_the_turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_forward()   

    for car in car_manager.cars:
        if rosbiff_the_turtle.distance(car) < 20:
            game_is_on = scoreboard.colision()

    if rosbiff_the_turtle.ycor() == 280:
        rosbiff_the_turtle.initial_position()
        car_manager.next_level()
        scoreboard.increase_score()
    



screen.exitonclick()