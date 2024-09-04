import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def populate(self, amount):
        for i in range(amount):
            self.add_car()

    def add_car(self):
        d6 = random.randint(1, 6)
        if d6 == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.speed(0)
            random_y = random.randint(-250, 250)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random_y)
            car.seth(180)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
