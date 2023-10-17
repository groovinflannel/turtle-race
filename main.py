from turtle import Turtle, Screen
import random

tom = Turtle(shape="turtle")
tina = Turtle(shape="turtle")
terry = Turtle(shape="turtle")
tyler = Turtle(shape="turtle")
tiara = Turtle(shape="turtle")
tammy = Turtle(shape="turtle")

screen = Screen()
screen.setup(width=500, height=400)
is_race_ready = False

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

if user_choice:
    is_race_ready = True

while is_race_ready:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_ready = False
            winner_color = turtle.pencolor()
            if winner_color == user_choice:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winner_color} turtle won.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
