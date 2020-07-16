#Rainbow Challenge - www.101computing.net/rainbow-challenge
import turtle

# Por último crea una figura geométrica o forma que utilice alguna de las armonías de colores que vimos en clase con el círculo cromático. 

turtle.speed(100)
colores=[(132, 94, 194), (214, 93, 177), (255, 111, 145), (255, 150, 113), (255, 199, 95), (249, 248, 113)]
for x in range(360):
  turtle.pencolor(colores[x%6])
  turtle.width(x/100)
  turtle.forward(x)
  turtle.right(55)