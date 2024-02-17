from turtle import Turtle, Screen
import random


def random_walk():

    for _ in range(50):
        # tim will do a random walk
        random_direction = random.choice(list(direction.values()))  # picks a random direction
        random_color = random.choice(colors)  # picks a random color
        tim.pencolor(random_color)
        tim.setheading(random_direction)
        tim.forward(50)  # tim moves forward


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

continue_random_walk = True

while continue_random_walk:

    random_walk()

    if input("Do you want to continue? Y/N: ").upper() == "N":
        continue_random_walk = False
        print("Exiting Application..")

screen.exitonclick()
