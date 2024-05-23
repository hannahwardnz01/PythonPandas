from turtle import *

size = int(input("Size: ")) #50 to 100 is recommended

# Set up the turtle window
bgcolor("black")
pensize(2)
color("green")
left(90)
backward(size)
speed(0)
hideturtle()
shape("turtle")

# Recursive function to draw the tree
def tree(i):
    if i < 10:
        return
    else:
        # Draw the trunk
        forward(i)
        color("orange")
        circle(2)
        color("brown")

        # Draw the left branch
        left(30)
        tree(3 * i / 4)

        # Draw the right branch
        right(60)
        tree(3 * i / 4)

        # Return to the trunk
        left(30)
        backward(i)

# Call the tree function with the given size
tree(size)

# Finish drawing
exitonclick()
done()
