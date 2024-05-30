import random
from turtle import *

#colormode(255)

# Create turtle for drawing the wheel
width(2)
speed(0)
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
        
        rt(7 * n)
        circle(300) 
        if(n%3):
            color("blue")
        elif(n%2):
            color("red")
        else:
            color("green")
        n = n + 1


draw()
exitonclick()
