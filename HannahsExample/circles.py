import random
from turtle import *

colormode(255)

# Create turtle for drawing the wheel
width(2)
speed(0.5)
hideturtle()


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
        
        rt(12 * n)
        circle(100) 
        color(random_color())
        n = n + 1

    width(50)
    up()
    goto(-100, -350)
    write("Random color circle", font=("Arial", 30)) 


draw()
exitonclick()
