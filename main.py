# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

import turtle as turtle_module
import random

screen = turtle_module.Screen()
screen.setup(width=600, height=600)

turtle_module.colormode(255)
tom = turtle_module.Turtle()
tom.speed("fastest")
tom.penup()
tom.hideturtle()

color_list = [(232, 52, 111), (230, 227, 81),
              (237, 220, 2), (17, 112, 177), (6, 196, 119),
              (232, 120, 171), (147, 64, 112), (225, 148, 54),
              (176, 194, 6), (221, 163, 216), (5, 175, 226),
              (242, 83, 32), (100, 199, 154), (108, 174, 204),
              (6, 53, 182), (9, 138, 95), (127, 222, 209), (219, 60, 18),
              (2, 93, 101), (240, 171, 162), (62, 25, 55)]


tom.setheading(225)
tom.forward(250)
tom.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)


screen.exitonclick()
