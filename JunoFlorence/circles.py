import random
from turtle import *

colormode(255)

# Create turtle for drawing the wheel
width(1)

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
    while(n < 100): 
        
        rt(10.8)
        circle(1665) 
        color(122, 189, 255)
        n = n + 1

    up(12)
    goto(-100, -350)
    write("cha cha!", font=("classic", 30)) 



draw()
exitonclick()
