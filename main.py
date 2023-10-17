from turtle import Turtle, Screen

tom = Turtle(shape="turtle")
tina = Turtle(shape="turtle")
terry = Turtle(shape="turtle")
tyler = Turtle(shape="turtle")
tiara = Turtle(shape="turtle")
tammy = Turtle(shape="turtle")

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = [tom, tina, terry, tyler, tiara, tammy]
curr_index = 0

for color in colors:
    turtles[curr_index].color(color)
    curr_index += 1

y_cord = -125
x_cord = -225

user_choice = screen.textinput(title="Choose a turtle", prompt="Which turtle will win the race? Enter a color: ")
print(user_choice)

for turtle in turtles:
    turtle.penup()
    turtle.goto(x=x_cord, y=y_cord)
    y_cord += 50


screen.exitonclick()
