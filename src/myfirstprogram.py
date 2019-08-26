import turtle

wn = turtle.Screen()  # create a screen
wn.bgcolor("yellow")  # set the screen background color
y = turtle.Turtle()  # create a turtle object
y.shape("turtle")  # define the shape of the obj
y.speed(3)  # speed of animation (if 0 then maximum speed)
dist = 10
y.up()  # penup, this will avoid the trace formation
for x in range(200):  # for loop for helix
    y.forward(dist)
    y.left(90)
    y.stamp()  # a stamp of the selected shape will be made at this point
    dist += 10

turtle.done()  # required in pycharm for turtle screen formation
