import turtle

wn = turtle.Screen()
wn.bgcolor("beige")


def create_cir(radius, x, y, color):
    circ = turtle.Turtle()
    circ.up()
    circ.speed(0)
    circ.shape("classic")
    circ.goto(x, y)
    for _ in range(36):
        circ.color(color)
        circ.forward(radius)
        circ.stamp()
        circ.forward(-radius)
        circ.left(10)


create_cir(50, 0, 0, "blue")
create_cir(75, 0, 0, "Red")
create_cir(100, 0, 0, "Purple")

turtle.done()
