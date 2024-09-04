import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()
car_manager = CarManager()

screen.listen()

screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) <= 20:
            game_is_on = False
            score_board.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        score_board.update_score()
        car_manager.level_up()

if game_is_on != True:
    
    score_board.level = 0
    player.goto(0, -280)
    game_is_on = True



screen.exitonclick()