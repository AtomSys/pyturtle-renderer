from turtle import *
def draw_polygon(sides,size):
    hideturtle()
    speed(10)
    for x in range(0,int(sides)):
        forward(int(size))
        right(360 / int(sides))
def draw_rectangle(s1,s2):
    for x in range(0,2):
        right(90)
        forward(int(s1))
        right(90)
        forward(int(s2))