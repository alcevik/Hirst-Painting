import turtle
from turtle import Screen
import random

tim = turtle.Turtle()
turtle.colormode(255)
color_list = [(131, 165, 204), (221, 149, 109), (30, 41, 62), (201, 134, 146), (166, 58, 48), (141, 184, 161), (41, 104, 154), (236, 213, 94), (150, 59, 66), (215, 82, 71), (236, 165, 157), (51, 112, 91), (33, 60, 55), (171, 29, 33), (156, 33, 30), (52, 44, 49), (229, 162, 166), (170, 188, 221), (17, 96, 70), (57, 51, 48), (186, 101, 111), (30, 60, 110), (107, 126, 159), (174, 200, 188), (34, 151, 210), (65, 66, 57)]
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.right(225)
tim.speed('fastest')


for x in range(10):
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)

screen = Screen()
screen.exitonclick()
