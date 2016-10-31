import turtle

leo = turtle.Turtle(shape="turtle")
screen = turtle.Screen()


R = 255
G = 0
B = 0

screen.bgcolor((255, 255, 255))

for i in range(2000):
  G += 1
  B += 0.5
  R -= 1
  leo.color((R, G, B))
  leo.forward(i)
  leo.right(98)
  turtle.speed(0)
