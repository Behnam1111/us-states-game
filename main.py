import turtle
import pandas

screen = turtle.Screen()

screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess 50 states of america",
                                    prompt="Guess another state").capitalize()
    t = turtle.Turtle()
    if answer_state == "Exit":
        missed_states = [state for state in states_list if state not in guessed_state]
        miss = pandas.DataFrame(missed_states)
        miss.to_csv("missed_states.csv")
        break
    if answer_state in states_list:
        guessed_state.append(answer_state)
        guess = data[data["state"] == answer_state]
        x_state = guess["x"].item()
        y_state = guess["y"].item()
        position = (x_state, y_state)
        t.penup()
        t.hideturtle()
        t.goto(position)
        t.pendown()
        t.write(guess.state.item(), False, "center")

screen.mainloop()
