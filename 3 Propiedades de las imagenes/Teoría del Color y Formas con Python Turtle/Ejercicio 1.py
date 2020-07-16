from turtle import *
import turtle
# Realizar una o varias figuras geométricas o formas que utilicen los colores primarios.
colors = ['red', 'red', 'blue', 'blue', 'green', 'green']
circle_size = 40
for i in range(6):
  turtle.color(colors[i])
  circle(circle_size)
  left(60)

turtle.penup()  
turtle.goto(35,20)
turtle.pendown()

colors2= ['cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow']
for i in range(6):
  turtle.color(colors[i])
  circle(circle_size)
  left(60)

turtle.penup()
turtle.goto(-35,20)
turtle.pendown()

for i in range(6):
  turtle.color(colors[i])
  circle(circle_size)
  left(60)

turtle.penup()
turtle.goto(-35,-20)
turtle.pendown()  

for i in range(6):
  turtle.color(colors[i])
  circle(circle_size)
  left(60)
 
turtle.penup()
turtle.goto(35,-20)
turtle.pendown()

for i in range(6):
  turtle.color(colors[i])
  circle(circle_size)
  left(60)