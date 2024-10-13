from turtle import *
shape("turtle")


# forward(x)
# exitonclick()
#left(x)

width(6)

color("gray")

left(180)
forward(300)
left(180)
forward(600)

left(90)
forward(200)

color('brown')
begin_fill()


left(45)
forward(150)
left(90)
forward(150)



right(90)
forward(150)
left(90)
forward(150)



right(90)
forward(140)
left(90)
forward(150)

left(135)

forward(630)
end_fill()

penup()
goto(-300,0)
color("gray")
pendown()
begin_fill()

right(180)
forward(30)
right(90)
forward(190)
right(90)
forward(625)
right(90)
forward(190)
right(90)
forward(630)
end_fill()

penup()
goto(-50,0)
pendown()
color("red")
begin_fill()
right(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
right(90)
forward(50)
end_fill()
exitonclick()