import turtle
jerry=turtle.Turtle()
jerry.speed(0)
"""
def square(size):
    for times in range(4):
        jerry.forward(size)
        jerry.left(90)
def triangle(size2):
    for times in range(3):
        jerry.forward(size2)
        jerry.left(120)
def pentagon(size3):
    for times in range(5):
        jerry.forward(size3)
        jerry.left(72)
        jerry.forward(10)
        jerry.left(10)
"""
def polygon(size,sides,color):
    angle=360/sides
    for times in range(sides):
        jerry.color(color)
        jerry.forward(size)
        jerry.left(angle)
        jerry.color(color)
