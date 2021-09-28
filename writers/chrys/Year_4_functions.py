import random
from num2words import num2words
from math import cos, sin, radians


def time_unit_converter(unit_in, unit_out, number):
    """how many unit_in in number unit_out, e.g. how many weeks in a month"""
    if unit_out in ['Months', 'months', 'month', 'Month'] and \
            unit_in in ['year', 'years', 'Year', 'Years']:
        return [number * 12, ' months']

    elif unit_out in ['Weeks', 'weeks', 'week', 'Week']:
        if unit_in in ['year', 'years', 'Year', 'Years']:
            return [number * 52, 'weeks']
        elif unit_in in ['Months', 'months', 'month', 'Month']:
            return [number * 4, ' weeks']

    elif unit_out in ['Days', 'days', 'day', 'Day']:
        if unit_in in ['year', 'years', 'Year', 'Years']:
            return [number * 365, ' days']
        elif unit_in in ['Months', 'months', 'month', 'Month']:
            return [number * 7 * 4, ' days']
        elif unit_in in ['Weeks', 'weeks', 'week', 'Week']:
            return [number * 7, ' days']

    elif unit_out in ['Hours', 'hours', 'hour', 'Hour']:
        if unit_in in ['Days', 'days', 'day', 'Day']:
            return [number * 24, ' hours']
        elif unit_in in ['Weeks', 'weeks', 'week', 'Week']:
            return [number * 24 * 7, ' hours']
        elif unit_in in ['Months', 'months', 'month', 'Month']:
            return [number * 24 * 7 * 4, ' hours']

    elif unit_out in ['Minutes', 'minutes', 'minute', 'Minute']:
        if unit_in in ['Hours', 'hours', 'hour', 'Hour']:
            return [number * 60, ' minutes']
        elif unit_out in unit_in in ['Days', 'days', 'day', 'Day']:
            return [number * 60 * 24, ' minutes']
        elif unit_in in ['Weeks', 'weeks', 'week', 'Week']:
            return [number * 60 * 24 * 7, ' minutes']
        elif unit_in in ['Months', 'months', 'month', 'Month']:
            return [number * 60 * 24 * 7 * 4, ' minutes']

    elif unit_out in ['Seconds', 'seconds', 'second', 'Second']:
        if unit_in in ['Minutes', 'minutes', 'minute', 'Minute']:
            return [number * 60, ' seconds']
        elif unit_in in ['Hours', 'hours', 'hour', 'Hour']:
            return [number * 60 * 60, ' seconds']
        elif unit_in in ['Days', 'days', 'day', 'Day']:
            return [number * 60 * 60 * 24, ' seconds']
        elif unit_in in ['Weeks', 'weeks', 'week', 'Week']:
            return [number * 60 * 60 * 24 * 7, ' seconds']


def time_to_words(hour_in, minute_in):
    if hour_in % 12 == 0:
        hour_out = 'twelve'
    else:
        hour_out = num2words(hour_in % 12)

    if 0 < minute_in <= 30:
        prefix = ' past '
        if minute_in == 30:
            minute_out = 'half'
        elif minute_in == 15:
            minute_out = 'quarter'
        else:
            minute_out = num2words(minute_in)
    elif minute_in == 0:
        prefix = " o'clock "
    else:
        prefix = ' to '
        if (hour_in + 1) % 12 == 0:
            hour_out = 'twelve'
        else:
            hour_out = num2words((hour_in + 1) % 12)
        if minute_in == 45:
            minute_out = 'quarter'
        else:
            minute_out = num2words(60 - minute_in)

    if minute_in == 0:
        return hour_out + prefix
    else:
        return minute_out + prefix + hour_out


def analogue_clock(hour, minute):
    hour_angle = (90 - 30 * (hour % 12)) % 360 - 0.5 * minute
    minute_angle = (90 - 6 * minute) % 360
    return "\\begin{tikzpicture}[line cap=rect,line width=3pt]\n" \
           "\\filldraw [fill=white] (0,0) circle [radius=1.3cm];\n" \
           " \\foreach \\angle [count=\\xi] in {60,30,...,-270}\n" \
           "{\n  \\draw[line width=1pt] " \
           "(\\angle:1.15cm) -- (\\angle:1.3cm);\n" \
           "\\node[font=\\large] at (\\angle:0.9cm) {\\textsf{\\xi}};\n}\n" \
           "\\foreach \\angle in {0,90,180,270}\n  " \
           "\\draw[line width=1.5pt] (\\angle:1.1cm) -- (\\angle:1.3cm);\n" \
           f"\\draw (0,0) -- ({hour_angle}:0.65cm);\n" \
           f"\\draw (0,0) -- ({minute_angle}:0.9cm);\n" \
           "\\end{tikzpicture}"


def num_line(denominator, labelled, additional="", length=6):
    n = denominator
    if n > 9:
        font = "\\large"
    else:
        font = "\\Large"

    if labelled is True:
        height = 3
    else:
        height = 5

    model = f"\\begin{{tikzpicture}}[font={font}]" \
            f"\\draw[line width = 1pt] (0,0) -- ({length},0); " \
            f"\\foreach \\x in {{0,{length}}} " \
            "\\draw[shift={\\x,0},color=black, line width = 1pt] " \
            f"(0pt,{height + 1}pt) -- (0pt,-{height + 1}pt);" \
            f"\\foreach \\x in {{1,...,{n-1}}}" \
            f"\\draw[shift={{(\\x * {length}/{n},0)}},color=black] " \
            f"(0pt,{height}pt) -- (0pt,-{height}pt) node[below] "

    if labelled is True:
        model += f"{{$\\frac{{\\x}}{{{n}}}$}};"
    else:
        model += ";"
    model += "\\draw (0,-3pt) node[below]{$0$};" \
             f"\\draw ({length},-3pt) node[below]{{$1$}};" \
             "\\draw[line width = 1pt, color=black] " \
             f"({length},{height+1}pt) -- ({length},-{height+1}pt);"
    model += additional + "\\end{tikzpicture}"
    return model


def angle(angle, radius, rotation=0):
    angle = 90
    rotation = 270
    radius = 4

    x_0 = cos(radians(rotation)) * radius
    y_0 = sin(radians(rotation)) * radius
    if x_0 <=0 and y_0 <= 0:
        theta = 180 + angle
    elif x_0 < 0 and y_0 >= 0:
        theta = 90 + angle
    elif x_0 >= 0 and y_0 < 0:
        theta = 270 + angle
    else:
        theta = angle
    x = cos(radians(theta + rotation)) * radius
    y = sin(radians(theta + rotation)) * radius

    model = "\\usetikzlibrary{angles,quotes}" \
            " \\begin{tikzpicture}[> = stealth]" \
            f"\\coordinate (a) at (0,0); " \
            f"\\coordinate (b) at ({x},{y}); " \
            f"\\coordinate (c) at ({x_0},{y_0});" \
            "\\draw pic[draw,fill=blue,angle radius=1cm] {angle=c--a--b};" \
            "\\draw[ultra thick,black, ->]  (a) -- node[above] {} (b);" \
            "\\draw[ultra thick,black,->]  (a) -- node[above right] {} (c);" \
            "\\end{tikzpicture}"
    return model
