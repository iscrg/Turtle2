'''
Fisher D. - 48%
Fedyakin D. - 55%
Popov I. - 40%
'''

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


def get_color_choice(color_num):
    if color_num == 1:
        num = 'first'
    else:
        num = 'second'

    color_in = input(f'Type in the {num} color: ')
    color_in = color_in.lower()

    if color_in == 'красный':
        return 'red'
    if color_in == 'синий':
        return 'blue'
    if color_in == 'зеленый':
        return 'green'
    if color_in == 'желтый':
        return 'yellow'
    if color_in == 'оранжевый':
        return 'orange'
    if color_in == 'пурпурный':
        return 'purple'
    if color_in == 'розовый':
        return 'pink'

    print('Incorrect color!')
    return get_color_choice(color_num)


def side_len(n):
    d = 500 // n
    return d / (3 ** 0.5)


def main():
    numbers = int(input('Type in the number of hexagons: '))
    color_1 = get_color_choice(1)
    color_2 = get_color_choice(2)

    for i in range(numbers):
        s = side_len(numbers)
        for j in range(numbers):
            if i % 4 in [0, 1]:
                if j % 2 == 0:
                    color = color_1
                else:
                    color = color_2
            else:
                if j % 2 == 0:
                    color = color_2
                else:
                    color = color_1

            draw_hexagon(s, color)
            x = turtle.xcor()
            y = turtle.ycor()
            turtle.goto(x + 500 // numbers, y)

        y = turtle.ycor()
        if i % 2 != 0:
            turtle.goto(0, y - s - (500 // numbers / (2 * 3 ** 0.5)))
        else:
            turtle.goto(-((500 // numbers) / 2), y - s - (500 // numbers / (2 * 3 ** 0.5)))

    turtle.done()


if __name__ == '__main__':
    main()
