from turtle import *
def draw_polygon(sides,size):
    hideturtle()
    speed(10)
    for x in range(0,int(sides)):
        forward(int(size))
        right(360 / int(sides))
