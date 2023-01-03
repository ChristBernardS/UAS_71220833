import turtle

p = turtle.Turtle()
s = turtle.Screen()

turtle.speed(0)

p.pensize(3)
s.bgcolor('Pink')
p.penup()

p.goto(-100, 0)
p.pencolor('Yellow')
p.pendown()

# kotak kuning
p.begin_fill()
p.goto(100, 0)
p.goto(120, 40)
p.goto(120, 220)
p.goto(100, 260)
p.goto(-100, 260)
p.goto(-120, 220)
p.goto(-120, 40)
p.goto(-100, 0)
p.fillcolor('Yellow')
p.end_fill()

p.penup()
p.goto(0, 0)
p.pencolor('Brown')

# kotak coklat
p.begin_fill()
p.goto(0, -50)
p.goto(10, -50)
p.goto(10, 0)
p.goto(0, 0)
p.fillcolor('Brown')
p.end_fill()

p.penup()
p.goto(-30, 20)
p.pendown()
p.pencolor('Red')

# HI!
# H
p.goto(-30, 60)
p.goto(-30, 40)
p.goto(-15, 40)
p.goto(-15, 60)
p.goto(-15, 20)

p.penup()
p.goto(-10, 20)
p.pendown()

# I
p.goto(0, 20)
p.goto(-5, 20)
p.goto(-5, 60)
p.goto(-10, 60)
p.goto(0, 60)

p.penup()
p.goto(20, 20)
p.pendown()

#!
p.dot(4)
p.penup()
p.goto(20, 25)
p.pendown()
p.goto(20, 60)

p.penup()
p.goto(0, 100)
p.pendown()
p.pencolor('Blue')

# Lingkaran
p.circle(60)

p.penup()
p.goto(-25, 120)
p.pencolor('Red')
p.pendown()

# Gambar
for i in range(10):
    p.forward(50)
    p.left(108)

p.hideturtle()
turtle.done()
