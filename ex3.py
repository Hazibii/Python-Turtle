'''
Hacker Pals
Python Turtles Tutorial
http://hackerpals.com
'''

import turtle

leo = turtle.Turtle()   # Create Leo

# Loop 4 times. Everything I want to repeat is
# *indented* by four spaces.
for i in range(4):
    leo.forward(50)
    leo.right(90)

# This isn't indented, so we aren't repeating it.
turtle.done()
