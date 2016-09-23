'''
Hacker Pals
Python Turtles Tutorial
http://hackerpals.com
'''

import turtle

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()
