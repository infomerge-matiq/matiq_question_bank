"""
MIT License

Copyright (c) 2021 Ali Sever

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from random import shuffle
from string import ascii_uppercase
from num2words import num2words


def multiple_choice(question: str, choices: list[str], correct: str,
                    onepar=True, reorder=True):
    """Takes question, choices(which contains answer), answer and returns
    a multiple choice question and the answer"""
    layout = ""
    if onepar:
        layout = "onepar"
    choices_list = []
    if reorder:
        shuffle(choices)
    letter = ascii_uppercase[choices.index(correct)]
    for choice in choices:
        choices_list.append(f"\\choice {choice}\n")
    full_question = "".join(
        [question, f"\n\n\\begin{{{layout}choices}}\n"] +
        choices_list + [f"\\end{{{layout}choices}}"])
    return [full_question, f"{letter}. {correct}"]


def dollar(x):
    return "$" + str(x) + "$"


def ordinal(n):
    return "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1)
                                   * (n % 10 < 4) * n % 10::4])


def is_prime(n: int):
    if n <= 1:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


def nth_prime(n):
    num = 1
    for _ in range(n):
        num = num + 1
        while not is_prime(num):
            num = num + 1
    return num


def factors(n):
    my_list = []
    for i in range(1, n + 1):
        if not n % i:
            my_list.append(i)
    return my_list


def prime_factors(n):
    return [x for x in factors(n) if is_prime(x)]


def gcd(m: int, n: int, *args: int):
    if args:
        return gcd(*(gcd(m, n),) + args)
    m, n = abs(m), abs(n)
    if m < n:
        (m, n) = (n, m)
    if n == 0:
        return m
    if (m % n) == 0:
        return n
    else:
        return gcd(n, m % n)


def frac_simplify(a, b):
    return a // gcd(a, b), b // gcd(a, b)


def latex_frac(a, b):
    return f"\\frac{{{a}}}{{{b}}}"


def latex_frac_simplify(a, b):
    return latex_frac(*frac_simplify(a, b))


def fraction_addition(a, b, c, d):
    numerator = a * d + b * c
    denominator = b * d
    return frac_simplify(numerator, denominator)


def fraction_subtraction(a, b, c, d):
    numerator = a * d - b * c
    denominator = b * d
    return frac_simplify(numerator, denominator)


def valid_metric(unit):
    prefixes = ["m", "c", "d", "", "da", "h", "k"]
    base_units = ["m", "g", "l"]
    return all([unit[-1] in base_units, unit[0:-1] in prefixes])


def convert_measurement(number, unit_in, unit_out):
    prefixes = {"m": 0.001, "c": 0.01, "d": 0.1, "": 1, "da": 10,
                "h": 100, "k": 1000}
    for unit in [unit_in, unit_out]:
        if not valid_metric(unit):
            raise NameError(f"{unit} is not a valid unit.")
    if unit_in[-1] != unit_out[-1]:
        raise TypeError("Units are not of the same type.")
    else:
        return number * prefixes[unit_in[0:-1]] / prefixes[unit_out[0:-1]]


def convert_imperial(unit_in, unit_out, number=1):
    if unit_in in ["inch", "inches"]:
        return convert_measurement(number * 2.5, "cm", unit_out)
    elif unit_in in ["lb", "lbs", "pounds"]:
        return convert_measurement(number / 2.2, "kg", unit_out)
    elif unit_in in ["pint", "pints"]:
        return convert_measurement(number * 568, "ml", unit_out)
    elif unit_in in ["mile", "miles"]:
        return convert_measurement(number * 1.6, "km", unit_out)
    elif unit_out in ["inch", "inches"]:
        return convert_measurement(number / 2.5, unit_in, "cm")
    elif unit_out in ["lb", "lbs", "pounds"]:
        return convert_measurement(number * 2.2, unit_in, "kg")
    elif unit_out in ["pint", "pints"]:
        return convert_measurement(number / 568, unit_in, "ml")
    elif unit_out in ["mile", "miles"]:
        return convert_measurement(number / 1.6, unit_in, "km")
    else:
        raise NameError("Given units are invalid.")


def time_unit_converter(unit_in, unit_out, number):
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
        elif unit_in in ['Days', 'days', 'day', 'Day']:
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
        return hour_out + " o'clock"
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
    return minute_out + prefix + hour_out


def analogue_clock(hour, minute):
    hour_angle = (90 - 30 * (hour % 12)) % 360 - 0.5 * minute
    minute_angle = (90 - 6 * minute) % 360
    clock = r'''
    \begin{center}
    \begin{tikzpicture}[line cap=rect, line width=3pt]
    \filldraw [fill=white] (0,0) circle [radius=1.3cm];
    \foreach \angle [count=\xi] in {60,30,...,-270}
      {
        \draw[line width=1pt] (\angle:1.15cm) -- (\angle:1.3cm);
        \node[font=\large] at (\angle:0.9cm) {\textsf{\xi}};
      }
    \foreach \angle in {0,90,180,270}
    \draw[line width=1.5pt] (\angle:1.1cm) -- (\angle:1.3cm);
    \draw (0,0) -- (%f:0.65cm);
    \draw (0,0) -- (%f:0.9cm);
    \end{tikzpicture}
    \end{center}
    ''' % (hour_angle, minute_angle)
    return clock


def num_line(denominator, additional="", length=6, labelled=False):
    if labelled:
        label = r' node[below] {$\frac{\x}{%d}$}' % denominator
    else:
        label = ''
    model = r'''
    \begin{tikzpicture}[font=\Large]
      \draw[line width = 1pt] (0,0) -- (%f,0);
      \foreach \x in {0,%f}
        {\draw [shift={(\x, 0)}, color=black, line width = 1pt] 
        (0pt,6pt) -- (0pt,-6pt);}
      \foreach \x in {1,...,%d} 
        {\draw [shift={(\x * %f/%d,0)}, color=black] 
          (0pt,5pt) -- (0pt,-5pt) %s;}
      \draw (0, -6pt) node[below]{0};
      \draw (%f, -6pt) node[below]{1};
    %s
    \end{tikzpicture}
    ''' % (length, length, denominator - 1, length, denominator, label, length,
           additional)

    return model


def angle_drawing(x_angle, y_angle=0, radius=4, shaded_radius=1):
    model = r'''
      \begin{tikzpicture}
      \draw
      (%f:%fcm) coordinate (a)
      -- (0:0) coordinate (b)
      -- (%f:%fcm) coordinate (c)
      pic[draw=blue!50!black, fill=blue!20, angle eccentricity=1.2, 
          angle radius=%fcm]
      {angle=c--b--a};
      \end{tikzpicture}
    ''' % (x_angle, radius, y_angle, radius, shaded_radius)
    return model
