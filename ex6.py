'''
Choose a color
http://www.colorpicker.com/

Make sure the hex code is like this

star.pencolor('#ff0000') 

'''

import turtle 

star = turtle.Turtle()

star.pencolor("blue") # Set pen color to Blue

for i in range(50):
    star.forward(50)
    star.left(123) # Let's go counterclockwise this time 

#Start of Big Star    
star.pencolor('red') # Set pen color to Red
for i in range(50):
    star.forward(100)
    star.left(123)
    
turtle.done()
