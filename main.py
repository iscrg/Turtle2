import turtle

turtle.speed(0)


def draw_hexagon(side_len, color):
    turtle.pu()
    turtle.rt(90)
    turtle.pd()
    turtle.color('black', color)
    turtle.begin_fill()
    for i in range(6):
        turtle.fd(side_len)
        turtle.lt(60)

    turtle.end_fill()
    turtle.pu()
    turtle.lt(90)


def get_color_choice():
    color_in = input()
    if color_in.lower() == 'красный':
        color_out = 'red'
    elif color_in.lower() == 'синий':
        color_out = 'blue'
    elif color_in.lower() == 'зеленый':
        color_out = 'green'
    elif color_in.lower() == 'желтый':
        color_out = 'yellow'
    elif color_in.lower() == 'оранжевый':
        color_out = 'orange'
    elif color_in.lower() == 'пурпурный':
        color_out = 'purple'
    elif color_in.lower() == 'розовый':
        color_out = 'pink'

    return color_out


def side_len(n):
    d = 500 // n
    return d / (3 ** 0.5)


n = int(input())
color = get_color_choice()

for i in range(n):
    s = side_len(n)
    for _ in range(n):
        draw_hexagon(s, color)
        x = turtle.xcor()
        y = turtle.ycor()
        turtle.goto(x + 500 // n, y)

    y = turtle.ycor()
    if i % 2 != 0:
        turtle.goto(0, y - s - (500 // n / (2 * 3 ** 0.5)))
    else:
        turtle.goto(-((500 // n) / 2), y - s - (500 // n / (2 * 3 ** 0.5)))

turtle.done()
