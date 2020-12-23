import turtle
from turtle import Screen

wn = Screen()
wn.bgcolor("#4b78bf")  # Slightly darker than snowflake color

class SnowFlake:
    def __init__(self, color, initAngle):
        # Turtle traits
        self.snow = turtle.Turtle()
        self.snow.color(color)
        self.snow.speed(2)
        self.snow.pensize(5)
        self.initAngle = initAngle

    def createFlake(self, bigStep, smallStep):
        # Instructions to creating a flake
        self.snow.left(self.initAngle)
        self.snow.forward(bigStep)
        self.snow.left(45)
        self.snow.forward(smallStep)
        for i in range(2):
            self.snow.backward(smallStep)
            self.snow.right(45)
            self.snow.forward(smallStep)
        self.snow.hideturtle()

def full_snowFlake():
    # Creating eight flakes
    for i in range(1, 9):
        snow_flake = SnowFlake("#a0b6d9", 45*i)
        snow_flake.createFlake(120, 65)

full_snowFlake()
turtle.done()
