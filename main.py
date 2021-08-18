import turtle
import pandas

screen = turtle.Screen()

screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess 50 states of america", prompt="Guess another state")
    answer_state = answer_state.capitalize()
    t = turtle.Turtle()
    if answer_state in states_list:
        guessed_state = data[data["state"] == answer_state]
        x_state = guessed_state["x"].item()
        y_state = guessed_state["y"].item()
        position = (x_state, y_state)
        t.penup()
        t.hideturtle()
        t.goto(position)
        t.pendown()
        t.write(guessed_state.state.item(), False, "center")

screen.mainloop()
