from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.pensize(10)
tim.speed(5)

colors = ["red", "green", "blue", "orange", "purple", "yellow", "violet", "gray"]

direction = {
    "east": 0,
    "north": 90,
    "west": 180,
    "south": 270,
}


for _ in range(50):
    # tim will do a random walk
    random_direction = random.choice(list(direction.values()))  # picks a random direction
    random_color = random.choice(colors)  # picks a random color
    tim.pencolor(random_color)
    tim.setheading(random_direction)
    tim.forward(50)  # tim moves forward


screen.exitonclick()
