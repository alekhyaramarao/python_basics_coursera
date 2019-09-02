import turtle

wn = turtle.Screen()
wn.bgcolor("beige")


colors = ['violet', 'blueViolet', 'purple', 'blue', 'green', 'yellow', 'orange', 'red', 'darkred', 'violet',
        'blueviolet', 'purple', 'blue', 'green', 'yellow', 'orange', 'red', 'darkred', 'violet', 'blueviolet',
       'purple', 'blue', 'green', 'yellow', 'orange', 'red', 'darkred', 'violet', 'blueviolet', 'purple', 'blue',
      'green', 'yellow', 'orange', 'red', 'darkred']



def create_cir(radius, x, y):
    circ = turtle.Turtle()
    circ.up()
    circ.speed(0)
    circ.shape("circle")
    circ.goto(x, y)
    for color in colors:
        circ.color(color)
        circ.forward(radius)
        circ.stamp()
        circ.forward(-radius)
        circ.left(10)


create_cir(50, 0, 0)
create_cir(75, 0, 0)
create_cir(100, 0, 0)

turtle.done()
