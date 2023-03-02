import turtle
import pandas

FONT = ("Helvetica", 9, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=0.4, height=0.5, startx=200, starty=200)
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

states_cor = pandas.read_csv("50_states.csv")
states = states_cor["state"]
states_list = states.to_list()

cor_x = 0
cor_y = 0
correct_answers = []

while len(correct_answers) < 50:

    state = turtle.Turtle()
    state.penup()
    state.hideturtle()

    if answer_state == "Exit":
        break

    if states.isin([answer_state]).any():
        cor_x = int(states_cor[states_cor.state == answer_state].x)
        cor_y = int(states_cor[states_cor.state == answer_state].y)
        state.goto(cor_x, cor_y)
        state.write(f"{answer_state}", align="center", font=FONT)
        if answer_state not in correct_answers:
            correct_answers.append(answer_state)

    score = len(correct_answers)
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

states_list = states.to_list()
missing_states = states.to_list()
for state in correct_answers:
    missing_states.remove(state)

missing_states_series = pandas.Series(missing_states)
missing_states_series.to_csv("states_to_learn.csv")

missing_state = turtle.Turtle()
missing_state.penup()
missing_state.hideturtle()
missing_state.color("red")
screen.tracer(0)

for state in missing_states:
    cor_x = int(states_cor[states_cor.state == state].x)
    cor_y = int(states_cor[states_cor.state == state].y)
    missing_state.goto(cor_x, cor_y)
    missing_state.write(f"{state}", align="center", font=FONT)

screen.update()

turtle.exitonclick()