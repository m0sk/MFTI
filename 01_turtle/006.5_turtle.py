#!C:\UDISK\ProgramFiles\python\3.6.2\python.exe

'''
   Turtle
import turtle

forward(X)  - X pixels forward
backward(X) - X pixels backward
left(X)     - turn left on X degree
rigth(X)    - turn rigth on X degree
penup()     - do not leave a trail
pendown()   - leave a trail
shape(X)    - change turtle icon ("arrow", "turtle", "circle", "square", "triangle", "classic")
stamp()     - draw copy of turtle here
color()     - color set up
begin_fil() - exec befor drawing figure, which need to fill down
end_fill()  - exec after drawing figure
width()     - set up line width
goto(x,y)   - goto (x,y) point

'''

'''
    draw square in square (10)
'''

import turtle

turtle.shape('turtle')

'''
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
'''

facets = 4
facetl = 10
x = 0
y = 0


for a in range(10):
    # don't draw -> goto point -> draw
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
    # draw square
    for i in range(facets):
        turtle.forward(facetl)
        turtle.left(360/facets)

    facetl+=10
    x -= 5
    y -= 5


input()
