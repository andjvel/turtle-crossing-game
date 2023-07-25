
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

cars = []
count = 0
num_of_cars = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    count += 1
    if count % 6 == 0:
        car = CarManager()
        car.move_car()
        cars.append(car)
    for car in cars:
        car.move_car()

        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.update_score()
        for car in cars:
            car.speed_up()


screen.exitonclick()