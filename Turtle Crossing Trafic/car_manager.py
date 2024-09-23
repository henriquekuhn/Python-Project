from turtle import Turtle
import random

VELOCITY_INCREMENT = 10
CAR_VELOCITY = 5
COLORS = ["green", "red", "yellow", "blue", "orange", "purple"]

class CarManager:
    def __init__(self):
        self.cars = []
        self.velocity = CAR_VELOCITY
        

    def create_car(self):
        create_new_car = random.randint(1,6)
        if create_new_car == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-260, 260))
            self.cars.append(new_car)


    def move_forward(self):
        for car in self.cars:
            car.backward(self.velocity)

    def next_level(self):
        self.velocity += VELOCITY_INCREMENT  
    
    