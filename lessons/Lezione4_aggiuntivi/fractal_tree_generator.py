'''
Module providing a recursive function that draws a 
tree based on length of branch, its angle and the limit of the tree.

# Gioele Amendola
# 01/05/2024

# Create a function that generates a fractal tree using recursion.
# Specify the starting trunk length and branching angle.
# Draw the trunk and then recursively call the function
# to draw two branches at the specified angle, each with a shorter length.
# Repeat the branching process until a desired level of detail is reached.
'''
# Import of turtle module. For graphic represantation
try:
    import turtle
except ModuleNotFoundError:
    print("turtle module not found.")


def fractal_tree(length = 100, angle = 20,limit_length=10):
    '''
    Main function to call. Initialize everything needed for the drawing

    Args:
        length (int, optional): length of branch. Defaults to 100.
        angle (int, optional): angle of branches. Defaults to 20.
        limit_length (int, optional): limit to the tree. Defaults to 10.
    '''
    # Initialization of turtle (pen) and screen
    t = turtle.Turtle()
    my_win = turtle.Screen()

    # Moving pen for optimal position, changing its speed (fastest) and color
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color("green")

    # Calling recursive function with these parameters
    # length: The length of a branch
    # angle: The angle at which the branch starts
    # limit_branch: (length-limit_branch)>0 determins how many branches there are on the tree
    # (ex: length = 20, limit_branch = 5 then there are a maximum of 4 branches [20/5 = 4]) 
    # t: pen
    tree(length, angle, limit_length, t)

    my_win.exitonclick()

def tree(length, angle, limit_length, t):
    '''
    Recursive function that draws branches

    Args:
        length (_type_): length of a branch
        angle (_type_): angle of a branch
        limit_length (_type_): used to calculate length of next branch
        t (_type_): pointer of graphic module Turtle
    '''
    if length > 0:
        # Draws branch of length value
        t.forward(length)
        # Angles pen to the right by angle value
        t.right(angle)
        # Calls itself passing length value minus limit_length
        tree(length-limit_length, angle, limit_length, t)
        # Angles pen so that can draw the other side
        t.left(angle*2)
        # Calls itself again
        tree(length-limit_length, angle, limit_length, t)
        # Recenters pen
        t.right(angle)
        # Goes back so that it can draw other branches
        t.backward(length)

# Test Example:
fractal_tree(150, 25, 15)
