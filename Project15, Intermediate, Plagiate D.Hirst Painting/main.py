# 08.02.2021, Frollo
# Level: Intermediate
# Project: Create a Damien Hirst painting using module turtle

import turtle
import random
turtle.colormode(255) # change the module to use the rgb color code

tim = turtle.Turtle()
tim.speed("fastest")
tim.penup() # remove the lines connecting the dots
tim.hideturtle() # remove the turtle


## extract the colors of the painting "painting.jpg"
# import colorgram as cg
# rgb_colors = [] # list of tuples
# colors = cg.extract("painting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# copy the output rgb_colors and remove first
# two colors as they are the background of the painting
color_list = [(238, 246, 244), (249, 243, 247), (1, 12, 31), (53, 25, 17),
               (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39),
               (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102),
               (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
               (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207),
               (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147),
               (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]


# draw 10 x 10 dots in a random pattern using the used_colors

# put the cursor at the left, down part of the screen
tim.setheading(255)
tim.forward(325)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1): # in total moved 500
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


#create a screen
screen = turtle.Screen()
screen.exitonclick()