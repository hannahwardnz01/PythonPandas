import random
import turtle
import math

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.colormode(255)

# Create turtle for drawing the wheel
pen = turtle.Turtle()
pen.width(2)
pen.speed(0.5)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Function to draw the wheel
def draw():

    # number of circles 
    n = 0   

    # loop for printing tangent circles 
    while(n < 30): 
        pen.seth(12 * n)
        pen.circle(100) 
        pen.color(random_color())
        n = n + 1

    pen.width(50)
    pen.up()
    pen.goto(-100, -350)
    pen.write("Random color circle", font=("Arial", 30)) 


draw()
turtle.exitonclick()
 #math.floor(n*7)