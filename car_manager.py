import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 5
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.left(90)
        self.penup()
        self.goto(290, random.randint(-250, 250))

    def move_car(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
