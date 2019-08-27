import turtle
wn= turtle.Screen()
wn.bgcolor("pink")

circ=turtle.Turtle()

circ.up()
circ.shape("classic")
circ.speed(0)
circ.goto(-50,0)
for _ in range (36):
    circ.color("#CD5C5C")
    circ.stamp()
    circ.forward(50)  
    circ.left(10)
    circ.forward(-50)
    
circ.goto(-75,0)
for _ in range (36):
    circ.color("blue")
    circ.stamp()
    circ.forward(75)  
    circ.left(10)
    circ.forward(-75)
    

    
    
turtle.done()