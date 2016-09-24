'''
Hacker Pals
Python Turtles Tutorial
http://hackerpals.com
'''

import turtle

leo = turtle.Turtle()

dot_distance = 25
width = 5
height = 7

leo.penup()

for y in range(height):
    for x in range(width):
        leo.dot()
        leo.forward(dot_distance)
    leo.backward(dot_distance * width)
    leo.right(90)
    leo.forward(dot_distance)
    leo.left(90)

turtle.done()
