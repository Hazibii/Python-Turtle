'''
Hacker Pals
Python Turtles Tutorial
http://hackerpals.com
'''


import turtle

smiles = turtle.Turtle()
smiles.penup()
smiles.goto(-75,150)
smiles.pendown()
smiles.circle(10)     #Draw eye one

smiles.penup()
smiles.goto(75,150)
smiles.pendown()
smiles.circle(10)     #Draw eye two


smiles.penup()
smiles.goto(-90,70)
smiles.pendown()
smiles.setheading(290) #set heading to go south
smiles.circle(100,140)

turtle.done() #Finish
