from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
colors = ["red", "green", "blue", "orange", "purple", "yellow", "violet", "gray"]

direction = {
    "east": 0,
    "north": 90,
    "west": 180,
    "south": 270,
}

tim.pensize(10)
tim.speed(5)


for _ in range(50):
    random_direction = random.choice(list(direction.values()))
    random_color = random.choice(colors)
    tim.pencolor(random_color)
    tim.setheading(random_direction)
    tim.forward(50)


screen.exitonclick()
