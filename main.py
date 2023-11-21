'''
Fisher D. - 100
Fedyakin D. - 100
Popov I. - 100
'''

import turtle

turtle.speed(0)


def draw_hexagon(side_len, color):
    """
    The function draws a hexagon.

    :param side_len: hexagon edge length
    :param color: hexagon fill color
    :return: None
    """

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


def get_color_choice(color_in):
    """
    The function converts the name of the color from Russian into the necessary ones for the turtle.
    Color list: красный, синий, зеленый, желтый, оранжевый, пурпурный, розовый.
    The register does not matter.

    :param color_in: color in russian
    :return: color for turtle
    """

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

    return None


def side_len(n):
    """
    The function calculates the length of an edge of a hexagon.

    :param n: number of hexagons
    :return: the length of an edge of a hexagon
    """
    d = 500 // n
    return d / (3 ** 0.5)


def main():
    numbers = int(input('Type in the number of hexagons: '))

    color_1 = None
    color_2 = None
    while None in [color_1, color_2]:
        color_1 = input('Type in the first color: ')
        color_2 = input('Type in the second color: ')

        color_1 = get_color_choice(color_1)
        color_2 = get_color_choice(color_2)

    step = 500 // numbers

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
            turtle.goto(x + step, y)

        if i % 2 != 0:
            turtle.goto(0, y - s - (step / (2 * 3 ** 0.5)))
        else:
            turtle.goto(-(step / 2), y - s - (step / (2 * 3 ** 0.5)))

    turtle.done()


if __name__ == '__main__':
    main()
