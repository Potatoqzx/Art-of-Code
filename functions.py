import turtle
from random import*
turtle.colormode(255)
jerry=turtle.Turtle()
'''
jerry.speed(0)
'''
def polygon(size, sides, c):
    for times in range(sides):
        jerry.color(c)
        angle=360/sides
        jerry.forward(size)
        jerry.left(angle)
def comet(size,angle,length,c):
    jerry.color(c)
    for times in range(length):
        jerry.forward(size)
        jerry.left(angle)
        jerry.width(times)
def jump(x,y):
    jerry.penup()
    jerry.goto(x,y)
    jerry.pendown()

def stairs(distance, amount):
    for times in range(amount):
        jerry.forward(distance)
        jerry.left(90)
        jerry.forward(distance)
        jerry.left(90)
        jerry.forward(distance)
def supersquare(square,circle):
    for times in range(4):
        jerry.forward(square)
        jerry.circle(circle)
        jerry.right(90)
def tree(x,y):
    jump(x,y)
    polygon(3,100,"green")
    jerry.forward(40)
    jerry.right(90)
    polygon(4,25,"brown")
    jerry.left(90)


def blueflower(x,y):
    jump(x,y)
    jerry.color("green")
    jerry.width(5)
    jerry.left(90)
    jerry.forward(10)
    jerry.right(90)
    jerry.color("blue")
    jerry.begin_fill()
    jerry.circle(12)
    jerry.end_fill()

def yellowflower(x,y):
    jump(x,y)
    jerry.color("green")
    jerry.width(5)
    jerry.left(90)
    jerry.forward(10)
    jerry.right(25)
    jerry.begin_fill()
    polygon(12,3,"yellow")
    jerry.end_fill()
    jerry.right(65)
def redflower(x,y):
    jump(x,y)
    jerry.color("green")
    jerry.width(5)
    jerry.left(90)
    jerry.forward(10)
    for times in range(3):
        jerry.right(25)
        jerry.begin_fill()
        polygon(12,4,"red")
        jerry.end_fill()
    jerry.right(15)
def flower_field(x,y,x2,y2,x3,y3):
    blueflower(x,y)
    yellowflower(x2,y2)
    redflower(x3,y3)
def wierdshape(size):
    for times in range(10):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        c=(r,g,b)
        comet(size,10,10,c)
        stairs(size*10,1)
        comet(10,10,10,c)
        stairs(50,1)
def idk(length,apart):
    for times in range(length):
        jerry.forward(times*apart)
        wierdshape()
        jerry.left(70)
def spiral(length,apart):
    for times in range(length):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        jerry.color(r,g,b)
        jerry.begin_fill()
        jerry.circle(20)
        jerry.end_fill()
        jerry.penup()
        jerry.forward(times*apart)
        jerry.left(75)
        jerry.pendown()
def spiral2(length,apart):
    for times in range(length):
        r=randint(150,255)
        g=randint(150,255)
        b=randint(150,255)
        c=(r,g,b)
        comet(1.52,5,25,c)
        jerry.penup()
        jerry.forward(times*apart)
        jerry.left(65)
        jerry.pendown()
def spiral3(length,apart):
    for times in range(length):
        r=randint(150,255)
        g=randint(150,255)
        b=randint(150,255)
        c=(r,g,b)
        jerry.begin_fill()
        polygon(30,3,c)
        jerry.end_fill()
        jerry.penup()
        jerry.forward(times*apart)
        jerry.left(95)
        jerry.pendown()
