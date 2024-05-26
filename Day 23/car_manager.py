import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randint(1, 6)

        if random_num == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(x=320, y=random_y)

            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def check_collide(self, player):
        for car in self.cars:
            if car.ycor() - 20 <= player.ycor() <= car.ycor() + 20 and car.xcor() - 20 <= player.xcor() <= car.xcor() + 20:
                return True

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
