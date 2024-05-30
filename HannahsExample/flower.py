from turtle import *

# set background color, speed, and hide the turtle 
bgcolor("black")
speed(0)
hideturtle()

# the colors being used (change them as you wish!)
Colors = ["yellow", "purple", "yellow", "purple"]

# repeat x times times
x = 30
for i in range(x):
    #for each color
    for col in Colors:
        #set pen color to that color 
        color(col)
        circle(200-i, 100)
        lt(90)
        circle(200-i, 100)
        rt(60)

exitonclick()
