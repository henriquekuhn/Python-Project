import colorgram
import turtle as turtle_module
import random
import os

def get_color_list():
    # Get the current working directory
    current_directory = os.getcwd()

    # Print the current working directory
    #print("Current Working Directory:", current_directory)
    image_path = current_directory + '\Extract RGB values From Image\hirst_spot_painting.jpg'

    colors = colorgram.extract(image_path, 30)

    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color_tuple = (r, g, b)
        rgb_colors.append(new_color_tuple)

    return rgb_colors

def initial_position():
    rosbiff_the_turtle.home()
    rosbiff_the_turtle.setheading(140)
    rosbiff_the_turtle.forward(400)
    rosbiff_the_turtle.setheading(360)

def start_draw(square_size, dot_step, rgb_list):

    for _ in range(square_size):
        for _ in range(square_size):
            rosbiff_the_turtle.dot(15, random.choice(rgb_list))
            rosbiff_the_turtle.forward(dot_step)
            #rosbiff_the_turtle.setheading(270)
        rosbiff_the_turtle.right(90)
        rosbiff_the_turtle.forward(dot_step)
        rosbiff_the_turtle.right(90)
        rosbiff_the_turtle.forward(square_size*dot_step)
        rosbiff_the_turtle.right(180)

    rosbiff_the_turtle.hideturtle()

rosbiff_the_turtle = turtle_module.Turtle()
turtle_module.colormode(255)
rosbiff_the_turtle.shape("turtle")
rosbiff_the_turtle.penup()
rosbiff_the_turtle.speed("fastest")
rgb_list = get_color_list()
initial_position()
start_draw(20, 25, rgb_list)



screen = turtle_module.Screen()
screen.exitonclick()

