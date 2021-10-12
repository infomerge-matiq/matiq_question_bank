import random
import roman

from datetime import time, datetime, timedelta
from math import floor, ceil
from num2words import num2words
from statistics import mean

from random import shuffle
import names


import matiq as mq


# NUMBER AND PLACE VALUE_______

def pv_1(difficulty):
    """
    Choice of fill in missing or find the next number in a sequence. Chrys
    """
    if difficulty == 1:
        step = random.choice([4 + random.randint(0, 5), 25, 100, 1000])
    else:
        step = random.choice([6, 7, 9, 25, 1000])

    numbers = []
    k = random.randint(3 + difficulty, 5 + difficulty)
    for i in range(1, k):
        numbers.append(mq.dollar(i * step))

    i = random.randint(0, 1)
    if i == 0:
        n = random.randint(0, len(numbers) - 2)
        answer = numbers[n]
        numbers[n] = "\\makebox[1em]{\\hrulefill}"
    else:
        numbers.append("\\fillin[][1em]")
        answer = mq.dollar(step * (k + 1))

    sequence = ",\\ ".join(numbers)
    question = f"Find the {['missing', 'next'][i]} number in the sequence. " \
               f"\n\n {sequence}"
    return [question, answer]


def pv_2(difficulty):
    """
    Choice of 3 questions involving the addition and subtraction of 1000.
    Chrys.
    """
    lower = round(1000/difficulty)
    upper = 8000+1000*difficulty
    x = random.randint(lower, upper)
    if x < 1000:
        x = round(x, -2)

    y = random.choice([[x, 1000, x + 1000, '$+$', 'more'],
                       [x, 1000, x - 1000, '$-$', 'less']
                       ])
    k = random.randint(0, 2)
    if k <= 1:
        answer = mq.dollar(y[2])
        question = random.choice([f"What is {y[0]}{y[3]}{y[1]}?",
                                  f"What number is 1000 {y[4]} than {x}?"
                                  ])
    else:
        n = random.randint(0, 2)
        answer = mq.dollar(y[n])
        y[n] = "$\\square$"
        question = f"Fill in the missing part of this equation: " \
                   f"{y[0]}{y[3]}{y[1]} $=$ {y[2]}"
    return [question, answer]


def pv_3(difficulty):
    """Rounding to nearest power of 10. Chrys."""
    lower = 1000 - 250 * difficulty
    upper = 4000 * difficulty - 3000
    no_start = random.randint(lower, upper)
    no_rnd = random.choice([[10, 'ten'],
                            [100, 'hundred'],
                            [1000, 'thousand']
                            ])
    choice = random.choices([no_rnd[0], no_rnd[1]],
                            weights=(1, difficulty), k=1)

    question = f"Round {no_start} to the nearest {choice[0]}."
    answer = mq.dollar(round(no_start / no_rnd[0]) * no_rnd[0])
    return [question, answer]


def pv_4(difficulty):
    """Identify place of a digit in a given number. Chrys."""
    places = ["Ones place",
              "Tens place",
              "Hundreds place",
              "Thousands place",
              "Ten thousands place"
              ]
    digits = random.sample(range(1, 9), 2+difficulty)
    n = int(''.join(map(str, digits)))
    d = random.randint(1, len(str(n)))
    question = f"What place is the digit {int(str(n)[- d]):g} " \
               f"in the number {mq.dollar(n)}?"
    choices = []
    for i in range(0, len(str(n))):
        choice1 = places[i]
        choices.append(choice1)
    answer = choices[d-1]
    return mq.multiple_choice(question, choices, answer)


def pv_5(difficulty):
    """Identify value of the digit in a given position in a number. Chrys."""
    places = ["ones", "tens", "hundreds", "thousands", "ten thousands"]
    n = random.randint(10 ** (difficulty + 1), 10 ** (difficulty + 2))
    d = random.randint(1 + round(difficulty / 3), len(str(n)))
    question = f"In the number {mq.dollar(n)}, " \
               f"what is the value of the digit in the {places[d-1]} position?"
    answer = mq.dollar({int(str(n)[- d])})
    return [question, answer]


def pv_6(difficulty):
    """Find the nth smallest or largest number in a sequence. Chrys."""
    limit = 3 + difficulty
    k = random.randint(0, 1)
    size = ["smallest", "largest"]

    n = random.randint(1, limit-1)
    if n == 1:
        order = ''
    else:
        order = mq.ordinal(n)

    numbers = random.sample(range(100, difficulty * 5000), limit)
    question = f"Which of these numbers is the {order} {size[k]}?\n\n"
    question += ", ".join([mq.dollar(i) for i in numbers])

    if k == 0:
        numbers.sort()
    else:
        numbers.sort(reverse=True)
    answer = mq.dollar(numbers[n-1])
    return [question, answer]


def pv_7(difficulty):
    """ Use table to find person with largest/smallest score. Chrys."""
    n = random.randint(0, 1)
    size = ['smallest', 'highest']
    col_2 = random.sample(range(100, 1000 + 10 ** (difficulty + 2)), 5)
    c = []
    for i in range(len(col_2)):
        c.append([names.get_first_name(), col_2[i]])

    data = [["\\textbf{Name}", "\\textbf{Score}"]]
    for k in range(5):
        data.append([c[k][0], str(c[k][1])])
    table = mq.draw_table(data)

    question = f"Some friends are playing a game. " \
               f"The table below shows each of their scores.\n\n{table}\n\n " \
               f"Who has the {size[n]} score?"

    choices = []
    if n == 0:
        c.sort(key=lambda x: x[1])
    else:
        c.sort(key=lambda x: x[1], reverse=True)
    answer = c[0][0]
    choices.append(answer)
    for j in range(1, len(c)):
        choices.append(c[j][0])
    return mq.multiple_choice(question, choices, answer)


def pv_8(difficulty):
    """ Use table to find the nth highest/smallest value. Chrys."""
    n = random.randint(0, 1)
    m = random.randint(0, 1)
    size = ['smallest', 'highest'][n]
    values = random.sample(
        range(10 ** (difficulty + 1) - (difficulty - 1) * 200,
              2000 + 10 ** (difficulty + 2)), k=5)
    name = [
        ['Athletics', 'Swimming', 'Badminton', 'Cycling', 'Volleyball'],
        ['Mountain Heights', 'Hilly Green', 'Rivertown',
         'Rocky Beach', 'Cloudy Valley']
    ]
    c = []
    for k in range(len(values)):
        c.append([name[m][k], values[k]])

    i = random.randint(2, len(values) - 2)
    order = mq.ordinal(i)

    choices = []
    title = [['Sport', 'Attendance'], ['Town', 'Population']][m]
    data = [title]
    for j in range(5):
        data.append([c[j][0], str(c[j][1])])
        choices.append(c[j][0])
    table = mq.draw_table(data)

    question = [
        "The table below shows the attendance for some sports events. ",
        f"The table below shows the populations for some towns. "][m]
    question += f"\n\n {table} \n\n"
    question += [f"What sport had the {order} {size} attendance?",
                 f"What town has the {order} {size} population?"][m]

    if n == 0:
        c.sort(key=lambda x: x[1])
    else:
        c.sort(key=lambda x: x[1], reverse=True)
    answer = c[i - 1][0]
    return mq.multiple_choice(question, choices, answer)


def pv_9(difficulty):
    """arranging integers in ascending or descending order. Chrys."""
    lower = 10 - 10*difficulty
    upper = 2 * 10 ** (difficulty+1)
    integers = random.sample(range(lower, upper), 6)
    integers.append(random.randint(lower, 0))
    n = random.randint(0, 1)
    ordered = [sorted(integers), sorted(integers, reverse=True)][n]
    question = f"Arrange the numbers from " \
               f"{['smallest to largest', 'largest to smallest'][n]}.\n\n "
    question += ", ".join([str(i) for i in integers])
    answer = ', '.join([str(j) for j in ordered])
    return [question, answer]


# noinspection PyTypeChecker
def pv_10(difficulty):
    """Pick the sign to complete the inequality. Chrys."""
    lower = 10 ** (difficulty-1)
    upper = 5 * 10 ** difficulty
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    question = "Choose the sign that correctly completes the statement. \n\n" \
               f"\\begin{{center}} {a} $\\square$ {b} \\end{{center}}"
    choices = ["$<$", "$=$", "$>$"]
    if a > b:
        answer = choices[2]
    elif a < b:
        answer = choices[0]
    else:
        answer = choices[1]
    return mq.multiple_choice(question, choices, answer)


def pv_11(difficulty):
    """Inequalities which include addition and subtraction. Chrys."""
    upper = 2**(3+difficulty)
    numbers = random.sample(range(2, upper), 4)
    no_3 = random.randint(0, numbers[0])

    question = "Choose the sign that correctly completes the statement. \n\n" \
               + r''' 
               \begin{center} 
               %d $+$ %d $-$ %d $\square$ %d $+$ %d 
               \end{center} 
               ''' % (numbers[0], numbers[1], no_3, numbers[2], numbers[3])

    choices = ["$<$", "$=$", "$>$"]
    x = numbers[0] + numbers[1] - no_3
    y = numbers[2] + numbers[3]
    if x > y:
        answer = choices[2]
    elif x < y:
        answer = choices[0]
    else:
        answer = choices[1]
    return mq.multiple_choice(question, choices, answer)


def pv_12(difficulty):
    """Roman Numerals to number and vice versa. Chrys."""
    n = random.randint(1, difficulty * 100)
    k = random.randint(0, 1)
    question = [f"What is {n} in Roman numerals?",
                f"What is the value of {roman.toRoman(n)}?"][k]
    answer = [roman.toRoman(n), mq.dollar(n)][k]
    return [question, answer]


def pv_13(difficulty):
    """
    Inequalities where student fills missing num to make statement true. Chrys.
    """
    upper = 2**(4+difficulty)
    no_1 = random.randint(5, upper)
    no_2 = random.randint(no_1 + 10, 2*upper)
    signs = [" $<$ ", " $=$ ", " $>$ "]
    sign = random.choice([" $<$ ", " $=$ ", " $>$ "])
    question = "Choose the number that makes this statement true. \n\n" \
               r''' 
               \begin{center}
               %s %s  %s $-$ 
               \fboxsep0pt\fbox{\rule{2em}{0pt}\rule{0pt}{2.2ex}}
               \end{center}
                 ''' % (mq.dollar(no_1), sign, mq.dollar(no_2))
    less = random.sample(range(no_2 - no_1 + 1, no_2), k=4)
    more = random.sample(range(0, no_2 - no_1 - 1), k=4)
    choices = [mq.dollar(less[0]), mq.dollar(more[0]), mq.dollar(no_2-no_1)]

    if sign == signs[0]:
        answer = choices[1]
        for i in range(1, 3):
            choices.append(less[i])
    elif sign == signs[2]:
        answer = choices[0]
        for i in range(1, 3):
            choices.append(more[i])
    else:
        answer = choices[2]
        choices.append(more[1])
        choices.append(less[1])
    return mq.multiple_choice(question, choices, answer)


def pv_14(difficulty):
    """
    Filling in each square to break down number into powers of ten. Chrys.
    """
    upper = 10 ** (difficulty + 2) - 1
    lower = 10 ** (difficulty + 1)
    n = random.randint(lower, upper)
    places = ["ones", "tens", "hundreds", "thousands", "ten-thousands"]
    y = []
    results = []
    for i in reversed(range(2 + difficulty)):
        y.append(f"\\makebox[1em]{{\\hrulefill}} {places[i]}")
        results.append(f"{mq.dollar({int(str(n)[- (i + 1)])})} {places[i]}")
    values = " $+$\\ ".join(y)
    answer = " $+$\\ ".join(results)

    question = f"Break down the number" \
               f"by filling in the gaps. \n\n {mq.dollar(n)}$=$ {values} "
    return [question, answer]


def pv_15(difficulty):
    """
    Breaking down number into thousands, tens ect. filling in each part. Chrys.
    """
    upper = 10 ** (difficulty + 2) - 1
    n = random.randint(100, upper)
    suffix = ["ones", "tens", "hundreds", "thousands", "ten-thousands"]

    x = ""
    for i in range(1, len(str(n))):
        j = len(str(n)) - i
        if int(str(n)[-(j + 1)]) != 0:
            x += f"\\mbox{{{mq.dollar({int(str(n)[-(j + 1)])})}" \
                 f" {suffix[j]}}} $+$ "
    x += f"\\mbox{{{mq.dollar({int(str(n)[- 1])})} {suffix[0]}}}"

    answer = mq.dollar(n)
    square = f"\\makebox[3em]{{\\hrulefill}}"
    question = f"Find the number that completes the statement. " \
               f"\n\n {square} = {x}"
    return [question, answer]

# Addition Subtraction_____________


def as_1(difficulty):
    """Addition of numbers up to 4 digits, using columnar method. Chrys."""
    lower = 2 * (400 * difficulty - 200)
    upper = 2000 * difficulty
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    question = r'''
    \hspace{2cm}{\LARGE$\begin{array}{r}  %s \\
    \underline{+ \ %s } \\ 
    \underline{\phantom{+ \ %s}}
    \end{array}$} \\ \\ \vspace{1.2ex}''' % (b, a, a)
    answer = mq.dollar(b+a)
    return [question, answer]


def as_2(difficulty):
    """Fill in missing value to balance equation. Chrys."""
    lower = 250 * (difficulty - 1) + 50
    upper = 400 * (difficulty - 1) + 100
    sums = random.randint(lower + 10, upper)
    nums = random.sample(range(21, lower), k=2)

    n = random.randint(0, 2)
    j = random.randint(0, 1)
    plus_minus = [[nums[0], sums - nums[0]], [sums + nums[1], nums[1]]]
    values = [[nums[0], sums - nums[0], nums[1], sums - nums[1]],  # plus plus
              [sums + nums[0], nums[0], sums + nums[1], nums[1]],  # 2 x minus
              [plus_minus[j][0],
               plus_minus[j][1],
               plus_minus[(j+1) % 2][0],
               plus_minus[(j+1) % 2][1]]
              ][n]
    sign = [['$+$', '$+$'],
            ['$-$', '$-$'],
            [['$+$', '$-$'], ['$-$', '$+$']][j]
            ][n]

    k = random.randint(0, 3)
    answer = mq.dollar(values[k])
    values[k] = "\\makebox[2.5em]{\\hrulefill}"
    question = f"Find the missing number to complete the equation." \
               f"\n\n {values[0]} {sign[0]} {(values[1])} " \
               f"$=$ {values[2]} {sign[1]} {values[3]}"
    return [question, answer]


def as_3(difficulty):
    """Addition and subtraction using words. Chrys."""
    lower = 250 * (difficulty-1) + 50
    upper = 400 * (difficulty-1) + 100
    num = random.sample(range(lower, upper), k=2)
    n = random.randint(0, 1)
    values = [[num[0], num[1], num[0] + num[1]],
              [num[0] + num[1], num[0], num[1]]
              ][n]
    sign = ["plus", "minus"][n]
    question = f"What does {num2words(values[0])} {sign} " \
               f"{num2words(values[1])} equal? "
    k = random.randint(0, 1)
    question += ["Write down your answer in words.",
                 "Write down your answer using digits."
                 ][k]
    answer = [num2words(values[2]), mq.dollar(values[2])][k]
    return [question, answer]


def as_4(difficulty):
    """
    Fill in missing number in columnar method for addition & subtraction. Chrys
    """
    lower = 200 * difficulty - 150
    upper = 300 * difficulty
    x = random.sample(range(lower, upper), k=2)
    n = random.randint(0, 1)
    k = random.randint(0, 1)

    nums = [[x[1], x[0] + x[1]][n], x[0]]
    op = ['+', '-'][n]
    result = [nums[1] + nums[0], x[1]][n]
    answer = str(nums[k])
    nums[k] = ''
    for i in range(len(answer)):
        nums[k] += r'{\fboxsep0pt\fbox{\rule{0.5em}{0pt}\rule{0pt}{2ex}}}'

    question = r'''
    Fill in the missing number. \\ \\
    \hspace{2cm}{\LARGE$\begin{array}{r} 
    %s \\ \underline{%s \ %s }\\ 
    %s \\ \overline{\phantom{%s \ %s}} 
    \end{array}$}
    \vspace{1ex}
    ''' % (nums[0], op, str(nums[1]), str(result), op, str(nums[1]))
    return [question, answer]


def as_5(difficulty):
    """
    Add/subtract 3 numbers with up to 3 digits, using columnar method. Chrys.
    """
    k = random.randint(0, 1)
    n = random.randint(0, 1)
    no_1 = [[random.randint(1, 9), random.randint(10, 99)][n],
            random.randint(50 * difficulty, 100*difficulty)
            ][k]
    no_3 = [random.randint(100 * difficulty, 250 * difficulty),
            random.randint(2*difficulty, 9*difficulty)
            ][k]

    no_2 = [[random.randint(50 * difficulty, 100*difficulty),
             random.randint(10, 60*difficulty)
             ][n],
            no_1 + no_3 + random.randint(100 * difficulty, 200 * difficulty)
            ][k]
    op = ["+", "-"][k]
    question = r'''
    \hspace{2cm}{\LARGE$\begin{array}{r}
    %s \\ %s \ %s  \\
    \underline{ %s \ %s} \\ \underline{\phantom{%s \ %s}}
    \end{array}$} \\ \\
    \vspace{1.2ex}
    ''' % (no_2,  op, no_1, op, no_3, op, no_3)
    answer = [mq.dollar(no_1 + no_2 + no_3), mq.dollar(no_2 - no_3 - no_1)][k]
    return [question, answer]


def as_6(difficulty):
    """Complete table using addition and subtraction rules. Chrys."""
    lower = 100 + (10 ** difficulty)
    upper = 500 * (2 ** difficulty)
    nums = random.sample(range(lower, upper), k=5)
    col_1 = sorted(nums)

    if difficulty == 1:
        no_plus = 5 * random.randint(30, 150)
        no_minus = -50 * random.randint(2, (col_1[0] // 50))
    else:
        no_plus = random.randint(lower / 2, upper / 2)
        no_minus = 5 * random.randint(1 - (col_1[0] // 5), 1 - (lower // 5))

    n = random.randint(0, 1)
    rule = [[no_plus, 'add'], [no_minus, 'minus']][n]
    col_2 = [i + rule[0] for i in col_1]

    data_1 = [
        ['Input', f"Rule: {rule[1]} {abs(rule[0])}"],
        [str(col_1[0]), str(col_2[0])]
    ]
    for i in range(1, 5):
        data_1.append([str(col_1[i]), ''])
    table = mq.draw_table(data_1)

    question = f"Use the rule to complete the table. \n\n {table}"

    data_2 = [['Input', 'Answer'], [str(col_1[0]), str(col_2[0])]]
    for j in range(1, 5):
        data_2.append([str(col_1[j]), r'\textbf{%s}' % (col_2[j])])
    answer = mq.draw_table(data_2)

    return [question, answer]


def as_7(difficulty):
    """
    Find answer to addition/subtraction question and state if odd/even. Chrys.
    """
    lower = 10 * difficulty
    upper = 60 * difficulty
    num_1 = random.sample(range(lower, upper), k=4)
    num_2 = random.choices(range(5 * difficulty, min(num_1)), k=4)
    sign = random.choices(["$+$", "$-$"], k=4)

    results = []
    odd_even = []
    answer = ""

    for k in range(4):
        if sign[k] == "$+$":
            results.append(num_1[k] + num_2[k])
        else:
            results.append(num_1[k] - num_2[k])
        if results[k] % 2 == 0:
            odd_even.append("even")
        else:
            odd_even.append("odd")

    question = f"Solve the problem and write down " \
               f"if the answer is odd or even. \n\n " \
               f"Example: {num_1[0]} {sign[0]} {num_2[0]} " \
               f"$=$ {results[0]} is {odd_even[0]} \n\n"
    for i in range(1, 4):
        question += f"{num_1[i]} {sign[i]} {num_2[i]} $=$ " \
                    "\\makebox[2.5em]{\\hrulefill} is " \
                    "\\makebox[2.5em]{\\hrulefill} \n\n"
        answer += f"{results[i]} is {odd_even[i]} \n\n"
    return [question, answer]


def as_8(difficulty):
    """Worded addition question. Chrys."""
    lower = 100 + (200 * (difficulty - 1))
    upper = 300 + (200 * (difficulty - 1))
    nums = [random.randint(round((lower+upper)/2), upper)]
    for k in range(0, 2):
        nums.append(random.randint(round(lower/(2**k)),
                                   round((nums[k]+lower)/(2**(k+1)))
                                   ))
    question = f"In a town, {nums[0]} people travel by bus each day. " \
               f"Another {nums[1]} travel by train and {nums[2]} cycle. " \
               f"In total, how many people travel each day?"
    answer = mq.dollar(nums[0] + nums[1] + nums[2])
    return [question, answer]


def as_9(difficulty):
    """
    Find missing value in table by deducting other values from total. Chrys.
    """
    lower = 50 + (100 * (difficulty - 1))
    upper = 180 + (100 * (difficulty - 1))

    col_1 = random.sample([
        'Oasis Airways', 'Artemis Air', 'Andromeda Airlines',
        'Air Alpha', 'Air Polaris'
    ], k=3)
    col_2 = random.sample(range(lower, upper), k=3)
    total = sum(x for x in col_2)

    n = random.randint(0, len(col_2) - 1)
    answer = mq.dollar(col_2[n])
    col_2[n] = ""

    data = [[r'\textbf{Airline}', r'\textbf{Passengers}']]
    for i in range(3):
        data.append([col_1[i], str(col_2[i])])
    data.append([r'\textbf{Total}', r'\textbf{%s}' % total])
    table = mq.draw_table(data)

    question = f"Here is some information about the amount of passengers who" \
               f" flew with some airlines. \n\n {table} \n\n Using the " \
               f"table, find how many passengers flew with {col_1[n]}."
    return [question, answer]


def as_10(difficulty):
    """Subtraction patterns. Chrys."""
    nums = random.sample(range(2*difficulty, 5*difficulty), k=2)
    sums = sum(nums)

    question = "Fill in the missing values.\n\n"
    answer = ""
    if difficulty == 1:
        for i in range(5):
            question += f"{sums * (10 ** i)} " \
                        "$-$ \\makebox[2.5em]{\\hrulefill} " \
                        f"$=$ {nums[1] * (10 ** i)} \n\n"
            answer += f"{sums * (10 ** i)} $-$ {nums[0] * (10 ** i)} " \
                      f"$=$ {nums[1] * (10 ** i)} \n\n"
    else:
        values = []
        for j in range(5):
            values.append([
                sums * (10 ** j),
                nums[0] * (10 ** j),
                nums[1] * (10 ** j)
            ])
            answer += f"{values[j][0]} $-$ {values[j][1]} " \
                      f"$=$ {values[j][2]}\n\n"

            n = random.randint(0, 2)
            values[j][n] = "\\makebox[2.5em]{\\hrulefill}"
            question += f"{values[j][0]} $-$ {values[j][1]} " \
                        f"$=$ {values[j][2]}\n\n"
    return [question, answer]


def as_11(difficulty):
    """Find the missing digit of a number in the columnar method. Chrys."""
    lower = 100 + (400 * (difficulty - 1))
    upper = 300 + (500 * (difficulty - 1))
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    nums = [a, b, a + b]
    n = random.randint(0, 1)
    d = random.randint(1, len(str(nums[n])))
    answer = f"{int(str(nums[n])[d-1]): g}"
    nums[n] = r'''
    %s \hspace{0.05em} 
    \fboxsep0pt\fbox{\rule{1.05ex}{0pt}\rule{0pt}{0.75em}}
    \hspace{ 0.05em} %s 
    ''' % (str(nums[n])[:d-1], str(nums[n])[d:])
    values = [
        str(nums[n]) + "",
        str(nums[(n + 1) % 2]) + "\\hspace{0.09em}",
        str(nums[2]) + "\\hspace{0.09em}"
    ]
    k = random.sample([0, 1], k=2)
    question = r'''
    Find the missing digit. \newline 
    \hspace{2cm}{\LARGE$\begin{array}{r}  
    %s \\ 
    \underline{+\  %s } \\ 
    %s \\
    \overline{\phantom{+ \ %s}} \\ 
    \end{array}$} \ \
    \vspace{1.2ex}
    ''' % (values[k[0]], values[k[1]], values[2], values[k[1]])
    return [question, answer]


def as_12(difficulty):
    """Subtraction over zero using columnar method. Chrys."""
    a = 100 * random.randint(2, 9) * 10 ** (difficulty - 1)
    if difficulty < 3:
        b = random.randint(round(a / 2), round(a * 3 / 4))
    else:
        b = random.randint(10 * 10 ** (difficulty - 1) - 1,
                           100 * 10 ** (difficulty - 1) - 1
                           )
    if int(str(b)[-1]) == 0:
        b = b + 3
    if int(str(b)[-2]) == 0:
        b = b + 10

    question = r'''
    \hspace{2cm}{\LARGE$\begin{array}{r}
    %s \\ \underline{- \ %s} \\ \underline{\phantom{- \ %s}} 
    \end{array}$} \\ \\ 
    \vspace{1.2ex}
    ''' % (a, b, b)
    answer = mq.dollar(a - b)
    return [question, answer]


def as_13(difficulty):
    """
    Worded subtraction question where values are in word or number format.
    Chrys.
    """
    lower = 200 + 1000 * (difficulty - 1)
    upper = 1000 + 4000 * (difficulty - 1)
    x_1 = random.randint(lower, upper)
    x_2 = random.randint(round(lower * 1/2), round(x_1 * 2/3))
    name = random.choice([["Cosmos Space Agency", "rockets", "uses"],
                          ["Car dealership", "cars", "sells"],
                          ["delivery company", "packages", "delivers"],
                          ["technology company", "laptops", "sells"]
                          ])
    n = random.randint(0, 1)
    question = f"A {name[0]} has {[x_1, num2words(x_1)][n]} {name[1]}. " \
               f"It {name[2]} {[x_2, num2words(x_2)][n]} {name[1]}.\n\n " \
               f"How many {name[1]} do they have left?"
    answer = [mq.dollar(x_1 - x_2), num2words(x_1 - x_2)][n]
    return [question, answer]


def as_14(difficulty):
    """
    Subtraction of numbers up to 4 digits, using columnar method. Chrys.
    """
    lower = 100 * difficulty + round(10 ** difficulty + 1)
    upper = 100 * difficulty + round(0.5 * (10 ** (difficulty + 1) - 1))
    b = random.randint(lower, upper)
    a = random.randint(round(0.5 * lower), round(0.7 * b))
    question = r'''
    \hspace{2cm}{\LARGE$\begin{array}{r}
    %s \\ \underline{- \ %s} \\ \underline{\phantom{- \ %s}}
    \end{array}$} \\ \\
    \vspace{1.2ex}
    ''' % (b, a, a)
    answer = mq.dollar(b - a)
    return [question, answer]

# Multiplication Division______


def md_1(difficulty):
    """Multiplication of 2 or 3 digit numbers with one digit number. Chrys."""
    a = random.randint(20 + (difficulty-1) * (difficulty * 150 - 200),
                       100 + (difficulty - 1) * (difficulty * 50 + 300))
    b = random.randint(3, 9)
    question = r'''
    \hspace{2cm}{\LARGE$\begin{array}{r} 
    %s \\ \underline{\times \ %s} \\  \underline{\phantom{\times \ %s}}
    \end{array}$} \vspace{3em}
    ''' % (a, b, b)
    answer = mq.dollar(a * b)
    return [question, answer]


def md_2(difficulty):
    """Fill in missing values in times table. Chrys."""
    x = random.randint(3, 12)

    sequence = []
    for k in range(1, 12):
        sequence.append(mq.dollar(x * k))
    n = random.sample(range(11), k=2 + difficulty)

    answer = []
    for i in range(0, difficulty + 1):
        answer.append(sequence[n[i]])
        sequence[n[i]] = "\\makebox[0.025\\textwidth]{\\hrulefill}"

    answer = ",\\ ".join(answer)
    sequence = ",\\ ".join(sequence)
    question = f"Fill in the missing numbers in the sequence: \n\n {sequence} "
    return [question, answer]


def md_3(difficulty):
    """Multiplication of two numbers. Chrys."""
    x = random.randint(3, 12)
    y = random.randint(4*difficulty, 12*difficulty)
    question = mq.dollar(x) + " $\\times$ " + mq.dollar(y) + " $=$ ?"
    answer = mq.dollar(x * y)
    return [question, answer]


def md_4(difficulty):
    """
    Find the missing value, multiplication worded in groups of numbers. Chrys.
    """
    x = random.randint(2, 5+difficulty)
    y = random.randint(x, 6 * difficulty)
    values = [mq.dollar(x), mq.dollar(y), mq.dollar(x * y)]

    n = random.randint(0, 2)
    answer = values[n]
    values[n] = "\\makebox[0.025\\textwidth]{\\hrulefill}"
    question = "Find the missing value.\n\n " \
               f"{values[0]} groups of {values[1]} $=$ {values[2]}"
    return [question, answer]


def md_5(difficulty):
    """
    Factor pair multiple choice, Chrys.
    """
    while True:
        n = random.randint(1, 25 * difficulty)
        if len(mq.factors(n)) > 4:
            break
    my_list = mq.factors(n)
    choices = []
    for k in random.sample(my_list, 4):
        choices.append(str((k, n // k)))
    a = random.choice(my_list)
    my_list.remove(n // a)
    b = random.choice(my_list)
    answer = str((a, b))
    choices.append(answer)
    question = f"Which of the following is NOT a factor pair of {n}?"
    return mq.multiple_choice(question, choices, answer)


def md_6(difficulty):
    """
    Multiplication of 1 digit and two digit number using area as model. Chrys.
    """
    x = random.randint(1 + difficulty, 7+difficulty)
    y = 10 * random.randint(difficulty, 9) + random.randint(1, 9)

    if difficulty == 3:
        x = random.randint(2, 6)
        y = y + 100 * random.randint(1, 3)
    ones = y % 10
    tens = (y - ones) % 100
    hundreds = y - tens - ones

    if difficulty == 3:
        box = [
            'r',
            f"& {hundreds} \\hspace{{{1.4}em}} ",
            r'& \tikz \fill [yellow] (0,0) rectangle (1.5em, 1.2);'
        ]
        size = [0.8, 0.4]
    else:
        box = ['', '', '']
        size = [1.5, 1]

    model = r'''
    {\arraycolsep=2pt \LARGE$ \begin{array}{rrr%s} 
      $$\times$$ %s & %s \hspace{%sem} & %s \hspace{%sem} \\  %s 
      & \tikz \fill [red] (0,0) rectangle (4em, 1.2);
      & \tikz \fill [cyan] (0,0) rectangle (2.5em, 1.2); %s \\
    \end{array}$ }
    ''' % (box[0], box[1], tens, size[0], ones, size[1], x, box[2])

    question = f"Use the model to solve {mq.dollar(x)}" \
               f" $\\times$ {mq.dollar(y)}." \
               f"\n\n \\textit{{Hint: Find each area first.}} \n\n {model}"
    answer = mq.dollar(x * y)
    return [question, answer]


def md_7(difficulty):
    """
    Choose whether a number is/ is not a multiple of a given number. Chrys.
    """
    num = random.randint(2 + difficulty, 9 + difficulty)
    multiplier = random.randint(2 + difficulty, 14 + difficulty)
    n = random.randint(0, 1)
    choices = ['True', 'False']
    is_not = ['', 'NOT'][n]
    k = random.randint(0, 1)
    a = [num * multiplier, num * multiplier + random.randint(1, num - 1)][k]
    answer = choices[(n + k) % 2]
    question = f"True or False, the number {a} is " \
               f"{is_not} a multiple of {num}?"
    return mq.multiple_choice(question, choices, answer)


def md_8(difficulty):
    """
    Choose the two numbers that multiply to produce a given answer. Chrys.
    """
    a = random.randint(difficulty + 2, 9 + difficulty)
    b = random.randint(3 * difficulty, 12 + 3 * (difficulty - 1))
    if b == a:
        b = b + 1

    num = a * b
    factor = mq.factors(num)

    choices = [a, b]

    while len(choices) < 4:
        rand = random.randint(2, round(0.5*num))
        if rand not in factor and rand not in choices:
            choices.append(str(rand))
    shuffle(choices)
    choices = ",\\ ".join([str(k) for k in choices])

    question = r'''
    Choose the two numbers from the list that complete the 
    multiplication.
    \begin{center} %s  \\ 
    \vspace{1em} \hspace{1em} \makebox[3em]{\hrulefill} \ 
    $\times$ \ \makebox[3em]{\hrulefill} $=$ %s
    \end{center}
    ''' % (choices, num)
    answer = ",\\ ".join([str(a), str(b)])
    return [question, answer]


def md_9(difficulty):
    """Long division"""
    power = difficulty + 1
    m = random.randint(2, 9 + difficulty)
    n = random.randint(4 ** power // m, (5 ** (power + 1) - 1) // m)
    question = f"\\intlongdivision[stage=0]{{{m * n}}}{{{m}}}"
    answer = str(n)
    return [question, answer]


# noinspection PyTypeChecker
def md_10(difficulty):
    """Find missing number in multiplication/division"""
    a = random.randint(2 + difficulty, 9 + difficulty)
    b = random.randint(2 + difficulty, 9 + difficulty)
    n = random.randint(0, 1)
    values = [[a, b, a * b], [a * b, a, b]][n]
    sign = ["$\\times$", "$\\div$"][n]

    k = random.randint(0, 1)
    answer = str(values[k])
    values[k] = "\\makebox[0.03\\textwidth]{\\hrulefill}"

    question = "Fill in the missing value. \n\n \\begin{center}" \
               f"{values[0]} {sign} {values[1]} = {values[2]} \\end{{center}}"
    return [question, answer]


def md_11(difficulty):
    """Multiplication of three values"""
    a = random.randint(3 + difficulty, 9 + difficulty)
    b = random.randint(2 + difficulty, 7 + difficulty)
    c = random.randint(2, 2 + difficulty)
    question = f"{str(a)} $\\times$ {str(b)} $\\times$ {str(c)} $=$ ?"
    answer = str(a * b * c)
    return [question, answer]


def md_12(difficulty):
    """Worded Multiplication question"""
    a = random.randint(1 + difficulty, 8 + 2 ** (difficulty - 1))
    b = 100 * difficulty + 10 * random.randint(1, 9)
    if difficulty > 1:
        b = b + random.randint(1, 9)
    n = random.randint(0, 2)
    name = [
        ["An airline", "planes", "plane", "passengers"],
        ["A company", "offices", "office", "workers"],
        ["A train company", "trains", "train", "seats"],
    ][n]
    question = f"{name[0]} has {str(a)} {name[1]}. " \
               f"Each {name[2]} has {str(b)} {name[3]}. " \
               f"How many {name[3]} are there in total?"
    answer = mq.dollar(a*b)
    return [question, answer]


def md_13(difficulty):
    """Choose the number that is/is not a multiple of a given value"""
    a = random.randint(2 + 2 ** (difficulty - 1), 9 + difficulty)
    multipliers = random.sample(range(2 + difficulty, 11 + difficulty), k=6)

    n = random.randint(0, 1)
    is_not = ["", "NOT"][n]

    choices = []
    for k in range(4):
        values = a * multipliers[k]
        if n == 0:
            values = values + random.randint(1, a - 1)
        choices. append(str(values))

    answer = a * multipliers[5]
    if n == 1:
        answer = answer + random.randint(1, a - 1)
    choices.append(answer)
    question = f"Which one of these numbers is {is_not} a multiple of {a}?"
    return mq.multiple_choice(question, choices, answer)


def md_14(difficulty):
    """finding value that is how many times more/less than a given value"""
    num = random.randint(3 * difficulty, 12 + 9 * (difficulty - 1))
    factor = random.randint(2 + difficulty, 9 + difficulty)

    name = []
    for i in range(2):
        name.append(names.get_first_name())
    item = random.choice([
        "pens", "sweets", "books",
        "fossils", "cupcakes", "marbles"
    ])

    n = random.randint(0, 1)
    more_less = ["as many as", f"as less than"][n]
    values = [num, num * factor]

    question = f"{name[0]} has {values[n]} {item}. {name[1]} has " \
               f"{factor} times {more_less} {name[0]}. " \
               f"How many {item} does {name[1]} have?"
    answer = str(values[(n + 1) % 2])
    return [question, answer]


def md_15(difficulty):
    """Complete table using multiplication or division rule. Chrys"""
    operand = random.randint(2 + difficulty, 12)
    n = random.randint(0, 1)
    operator = ['Times by', 'Divide by'][n]

    nums = random.sample(range(2 + difficulty, 11 + difficulty), k=5)
    sorted_results = sorted(i * operand for i in nums)

    if n == 0:
        col_1 = sorted(nums)
        col_2 = sorted_results
    else:
        col_1 = sorted_results
        col_2 = sorted(nums)

    data_1 = [
        [r'\textbf{Input}', r'\textbf{Rule: %s %s}' % (operator, operand)],
        [str(col_1[0]), str(col_2[0])]
    ]
    for i in range(1, 5):
        data_1.append([str(col_1[i]), ''])
    table = mq.draw_table(data_1)

    question = f"Use the rule to complete the table. \n\n {table}"

    data_2 = [
        [r'\textbf{Input}', r'\textbf{Answer}'], [str(col_1[0]), str(col_2[0])]
    ]
    for j in range(1, 5):
        data_2.append([str(col_1[j]), r'\textbf{%s}' % col_2[j]])

    answer = mq.draw_table(data_2)
    return [question, answer]


def md_16(difficulty):
    """Multiplication/Division patterns. Chrys."""
    nums = random.sample(range(2 + difficulty, 9 + difficulty), k=2)
    result = nums[0] * nums[1]

    question = "Fill in the missing values.\n\n"
    answer = ""
    values = []
    k = random.randint(0, 1)
    operator = ["$\\times$", "$\\div$"][k]

    for j in range(4 - k):
        values.append([
            [nums[0], result * (10 ** j)][k],
            [nums[1] * (10 ** j), nums[1]][k],
            [result * (10 ** j), nums[0] * (10 ** j)][k]
        ])
        answer += f"{values[j][0]} {operator} {values[j][1]} " \
                  f"$=$ {values[j][2]}\n\n"

        n = [random.randint(1, 2), random.choice([0, 2])][k]
        values[j][n] = "\\makebox[2.5em]{\\hrulefill}"
        question += f"{values[j][0]} {operator} {values[j][1]} " \
                    f"$=$ {values[j][2]}\n\n"
    return [question, answer]


def md_17(difficulty):
    """Worded multiplication question with 3 numbers. Chrys."""
    num_1 = random.randint(2, 5)
    num_2 = random.randint(2 + difficulty, 5 + difficulty)
    num_3 = random.randint(5 + difficulty, 9 + difficulty)
    n = random.randint(0, 6)
    items = [
        [
            "school", "floors", "floor",
            "classrooms", "class", "tables"],
        [
            "cinema", "rooms", "room",
            "rows", "row", "seats"],
        [
            "rail company", "trains", "train",
            "carriages", "carriage", "passengers"],
        [
            "company", "offices", "office",
            "departments", "department", "employees"],
        [
            "company", "restaurants", "restaurant",
            "tables", "table", "seats", "customers can they seat"],
        [
            "space company", "factories", "factory",
            "spacecrafts", "spacecraft", "engines", "engines do they produce"],
        [
            "sports competition", "events", "event",
            "teams", "team", "athletes", "athletes are competing"]
    ][n]

    if n <= 1:
        items.append(f"{items[5]} does the {items[0]} have")
    elif 2 <= n <= 3:
        items.append(f"{items[5]} are there")

    question = f"A {items[0]} has {num_1} {items[1]}. " \
               f"Each {items[2]} has {num_2} {items[3]}. " \
               f"Each {items[4]} has {num_3} {items[5]}. " \
               f"How many {items[6]} have in total?"

    answer = mq.dollar(num_1 * num_2 * num_3)
    return [question, answer]


def md_18(difficulty):
    """find answer to x divided by y. Chrys."""
    a = random.randint(3, 12)
    b = random.randint(2 * difficulty, 9 + difficulty)
    question = f"What is {a * b} $\\div$ {b}?"
    answer = mq.dollar(a)
    return [question, answer]


def md_19(difficulty):
    """long Division with remainder. Chrys."""
    m = random.randint(2 * difficulty, 12)
    n = random.randint(200 * difficulty - 100, 450 * difficulty - 350)
    question = f"\\longdivision[stage=0]{{{n}}}{{{m}}}"
    if n % m:
        answer = f"{n // m} r.{n % m}"
    else:
        answer = str(n // m)
    return [question, answer]


def md_20(difficulty):
    """Multiplication using distributive law. Chrys."""
    a = random.randint(2 * difficulty, 12)
    b = random.randint(2 * difficulty, 9 + difficulty)
    c = random.randint(3 * difficulty, 9 + difficulty)
    d = random.randint(2 * difficulty, 9 + difficulty)
    question = f"What is {a} $\\times$ ({b} $+$ {c}"
    if difficulty == 3:
        question += f" $+$ {d})?"
        answer = mq.dollar(a * (b + c + d))
    else:
        question += ")?"
        answer = mq.dollar(a * (b + c))
    return [question, answer]


def md_21(difficulty):
    """Choose the two numbers that divide to produce a given answer. Chrys."""
    a = random.randint(2 * difficulty, 4 + 2 ** difficulty)
    b = random.randint(3 + difficulty, 10 + 4 * (difficulty - 1))
    if a == b:
        b = b + 1
    num = a * b

    choices = [a, num]
    while len(choices) < 4:
        rand = random.randint(2, num + 10)
        for k in choices:
            if rand / k != b and k / rand != b and rand not in choices:
                choices.append(rand)
    shuffle(choices)
    choices = ",\\ ".join([str(i) for i in choices])

    question = r'''
    Choose the two numbers from the list that complete the statement. \
    \begin{center} %s \end{center} 
    \begin{center} 
    \makebox[3em]{\hrulefill} \ $\div$ \ \makebox[3em]{\hrulefill} $=$ %s 
    \end{center}
    ''' % (choices, b)
    answer = ",\\ ".join([str(num), str(a)])
    return [question, answer]


def md_22(difficulty):
    """Find missing values in division table. Chrys"""
    col_2 = random.sample(range(2 + difficulty, 9 + difficulty), k=5)
    col_3 = random.choices(range(2 + difficulty, 10 + 2 * difficulty), k=5)

    values = []
    for i in range(5):
        values.append([col_2[i] * col_3[i], col_2[i], col_3[i]])

    title = [
        'Total',
        r'\shortstack{Number of \\ Groups}',
        r'\shortstack{Number in \\ Each Group}'
    ]

    data_ans = [title]
    for j in range(5):
        n = random.randint(0, 2)
        values[j][n] = r'\textbf{%s}' % values[j][n]
        data_ans.append(
            [str(values[j][0]), str(values[j][1]), str(values[j][2])]
        )
        values[j][n] = ""
    answer = mq.draw_table(data_ans)

    data_q = [title]
    for k in range(5):
        data_q.append(
            [str(values[k][0]), str(values[k][1]), str(values[k][2])]
        )
    table = mq.draw_table(data_q)
    question = r'Fill in the missing values in the table using the formula.' \
               r'\\ \\ \textit{Total} = ' \
               r'\textit{Number of Groups} \\ \hphantom{Total =}' \
               r'$\times$ \textit{Number in Each Group}' + table
    return [question, answer]


def md_23(difficulty):
    """
    Worded division question, dividing 3 digit number, includes remainder.
    Chrys.
    """
    n = random.randint(100 * difficulty, 250 * difficulty)
    m = random.randint(2 * (difficulty + 1), 11 + difficulty)

    k = random.randint(0, 4)
    choices = [
        ["party", "guests", "table", "hold", "guests"],
        ["concert", "attendees", "row", "seat", "people"],
        ["bakery", "pastries to deliver", "box", "hold", "pastries"],
        ["racing track", "people waiting to race", "race", "fit", "people"],
        [
            "sports competition", "athletes competing",
            "team", "have up to", "athletes"]
    ][k]

    question = f"A {choices[0]} has {n} {choices[1]}. " \
               f"Each {choices[2]} can {choices[3]} {m} {choices[4]}. " \

    question += [
        "How many tables will be needed to hold all the guests?",
        "How many rows of seats will be needed to hold all the attendees?",
        "How many boxes will be needed in total?",
        "How many races are needed so that everyone can have a go?",
        "How many teams are needed so that everyone gets to compete?"
    ][k]
    answer = str(ceil(n / m))
    return [question, answer]


def md_24(difficulty):
    """
    Worded division question that divides 3 digit number into an integer. Chrys
    """
    a = random.randint(2 * (difficulty + 1), 11 + difficulty)
    b = random.randint(5 + 5 * difficulty, 15 + 5 * difficulty)
    c = a * b

    k = random.randint(0, 4)
    choices = [
        ["An aeroplane", "passengers", "rows of seats", "row"],
        ["A train", "passengers", "carriages", "carriage"],
        ["A library", "books", "shelves", "shelf"],
        ["space company", "do", "launches"],
        ["bookshop", "sell", "books"]
    ][k]

    if k <= 2:
        question = f"{choices[0]} has {c} {choices[1]} that need to be" \
                   f" divided equally across {a} {choices[2]}. " \
                   f"How many {choices[1]} are there per {choices[3]}?"
    else:
        question = f"A {choices[0]} needs to {choices[1]} {c} {choices[2]} " \
                   f"within {a} months. How many {choices[2]} will they " \
                   f"need to {choices[1]} per month to achieve this target?"
    answer = str(b)
    return [question, answer]


def md_25(difficulty):
    """
    True or false question whether an integer is divisible by another. Chrys
    """
    b = random.randint(3 + difficulty, 12)
    n = random.randint(0, 1)
    a = [
        b * random.randint(10 * difficulty, 10 + 10 * difficulty),
        b * random.randint(10 * difficulty, 10 + 10 * difficulty)
        + random.randint(1, b - 1)
    ][n]

    choices = ["True", "False"]
    answer = choices[n]
    question = f"Is {a} divisible by {b}?"
    return mq.multiple_choice(question, choices, answer)


def md_26(difficulty):
    """division using model, with area given. Chrys."""
    x = random.randint(3, 8 + (difficulty % 3))
    tens = random.randint(1, 3 * difficulty) * 10
    ones = random.randint(1, 9)

    box = r'\fboxsep0pt\fbox{\rule{1.7em}{0pt}\rule{0pt}{1em}}'
    if difficulty == 3:
        rectangle = [
            'r',
            r'& %s \hspace{1.1em}' % box,
            r'& \colorbox{yellow}'
            r'{\makebox(40,34){\textcolor{black}{%s}}}' % (ones * x),
        ]
        size = [0.8, 0.4]
        values = [100 * x, tens * x, 100 + tens + ones]
    else:
        rectangle = ['', '', '']
        size = [0.95, 0.9]
        values = [tens * x, ones * x, tens + ones]

    model = r'''
    {\arraycolsep=2pt\LARGE$\begin{array}{rrr%s}
    %s & %s \hspace{%sem} & %s \hspace{%sem} \\
    %s 
    & \colorbox{red}{\makebox(59,34){\textcolor{black}{%s}}}
    & \colorbox{cyan}{\makebox(55,34){\textcolor{black}{%s}}}
    %s 
    \end{array}$} \
    ''' % (rectangle[0], rectangle[1], box, size[0], box,
           size[1], x, values[0], values[1], rectangle[2])

    question = f"Use the model to solve {x * values[2]} $\\div$ {x}." \
               f"\n\n \\textit{{Hint: Firstly, use the areas to find the " \
               f"missing lengths of the rectangles.}} \n\n" + model
    answer = mq.dollar(values[2])
    return [question, answer]


# FRACTION QUESTIONS____________

def fr_1(difficulty):
    """Fraction addition and subtraction question. Chrys."""
    lower = 2 ** (1 + difficulty)
    upper = 2 ** (3 + difficulty)
    denominator = random.randint(lower, upper)
    sums = random.sample(range(1, denominator), 3)

    num_1 = sums[0]
    num_2 = sums[1] - sums[0]
    num_3 = sums[2] - sums[1]

    op_1 = op_2 = '$+$'
    if num_2 < 0:
        op_1 = '$-$'
        num_2 = -num_2
    if num_3 < 0:
        op_2 = '$-$'
        num_3 = -num_3

    fracs = [
        r'$\frac{%s}{%s}$' % (num_1, denominator),
        r'$\frac{%s}{%s}$' % (num_2, denominator),
        r'$\frac{%s}{%s}$' % (num_3, denominator),
    ]
    question = r'''
    \begin{LARGE} %s%s%s%s%s $=$ ? \end{LARGE}
    ''' % (fracs[0], op_1, fracs[1], op_2, fracs[2])
    answer = r'$\frac{%d}{%d}$' % (sums[2], denominator)
    return [question, answer]


def fr_2(difficulty):
    """Write fraction as decimal. Chrys."""
    n = random.randint(0, 2)
    a = [
        random.randint(1, 3 + 16 * difficulty * n),
        random.randint(1, 9)
    ][n % 2]
    b = [4, 10, 100][n]
    fraction = [
        mq.latex_frac_simplify(a, b),
        mq.latex_frac(a, b),
        mq.latex_frac(a, b)
    ][n]

    question = f"Write ${fraction}$ as a decimal."
    answer = mq.dollar(a / b)
    return [question, answer]


def fr_3(difficulty):
    """Find missing number when converting decimal to fraction. Chrys."""
    n = random.randint(0, 2)
    a = [
        random.randint(1, 3),
        random.randint(1, 9),
        random.randint(1, 33 * difficulty)
    ][n]
    b = [4, 10, 100][n]

    if a == 2 and b == 4:
        a = 1
        b = 2

    choice = [a, b]
    k = random.randint(0, 1)
    answer = str(choice[k])
    choice[k] = "\\fboxsep0pt\\fbox{\\rule{1.5em}{0pt}\\rule{0pt}{0.8em}}"

    question = f"Fill in the missing value to complete the statement. \n\n" \
               f" \\begin{{center}} \\LARGE {a / b} $=$ " \
               f"${mq.latex_frac(choice[0], choice[1])}$ \\normalsize" \
               f"\\end{{center}}"
    return [question, answer]


def fr_4(difficulty):
    """Round number with 1 decimal place to nearest integer. Chrys."""
    integer = random.randint(1, 10 ** (difficulty + 1))
    int_choices = [
        0,
        9 + random.randint(0, 100),
        99 + 100 * random.randint(1, 100)
    ][difficulty - 1]

    decimal = 0.1 * random.randint(1, 9)
    n = random.choice([integer + decimal, int_choices + decimal])

    question = f"Round {n} to the nearest whole number."
    answer = mq.dollar(round(n))
    return [question, answer]


def fr_5(difficulty):
    """Which decimal is smallest/largest. Chrys."""
    size = random.choice(["smallest", "largest"])
    upper = [8, 819, 819][difficulty - 1]

    n = random.randint(1, upper)
    numbers = random.sample(range(1, 20 * (2 ** (3 - difficulty))), 5)
    dec_places = [100, 1000, 1000][difficulty - 1]
    decimals = [(n + i) / dec_places for i in numbers]
    if size == "smallest":
        answer = min(decimals)
    else:
        answer = max(decimals)
    question = f"Which of the following decimals is the {size}?"
    return mq.multiple_choice(question, decimals, answer)


def fr_6(difficulty):
    """Arrange fractions from smallest to largest and vice versa. Chrys."""
    upper = random.choices(
        [8, 12, 16], weights=(3, difficulty + 1, difficulty))[0]
    denominator = [upper, upper, upper // 2, upper // 4]
    numerator = [
        random.randint(1, upper // 2 - 1),
        random.randint(upper // 2 + 1, upper - 1)
    ]

    compare = [numerator[0] / upper, numerator[1] / upper]
    while len(numerator) < 4:
        num_1 = random.randint(1, upper // 2 - 1)
        num_2 = random.randint(1, upper // 4 - 1)
        nums = [num_1 / denominator[2], num_2 / denominator[3]]
        for i in range(len(nums)):
            if nums[0] != nums[1] and nums[i] not in compare:
                numerator.extend([num_1, num_2])

    values = []
    for k in range(4):
        values.append((
            f"${mq.latex_frac(numerator[k], denominator[k])}$",
            numerator[k] / denominator[k]
        ))
    shuffle(values)

    n = random.randint(0, 1)
    ordered = [
        sorted(values, key=lambda x: x[1]),
        sorted(values, key=lambda x: x[1], reverse=True)
    ][n]
    size = ["smallest to largest", "largest to smallest"][n]
    question = f"Arrange the fractions from {size}.\n\n " \
               f"\\begin{{center}} \\LARGE"
    question += ", ".join([values[i][0] for i in range(len(values))])
    question += "\\end{center} \\large"
    answer = ', '.join([ordered[j][0] for j in range(len(ordered))])
    return [question, answer]


def fr_7(difficulty):
    """What decimal is the nth smallest/ largest. Chrys."""
    upper = [8, 819, 819][difficulty - 1]
    m = random.randint(1, upper)
    numbers = random.sample(range(1, 20 * (2 ** (3 - difficulty))), 5)
    dec_places = [100, 1000, 1000][difficulty - 1]
    decimals = [(m + i) / dec_places for i in numbers]

    k = random.randint(0, 1)
    order = ["smallest to largest", "largest to smallest"][k]
    n = random.randint(1, 5)
    question = f"If you order the following decimals from {order}," \
               f" which comes {num2words(n, to='ordinal')}?"

    choices = []
    my_list = []
    for i in range(5):
        my_list.append(decimals[i])
        choices.append(mq.dollar(decimals[i]))
    if k == 0:
        my_list.sort()
    else:
        my_list.sort(reverse=True)
    answer = mq.dollar(my_list[n - 1])
    return mq.multiple_choice(question, choices, answer)


def fr_8(difficulty):
    """
    Identify tenths, hundredths and thousandths digits from decimal. Chrys.
    """
    places = ["thousandths", "hundredths", "tenths"]
    integer = random.choice([0, random.randint(0, 99)])
    power = 10 ** difficulty
    decimal = random.randint(power + 1, 10 * power - 1)
    if decimal % 10 == 0:
        decimal = decimal + 1
    n = integer + (decimal / (10 * power))

    d = random.randint(2 - round(difficulty / 3), 3)
    question = f"What is the value of the {places[d - 1]} digit in " \
               f"the number {n}?"
    answer = mq.dollar(f"{int(str(n)[- d + (2 - difficulty)]) :g}")
    return [question, answer]


def fr_9(difficulty):
    """Find answer to a fraction of a given integer. Chrys."""
    n = random.randint(2, 2 + 2 ** difficulty)
    m = random.choices(
        [1, random.randint(1, n - 1)],
        weights=(4, difficulty)
    )[0]
    a = n * random.randint(1, 3 + difficulty)
    question = f"What is ${mq.latex_frac(m, n)}$ of {a}?"
    answer = mq.dollar((m * a) // n)
    return [question, answer]


def fr_10(difficulty):
    """Compare sums and difference of fractions with same denominator. Chrys"""
    n = random.randint(4, 2 + 2 ** difficulty)
    a = random.randint(1, n - 1)
    b = random.randint(1, n - a)
    c = random.randint(2, n - 1)

    if a > b:
        op = "$-$"
        result = (a - b)
    else:
        op = "$+$"
        result = (a + b)

    question = "Which sign that makes the following statement true. \n\n" \
               f"\\begin{{center}} \\huge ${mq.latex_frac(a, n)}$ " \
               f"{op} ${mq.latex_frac(b, n)}$ $\\square$ " \
               f"${mq.latex_frac(c, n)}$ \\end{{center}} \\large"
    choices = [
        "\\LARGE $<$ \\large",
        "\\LARGE $=$ \\large",
        "\\LARGE $>$ \\large"
    ]
    if result > c:
        answer = choices[2]
    elif result < c:
        answer = choices[0]
    else:
        answer = choices[1]
    return mq.multiple_choice(question, choices, answer)


def fr_11(difficulty):
    """Choose which fraction is equivalent to the one given. Chrys."""
    n = random.randint(2, 4 + 2 ** difficulty)
    m = random.randint(1, n - 1)

    choices = []
    if mq.gcd(m, n) != 1 and mq.gcd(m, n) != n:
        answer = f"${mq.latex_frac_simplify(m, n)}$"
    else:
        c = random.randint(2, 2 + difficulty)
        answer = f"${mq.latex_frac(m * c, n * c)}$"
    choices.append(answer)

    k = random.randint(2, 3 + difficulty)
    lower = random.randint(1, m * k - 1)
    upper = random.randint(m * k + 1, n * k - 1)
    choice_1 = random.choice([lower, upper])
    choices.append(f"${mq.latex_frac(choice_1, n * k)}$")

    my_list = [m/n, lower / n * k, upper / n * k]
    while len(choices) < 5:
        b_2 = random.randint(2, 11 + difficulty)
        a_2 = random.randint(1, b_2 - 1)
        while a_2 / b_2 != m / n and a_2 / b_2 not in my_list:
            choices.append(f"${mq.latex_frac(a_2, b_2)}$")
            my_list.append(a_2 / b_2)

    question = "Which of these fractions is equivalent to " \
               f"${mq.latex_frac(m, n)}$?"
    return mq.multiple_choice(question, choices, answer)


def fr_12(difficulty):
    """Simplify fraction. Chrys."""
    n = random.randint(2, 4 + 2 ** difficulty)
    m = random.randint(1, n - 1)
    if 1 < mq.gcd(n, m) < n:
        a = m
        b = n
        answer = f"${mq.latex_frac_simplify(m, n)}$"
    else:
        c = random.randint(2, 2 + difficulty)
        a = m * c
        b = n * c
        answer = f"${mq.latex_frac(m, n)}$"
    question = f"Simplify the fraction ${mq.latex_frac(a, b)}$ " \
               "to it's lowest form."
    return [question, answer]


def fr_13(difficulty):
    """Identify what fraction of a rectangle is shaded. Chrys."""
    n = random.randint(3, 8 + 2 ** (difficulty - 1))
    m = random.randint(1, n - 1)
    shaded_boxes = r''
    white_boxes = r''
    r = ""

    if n <= 6:
        size = [2, 2]
    elif 6 < n <= 9:
        size = [1.75 - 0.2 * (n - 7), 2]
    else:
        size = [1.2 - 0.1 * (n - 10), 2]

    colour = random.choice(["red", "cyan", "yellow"])
    for i in range(m):
        shaded_boxes += r'& \tikz \draw [fill=%s] (0,0) rectangle ' \
                        r'(%sem, %sem);' % (colour, size[0], size[1])
    for j in range(n-m):
        white_boxes += r'& \tikz \draw [fill=white] (0,0) rectangle ' \
                       r'(%sem, %sem);' % (size[0], size[1])
    for k in range(n):
        r += "r"

    box = r'''
    {\arraycolsep=0pt \LARGE$ \begin{array}{r%s} %s %s \end{array}$} \
    ''' % (r, shaded_boxes, white_boxes)
    question = f"What fraction of the shape is shaded? "
    if difficulty == 1:
        answer = f"${mq.latex_frac(m, n)}$"
    else:
        question += f"Reduce your answer to its lowest form. "
        answer = f"${mq.latex_frac_simplify(m, n)}$"
    question += f"\n\n {box}"
    return [question, answer]


def fr_14(difficulty):
    """
    Choose which of the shaded rectangles represent the given fraction. Chrys.
    """
    quantity = 1 + difficulty
    m = []
    n = []
    my_list = []

    while len(m) < quantity:
        for i in range(quantity):
            b = random.randint(3, 8 + 2 ** (difficulty - 1))
            a = random.randint(1, b - 1)
            if a / b not in my_list and b not in n:
                m.append(a)
                n.append(b)
                my_list.append(a / b)

    choices = []
    colour = ["cyan", "red", "yellow", "orange"]
    shuffle(colour)
    for i in range(quantity):
        shaded_boxes = ""
        white_boxes = ""
        r = ""
        for j in range(m[i]):
            shaded_boxes += r'& \tikz \draw [fill=%s] (0,0)' \
                            r' rectangle (0.9em, 2em);' % (colour[i])
        for j in range(n[i] - m[i]):
            white_boxes += r'& \tikz \draw [fill=white] (0,0) ' \
                           r'rectangle (0.9em, 2em);'
        for k in range(n[i]):
            r += "r"
        box = r'''
        {\arraycolsep=0\leftmargin\LARGE$ \begin{array}{r%s} 
        %s %s \end{array}$}  \ \newline
        ''' % (r, shaded_boxes, white_boxes)
        choices.append(box)

    question = f"What model has had ${mq.latex_frac_simplify(m[0], n[0])}$ " \
               f"of it shaded?"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer)


def fr_15(difficulty):
    """Find the proportion of a pattern that is a specified shape. Chrys."""
    b = random.randint(3 + difficulty, 9 + difficulty)
    a_1 = random.randint(1, b - 2)
    a_2 = random.randint(1, b - a_1 - 1)
    a_3 = b - a_1 - a_2

    k = random.randint(0, 2)
    shape_names = ["circles", "squares", "triangles"][k]

    order = []
    for i in range(a_1):
        circle = r'\tikz \node[circle, text opacity=0, minimum size=1.5em,' \
                 r' draw=blue,fill=blue] (c) {};'
        order.append(circle)
    for j in range(a_2):
        square = r'\tikz \node[regular polygon, regular polygon sides=4, ' \
                 r' text opacity=0, minimum size=2em, ' \
                 r'draw=red,fill=red] (S) {};'
        order.append(square)
    for n in range(a_3):
        triangle = r'\tikz \node[isosceles triangle, minimum size=1.5em, ' \
                   r'text opacity=0, rotate=90,' \
                   r'draw=yellow,fill=yellow] (T) {};'
        order.append(triangle)
    shuffle(order)

    r = ""
    if b <= 6 and b % 2 == 1:
        columns = b
        shapes_1 = '&'.join(map(str, [order[i] for i in range(columns)]))
        shapes = shapes_1
    else:
        columns = ceil(b / 2)
        shapes_1 = '&'.join(map(str, [order[i] for i in range(columns-1)]))
        shapes_2 = \
            '&'.join(map(str, [order[i] for i in range(columns, len(order))]))
        shapes = shapes_1 + "\\\\" + shapes_2
    for m in range(columns):
        r += "r"

    model = r'''
    \begin{center}
    {\arraycolsep=2pt\LARGE$\begin{array}{%s} %s \end{array}$} 
    \end{center}
    ''' % (r, shapes)
    question = f"What fraction of the shapes are {shape_names}? " \

    if mq.gcd([a_1, a_2, a_3][k], b) != 1 and difficulty > 1:
        question += f"Simplify your answer where possible."
        answer = f"${mq.latex_frac_simplify([a_1, a_2, a_3][k], b)}$"
    else:
        answer = f"${mq.latex_frac([a_1, a_2, a_3][k], b)}$"
    question += f"\n\n{model}"
    return [question, answer]


def fr_16(difficulty):
    """Convert worded version of fraction into numbers. Chrys."""
    b = random.randint(1 + difficulty, 4 + 2 ** difficulty)
    a = random.randint(1, b - 1)

    if b == 2:
        denominator = "half"
    elif b == 4:
        denominator = "quarter"
    else:
        denominator = f"{num2words(b, ordinal=True)}"
    if a != 1:
        denominator += "s"

    question = f"Write down {num2words(a)} {denominator} as a fraction."
    answer = f"${mq.latex_frac(a, b)}$"
    return [question, answer]


def fr_17(difficulty):
    """Convert decimal to fraction and vice versa. Chrys."""
    n = random.randint(0, 1)
    num_type = ["decimal", "fraction"][n]
    b = 10 ** difficulty
    a = random.choice([x for x in range(1, b) if mq.gcd(x, 10) == 1])
    fraction = mq.dollar(mq.latex_frac(a, b))
    decimal = a / b
    num = [fraction, mq.dollar(decimal)][n]
    answer = [mq.dollar(decimal), fraction][n]
    question = f"What is {num} as a {num_type}?"
    return [question, answer]


def fr_18(difficulty):
    """
    Fill in each square to break down decimal number into powers of tens. Chrys
    """
    upper = 10 ** difficulty
    decimal = random.randint(upper / 10 + 1, upper - 2)
    if decimal % 10 == 0:
        decimal = decimal + 1
    integer = random.randint(1, upper - 1)
    num = integer + decimal / upper

    integer_place = ["ones", "tens", "hundreds", "thousands"]
    decimal_place = ["tenths", "hundredths", "thousandths"]

    y_1 = f"\\makebox[1em]{{\\hrulefill}} " \
          f"{integer_place[len(str(integer)) - 1]}"
    y_2 = ""

    result_int = f"{mq.dollar({int(str(integer)[- len(str(integer))])})} " \
                 f"{integer_place[len(str(integer)) - 1]}"
    result_dec = f""

    if len(str(integer)) > 1:
        for i in reversed(range(1, len(str(integer)))):
            y_1 += f" $+$ \\makebox[1em]{{\\hrulefill}} {integer_place[i - 1]}"
            result_int += f" $+$ {mq.dollar({int(str(integer)[- i])})} " \
                          f"{integer_place[i - 1]} "

    for j in range(len(str(decimal))):
        y_2 += f" $+$ \\makebox[1em]{{\\hrulefill}} {decimal_place[j]}"
        result_dec += f" $+$ {mq.dollar({int(str(decimal)[j])})} " \
                      f"{decimal_place[j]} "

    answer = result_int + result_dec
    question = f"Break down the number " \
               f"by filling in the gaps. \n\n {mq.dollar(num)} $=$ {y_1} {y_2}"
    return [question, answer]


def fr_19(difficulty):
    """Addition/Subtraction of two fractions with same denominator. Chrys."""
    b = random.randint(3, 9 + difficulty)
    a_1 = random.randint(1, b - 2)
    a_2 = random.randint(1, b - a_1 - 1)
    if a_2 < a_1:
        op = "$-$"
        k = 1
    elif a_2 == a_1:
        k = random.randint(0, 1)
        op = ["$+$", "$-$"][k]
    else:
        op = "$+$"
        k = 0
    question = f" \\Large ${mq.latex_frac(a_1, b)}$ {op} " \
               f"${mq.latex_frac(a_2, b)}$ $=$ \\large"
    answer = f"${mq.latex_frac(a_1 + ((-1) ** k) * a_2, b)}$"
    return [question, answer]


# noinspection PyTypeChecker
def fr_20(difficulty):
    """Find missing value in subtraction/addition of two fractions. Chrys."""
    b = random.randint(3, 9 + difficulty)
    a_1 = random.randint(1, b - 2)
    a_2 = random.randint(1, b - a_1 - 1)
    if a_2 < a_1:
        op = "$-$"
        k = 1
    elif a_2 == a_1:
        k = random.randint(0, 1)
        op = ["$+$", "$-$"][k]
    else:
        op = "$+$"
        k = 0
    values = [
        [a_1, b],
        [a_2, b],
    ]
    n = random.randint(0, 1)
    answer = f"${mq.latex_frac(values[n][0], b)}$"
    fracs = [f"${mq.latex_frac(values[0][0], values[0][1])}$",
             f"${mq.latex_frac(values[1][0], values[1][1])}$"
             ]
    fracs[n] = "?"
    if a_1 + ((-1) ** k) * a_2 == 0:
        result = 0
    else:
        result = f"${mq.latex_frac(a_1 + ((-1) ** k) * a_2, b)}$"
    question = f" Fill in the missing number: \n\n \\Large " \
               f"{fracs[0]} {op} {fracs[1]} " \
               f"$=$ {result} \\large"
    return [question, answer]


def fr_21(difficulty):
    """Worded subtraction question. Subtracting 2 fractions from 1. Chrys."""
    b = random.randint(2 + difficulty, 9 + difficulty)
    a_1 = random.randint(1, b - 2)
    a_2 = random.randint(1, b - a_1 - 1)
    fracs = [f"${mq.latex_frac(a_1, b)}$", f"${mq.latex_frac(a_2, b)}$"]

    n = random.randint(0, 2)
    item = ["tank of petrol", "pizza", "pocket money"][n]
    verb = ['used', 'eaten', 'spent'][n]

    i = random.randint(0, 1)
    name_1 = names.get_first_name(gender=["male", "female"][i])
    name_2 = names.get_first_name(gender=["male", "female"][(i + 1) % 2])
    pronoun = [["He", "his"], ["She", "her"]][i]

    question = [
        f"{name_1} has a full {item} in {pronoun[1]} car before "
        f"{pronoun[0].lower()} leaves for work. "
        f"{pronoun[0]} uses up {fracs[0]} of a tank on the journey to work. "
        f"On the way back, {pronoun[0].lower()} uses up another "
        f"{fracs[1]} of the tank.",

        f"{name_1} and {name_2} are sharing a {item}. {name_1} eats {fracs[0]}"
        f" of the pizza and {name_2} eats {fracs[1]} of it.",

        f"{name_1} is given some {item} for the weekend. "
        f"{pronoun[0]} spends {fracs[0]} of the money on Saturday "
        f"and spends {fracs[1]} of the money on Sunday. "
        ][n]

    k = random.randint(0, 1)
    question += [
        f" What fraction of the {item} is left?",
        f" In total, what fraction of the {item} has been {verb}?"
    ][k]
    result = [b - a_1 - a_2, a_1 + a_2][k]
    answer = f"${mq.latex_frac(result, b)}$"
    return [question, answer]


def fr_22(difficulty):
    """Worded subtraction question. Difference of two fractions. Chrys."""
    b = random.randint(2 + difficulty, 9 + difficulty)
    a_1 = random.randint(ceil(b / 2), b - 1)
    a_2 = random.randint(1, a_1 - 1)
    fracs = [f"${mq.latex_frac(a_1, b)}$", f"${mq.latex_frac(a_2, b)}$"]

    n = random.randint(0, 3)
    item = ["tank of fuel", "carton of milk", "questions", "marathon"][n]
    verb = ['used during the flight', 'used', 'correctly', 'completed'][n]

    i = random.randint(0, 1)
    gender = ["male", "female"]
    name_1 = names.get_first_name(gender=gender[i])
    name_2 = names.get_first_name(gender=gender[(i + 1) % 2])

    question = [
        f"An aeroplane is flying from London to New York. The plane began it's"
        f" journey with {fracs[0]} of a {item}. "
        f"By the end, it only had {fracs[1]} of a tank remaining.",

        f"At the start of the day, {name_1} has {fracs[0]} of a {item}. By "
        f"the end of the day, there is only {fracs[1]} of a carton left.",

        f"{name_1} and {name_2} are doing a test. {name_1} {verb} solves "
        f"{fracs[0]} of the {item}. {name_2} only answers {fracs[1]} of the "
        f"{item} {verb}.",

        f"{name_1} and {name_2} are running a {item}. "
        f"After {round(4 * (a_1 / b))} hours, {name_1} has {verb} {fracs[0]}"
        f" of the {item} whereas {name_2} has only {verb} {fracs[1]}."
    ][n]

    if n == 2 or n == 3:
        question += [
            f" What fraction of the questions did {name_1} "
            f"{verb} answer more than {name_2}?",

            f" How much more of the {item} has {name_1} "
            f"{verb} compared to {name_2}. Write your answer as a fraction."
        ][n % 2]
    else:
        question += f" What fraction of the {item} has been {verb}?"
    answer = f"${mq.latex_frac(a_1 - a_2, b)}$"
    return [question, answer]


def fr_23(difficulty):
    """Identify place of a digit in a decimal number. Chrys."""
    int_places = ["Ones", "Tens", "Hundreds"]
    dec_places = ["Tenths", "Hundredths", "Thousandths"]

    digits = random.sample(range(1, 9), difficulty * 2)
    integer = int(''.join(map(str, [digits[i] for i in range(difficulty)])))
    decimal = int(''.join(
        map(str, [digits[i] for i in range(difficulty, 2 * difficulty)]))
    )
    n = '.'.join(map(str, [integer, decimal]))

    k = random.randint(0, 1)
    value = [integer, decimal][k]
    d = random.randint(1, len(str(value)))
    question = f"What place is the digit {int(str(value)[- d])} " \
               f"in the number {mq.dollar(n)}?"
    choices = []
    for i in range(difficulty):
        choices.append(int_places[i])
    for j in reversed(range(difficulty)):
        choices.append(dec_places[j])

    answer = choices[(difficulty * k) + d - 1]
    return mq.multiple_choice(question, choices, answer)


def fr_24(difficulty):
    """Identify fraction from number line. Chrys."""
    b = random.randint(1 + difficulty, 3 + 2 ** difficulty)
    a = random.randint(1, b - 1)
    length = 7
    marker = r'''\fill [shift={(%d * %f/%d, 7pt)}, color=red] (0,0) -- 
    (0.2cm, 0.4cm) -- (-0.2cm, 0.4cm) -- cycle;
    ''' % (a, length, b)
    question = "What fraction is shown on the number line?"
    if mq.gcd(b, a) != 1:
        question += " Simplify your answer."
    answer = f"${mq.latex_frac_simplify(a, b)}$"
    question += "\n\n" + mq.num_line(b, marker, length=length)
    return [question, answer]


def fr_25(difficulty):
    """Identifying fraction lengths on number line. Multiple choice. Chrys."""
    b = random.sample(range(3 + difficulty, 8 + 2 ** (difficulty-1)), k=2)
    a = random.sample(range(1, b[0] - 1), k=2)
    length = 6
    values = [a[0] / b[0], a[1] / b[0]]

    choices = []
    for i in range(2):
        start = random.randint(0, b[0] - a[i])
        line = r'''
        \draw[line width = 2pt, color=red](%s,0) -- (%s,0);
        ''' % (start * (length / b[0]), (start + a[i]) * (length / b[0]))
        choices.append(
            f"{mq.num_line(b[0], line, length)} \\vspace{{2em}}")

    while len(choices) < 3:
        c = random.randint(1, b[1] - 1)
        if c/b[1] not in values:
            start = random.randint(0, b[1] - c)
            line = r''' 
            \draw[line width = 2pt, color=red] (%s,0) -- (%s,0);
            ''' % (start * (length / b[1]), (start + c) * (length / b[1]))
            choices.append(f"{mq.num_line(b[1], line, length)} "
                           f"\\vspace{{2em}}")

    question = "Which number line has a coloured segment of length " \
               f"${mq.latex_frac(a[0],b[0])}$?"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer)

# MONEY QUESTIONS______________________


def me_1(difficulty):
    """
    Money question, subtracting a value from a starting amount. Chrys.
    """
    y0 = random.randint(2, round(0.5 * difficulty) + 5)
    if difficulty == 2:
        d_p = 1
    else:
        d_p = 2
    x = round(random.uniform(0.1 * y0, 2 * y0 / 3), d_p)
    question = f"{names.get_first_name(gender='female')} has " \
               f"\\pounds {y0:.2f} in pocket money. " \
               f"She spends \\pounds {x:.2f}. " \
               f"How much money does she have left over?"
    answer = f"\\pounds {round(y0 - x, 2):.2f}"
    return [question, answer]

# CLOCK QUESTIONS______________________


def me_2(difficulty):
    """ Convert 24hr into 12hr clock and vice versa. Chrys."""
    h = random.choices([random.randint(0, 12), random.randint(12, 23)],
                       weights=(1.5, difficulty), k=1)[0]
    m = random.randint(0, 59)
    n = random.randint(0, 1)
    t = [
        time(h, m).strftime("%H:%M"),
        time(h, m).strftime("%I:%M %p")
    ]
    question = f"Convert {t[n]} into {['12', '24'][n]} hour format."
    answer = t[(n+1) % 2]
    return [question, answer]


def me_3(difficulty):
    """How many minutes is between two 24hr times t1 and t2? Chrys."""
    if difficulty == 1:
        h1, m1 = random.randint(1, 11), 5*random.randint(0, 4)
        h2, m2 = h1, m1+15+5*random.randint(0, 4)
    elif difficulty == 2:
        h1, m1 = random.randint(1, 23), random.randint(1, 19)
        h2, m2 = h1, random.randint(m1+17, 59)
    else:
        h1, m1 = random.randint(1, 22), random.randint(10, 58)
        choice = random.choice([
            [(h1 + 1), random.randint(0, m1 - 1)],
            [(h1 + 1), random.randint(m1 + 1, 59)]
        ])
        h2, m2 = choice[0], choice[1]

    d1 = timedelta(hours=h1, minutes=m1)
    d2 = timedelta(hours=h2, minutes=m2)

    question = "How many minutes after " \
               + time(h1, m1).strftime("%H:%M") \
               + " do we have to wait until it is " \
               + time(h2, m2).strftime("%H:%M") + "?"
    answer = str(int(abs((d2-d1).total_seconds())/60)) + " minutes"
    return [question, answer]


def me_4(difficulty):
    """
    Find how long someone was doing an activity, answer in hrs & mins. Chrys.
    """
    activity = random.choice(['studying', 'reading', 'walking', 'painting',
                              'drawing', 'gardening'])

    n = random.randint(0, 1)
    gender = ['Male', 'Female'][n]
    name = names.get_first_name(gender=gender)
    hour_start = random.randint(5, 22)
    if difficulty == 3:
        min_start = (20 - 5 * difficulty) * random.randint(0, 11)
        time_elapsed = random.choice([
            [0, 5 * random.randint(3, 11)],
            [1, 5 * random.randint(0, 6)],
            [2, 10 * random.randint(0, 3)]
        ])
    else:
        min_start = (15 - 5 * difficulty) * random.randint(0,
                                                           5 * difficulty - 1)
        if difficulty == 2:
            time_elapsed = random.choice([
                [0, 5 * random.randint(3, 11)],
                [1, 10 * random.randint(0, 3)]
            ])
        else:
            time_elapsed = [0, 5 * random.randint(3, 11)]

    start_time = datetime(year=2021, month=6, day=20,
                          hour=hour_start, minute=min_start)
    end_time = start_time + timedelta(hours=time_elapsed[0],
                                      minutes=time_elapsed[1])
    format_time = random.choice([
        [start_time.strftime("%H:%M"), end_time.strftime("%H:%M")],
        [start_time.strftime("%I:%M %p"), end_time.strftime("%I:%M %p")]
    ])

    question = f" {name} starts {activity} at {format_time[0]}." \
               f" At {format_time[1]} {['he', 'she'][n]} stops for a break. " \
               f"In total, how long has {['he', 'she'][n]} " \
               f"been {activity} for?\\ \\\n\n"

    if time_elapsed[0] == 0:
        answer = f"{time_elapsed[1]} minutes."
        question += r'\begin{center} \makebox[0.04\textwidth]{\hrulefill}' \
                    r' minutes \end{center}'
    else:
        answer = f"{time_elapsed[0]} hours and {time_elapsed[1]} minutes."
        question += r'\begin{center} \makebox[0.04\textwidth]{\hrulefill} ' \
                    r' hours and \hspace{0.1em} ' \
                    r'\makebox[0.04\textwidth]{\hrulefill} minutes ' \
                    r'\end{center}'
    return [question, answer]


def me_5(difficulty):
    """Converting units of clock measurements, e.g. 1 week in days. Chrys."""
    units = ['months', 'weeks', 'days', 'hours', 'minutes', 'seconds']
    unit_out = random.choice(units)

    unit_in = ""
    if unit_out == units[0]:
        unit_in = 'year'
    elif unit_out == units[1]:
        unit_in = random.choices(
            ['year', 'month'], weights=(difficulty, 1), k=1)[0]
    elif unit_out == units[2]:
        unit_in = random.choices(
            ['year', 'week'], weights=(difficulty, 1), k=1)[0]
    elif unit_out == units[3]:
        unit_in = random.choices(
            ['week', 'day'], weights=(difficulty, 1), k=1)[0]
    elif unit_out == units[4]:
        unit_in = random.choices(
            ['hour', 'day'], weights=(1, difficulty), k=1)[0]
    elif unit_out == units[5]:
        unit_in = random.choices(
            ['hour', 'minute'], weights=(difficulty, 1), k=1)[0]

    if unit_in == 'hour':
        prefix = 'an'
    else:
        prefix = 'a'

    result = mq.time_unit_converter(1, unit_in, unit_out)
    question = f"How many {unit_out} are there in {prefix} {unit_in}?"
    answer = str(result[0]) + result[1]
    return [question, answer]


def me_6(difficulty):
    """
    Select the correct time in words from a 24hr clock, multiple choice. Chrys.
    """
    sample = random.sample(range(0, 11), 3)
    minutes = [5 * i for i in sample]
    hours = random.choices([
        random.sample(range(2, 12), 2),
        random.sample(range(13, 22), 2)
    ],
        weights=(1, difficulty), k=1)[0]
    time_in = [hours[0], minutes[0]]
    question = "Which of the following is equivalent to " \
               f"{time(time_in[0], time_in[1]).strftime('%H:%M')}?"
    choices = []

    if time_in[1] <= 30:
        hour_1 = (time_in[0] + 1)
    else:
        hour_1 = (time_in[0] - 1)
    choice1 = mq.time_to_words(hour_1 % 12, time_in[1])

    if time_in[1] == 0:
        difference = random.choice([1, -1])
        time_2 = [time_in[0] + difference, time_in[1]]
    elif time_in[1] == 45 or time_in[1] == 15:
        difference = random.choice([1, 0])
        time_2 = [(time_in[0] + difference), (time_in[1] + 30) % 60]
    else:
        time_2 = [hours[1], minutes[2]]
    choice2 = mq.time_to_words(time_2[0] % 12, time_2[1])
    choice3 = mq.time_to_words(time_in[1] % 12, time_in[0])

    answer = mq.time_to_words(time_in[0] % 12, time_in[1])
    choices.extend([choice1, choice2, choice3, answer])
    return mq.multiple_choice(question, choices, answer)


def me_7(difficulty):
    """"
    Multiple choice, converting time in words to a 12hr or 24hr clock. Chrys.
    """
    minutes = random.sample(range(0, 59), 5)
    hour = random.choices([random.randint(1, 11), random.randint(12, 23)],
                          weights=(1, difficulty), k=1
                          )[0]
    n = random.randint(0, 1)
    clock_format = ['24 hour', '12 hour'][n]
    if 0 < hour < 12:
        morn_eve = 'in the morning'
    elif 12 <= hour < 17:
        morn_eve = 'in the afternoon'
    elif 17 < hour < 21:
        morn_eve = 'in the evening'
    else:
        morn_eve = 'at night'

    question = f'What is {mq.time_to_words(hour % 12, minutes[0])} ' \
               f'{morn_eve} in {clock_format} format.'
    choices = []
    time_out = time(hour, minutes[0])

    for i in range(1, 3):
        choice1 = [
            (time(hour, minutes[i])).strftime("%H:%M"),
            (time(hour, minutes[i])).strftime("%I:%M %p")
        ][n]
        choices.append(choice1)

    if minutes[0] > 30:
        choice2 = time(hour + 1, 60 - minutes[0])
    elif minutes[0] == 30 or minutes[0] == 0:
        choice2 = time(hour + 1, minutes[4])
    else:
        choice2 = time(hour, 60 - minutes[0])
    choice2 = [choice2.strftime("%H:%M"), choice2.strftime("%I:%M %p")][n]

    h_3 = (round(minutes[0] * 0.2)) % [24, 12][n]
    m_3 = ((hour % 12) * 5) % 60
    choice3 = [
        time(h_3, m_3).strftime("%H:%M"),
        time(h_3, m_3).strftime("%I:%M %p")
    ][n]

    answer = [time_out.strftime("%H:%M"), time_out.strftime("%I:%M %p")][n]
    choices.extend([choice2, choice3, answer])
    return mq.multiple_choice(question, choices, answer)


def me_8(difficulty):
    """
    Simple elapsed time question with mix of time in words and digits. Chrys.
    """
    h1 = random.randint(0, 22)
    if difficulty == 3:
        m1 = 5 * random.randint(0, 9)
        minutes_add = random.randint(10, 45)
    else:
        m1 = 5 * random.randint(2, round((11 / 2) * difficulty))
        minutes_add = 5 * random.randint(1 + difficulty, 6)

    time1 = time(h1, m1).strftime("%H:%M")
    delta1 = timedelta(hours=h1, minutes=m1)
    delta2 = timedelta(minutes=minutes_add)
    delta = (delta1 + delta2).total_seconds()

    hour_out = floor(delta / (60 * 60) % 24)
    min_out = floor((delta % (60 * 60)) / 60)
    answer = random.choice([time(hour_out, min_out).strftime("%H:%M"),
                            mq.time_to_words(hour_out % 12, min_out)
                            ])

    words_or_number = random.choice([
        [time1, num2words(minutes_add)],
        [mq.time_to_words(h1 % 12, m1), minutes_add],
        [time1, minutes_add]
    ])
    choices = []
    mins_sample_1 = random.sample(range(min_out-20, min_out-1), k=3)
    mins_sample_2 = random.sample(range(min_out+1, min_out-20+30), k=3)
    for i in range(3):
        m_2 = random.choice([mins_sample_1[i], mins_sample_2[i]])
        choice2 = random.choice([time(hour_out, m_2 % 60).strftime("%H:%M"),
                                 mq.time_to_words(hour_out % 12, m_2 % 60)
                                 ])
        choices.append(choice2)
    ch1 = random.choice([(hour_out + 1) % 24, (hour_out - 1) % 24])
    cm1 = random.randint(0, 59)
    choice1 = random.choice([time(ch1, cm1).strftime("%H:%M"),
                             mq.time_to_words(ch1 % 12, cm1)
                             ])
    choices = choices + [choice1, answer]
    question = f"The time is {words_or_number[0]}, " \
               f"what time will it be in {words_or_number[1]} minutes?"
    return mq.multiple_choice(question, choices, answer)


def me_9(difficulty):
    """elapsed time question, mixture of 12hr, 24hr and worded format. Chrys"""
    n = random.randint(0, 1)
    gender = ['Female', 'Male'][n]
    name = names.get_first_name(gender=gender)
    sport = random.choice(['runs', 'jogs', 'swims', 'does gymnastics',
                           'plays basketball', 'plays table tennis'])

    hour_start = random.randint(3, 22)
    if difficulty == 3:
        min_start = (20 - 5 * difficulty) * random.randint(0, 11)
        time_elapsed = random.randint(15, 45)
    else:
        min_start = (15 - 5 * difficulty) * random.randint(0, 5*difficulty - 1)
        time_elapsed = 5 * random.randint(3, 3 + 3 * difficulty)

    start_time = datetime(year=2021, month=6, day=20, hour=hour_start,
                          minute=min_start)
    end_time = start_time + timedelta(minutes=time_elapsed)

    format_time = random.choice([
        [start_time.strftime("%H:%M"), end_time.strftime("%H:%M")],
        [start_time.strftime("%I:%M %p"), end_time.strftime("%I:%M %p")]
    ])
    question = f" {name} wants to do some exercise. The time is " \
               f"{format_time[0]}. {['She', 'He'][n]} {sport} for " \
               f"{time_elapsed} minutes. What time is it now?"
    answer = format_time[1]
    return [question, answer]


def me_10(difficulty):
    """
    AM/PM question where student picks correct time from multiple choice. Chrys
    """
    if difficulty == 3:
        time_in = [random.randint(0, 23), 5 * random.randint(0, 11)]
    else:
        time_in = [
            random.randint(0, 23),
            (20 - 5 * difficulty) * random.randint(0, 1 + 2*difficulty)
        ]

    time_24hr = datetime(year=2021, month=6, day=20,
                         hour=time_in[0], minute=time_in[1])
    if time_in[0] < 12:
        morn_eve = ['in the morning', 'morning', 'afternoon']
    elif 12 <= time_in[0] < 17:
        morn_eve = ['in the afternoon', 'afternoon', 'morning']
    elif 17 <= time_in[0] < 20:
        morn_eve = ['in the evening', 'evening', 'morning']
    else:
        morn_eve = ['at night', 'night', 'morning']

    time_format = time_24hr.strftime("%H:%M")
    n = random.choices([0, 1, 2], weights=(1, 4, 2), k=1)[0]
    num_or_words = [
        [mq.time_to_words(time_in[0] % 12, time_in[1]), morn_eve[0]],
        [time_format, ''],
        [mq.time_to_words(time_in[0] % 12, time_in[1]), morn_eve[0]]
    ][n]
    question = f"John looks at his clock, " \
               f"it is {num_or_words[0]} {num_or_words[1]}. "
    question += ['What is the time in 12 hour format?',
                 'What time of the day is it?',
                 'What is the time in 24 hour format?'
                 ][n]
    answer = [time_24hr.strftime("%I:%M %p"), morn_eve[1], time_format][n]
    choice_1 = time_24hr + timedelta(hours=12)
    choices = [[choice_1.strftime("%I:%M %p"),
                morn_eve[2], choice_1.strftime("%H:%M")
                ][n],
               answer]
    if n == 0 or n == 2:
        choice_2 = [
            datetime(year=2021, month=6, day=20, hour=(time_in[0] + 6) % 24,
                     minute=time_in[0]).strftime("%I:%M %p"),
            '',
            time(time_in[1] % 12, time_in[0]).strftime("%H:%M")
        ][n]
        choices.append(choice_2)
    return mq.multiple_choice(question, choices, answer)


def me_11(difficulty):
    """ Converting analogue clock to digital times or worded time. Chrys."""
    hour = random.randint(0, 11)
    minute = ((20-5*difficulty)*random.randint(0, 11)) % 60
    choice = random.choice([
        ['In 12 hour format', time(hour, minute).strftime("%H:%M")],
        ['Using words', mq.time_to_words(hour % 12, minute)]
    ])
    question = f"{choice[0]}, write down the time shown on the clock.\n\n " \
               f"\\begin{{center}}\n {mq.analogue_clock(hour, minute)}" \
               f"\\end{{center}}"
    answer = choice[1]
    return [question, answer]


def me_12(difficulty):
    """
    Multiple choice, converting analogue to digital clock and vice versa. Chrys
    """
    hour = random.randint(0, 12)
    sample = random.sample(range(0, 11), 6)
    minute = [(x * (20 - 5 * difficulty)) % 60 for x in sample]

    for k in range(1, 6):
        if minute[k] == minute[0]:
            minute[k] = (minute[k] + 5) % 60
        for j in range(1, 6):
            if minute[j] == minute[k]:
                minute[j] = (minute[k] + 13) % 60

    time_in = random.choice([
        mq.time_to_words(hour % 12, minute[0]),
        time(hour, minute[0]).strftime("%I:%M")
    ])

    n = random.randint(0, 1)
    choices = []
    if n == 0:
        question = f"Choose the clock that shows {time_in}."
        if minute[0] <= 30:
            difference = 1
        else:
            difference = -1
        choice1 = mq.analogue_clock((hour + difference) % 12, minute[0], False)
        choice2 = mq.analogue_clock(minute[0] / 5, (5*hour) % 60, False)
        choice3 = mq.analogue_clock(
            hour, (minute[0] + 5 * random.randint(1, 11)) % 60, center=False)
    else:
        question = f"What is the correct time, in 12 hour format, " \
                   f"that is shown on the clock?\n\n" \
                   f"\n {mq.analogue_clock(hour, minute[0])}"
        for j in range(1):
            choice4 = time(hour,
                           (minute[0] + 5*sample[j]) % 60).strftime("%I:%M")
            choices.append(choice4)
        choice2 = time(round(minute[0] / 5), (5*hour) % 60).strftime("%I:%M")
        choice3 = time(
            hour + 1,
            (minute[0] + 5 * sample[3]) % 60).strftime("%I:%M")

        difference = random.choice([1, -1])
        choice1 = time((hour + difference) % 12, minute[0]).strftime("%I:%M")

    answer = [
        mq.analogue_clock(hour, minute[0], center=False),
        time(hour, minute[0]).strftime("%I:%M")
    ][n]
    choices.extend([answer, choice1, choice2, choice3])
    return mq.multiple_choice(question, choices, answer)


def me_13(difficulty):
    """Draw on clock to get time. Chrys."""
    hour = random.randint(0, 11)
    minute = ((20-5*difficulty) * random.randint(0, 11)) % 60
    time_in = random.choice([
        time(hour, minute).strftime("%H:%M"),
        mq.time_to_words(hour % 12, minute)
    ])
    blank_clock = r'''
    \begin{center} 
    \begin{tikzpicture} [line cap=rect,line width=3pt]
    \filldraw [fill=white] (0,0) circle [radius=1.3cm]; 
    \foreach \angle [count=\xi] in {60,30,...,-270} 
      { \draw[line width=1pt] (\angle:1.15cm) -- (\angle:1.3cm);
      \node[font=\large] at (\angle:0.9cm) {\textsf{\xi}};}
    \foreach \angle in {0,90,180,270}
      \draw[line width=1.5pt] (\angle:1.1cm) -- (\angle:1.3cm);
    \end{tikzpicture}
    \end{center}
    '''
    question = f"Draw the time {time_in} on the clock.\n\n {blank_clock}"
    answer = mq.analogue_clock(hour, minute)
    return [question, answer]


def me_14(difficulty):
    """Elapsed time question using analogue clock. Chrys. """
    hour_in = random.randint(0, 11)
    minute_in = ((20-5*difficulty) * random.randint(0, 11)) % 60

    if difficulty == 3:
        time_elapsed = random.choice([5 * random.randint(4, 12),
                                      random.randint(10, 30)])
    else:
        time_elapsed = (10/difficulty)*random.randint(2*difficulty,
                                                      7*difficulty-2)

    result = datetime(year=2021, month=6, day=20,
                      hour=hour_in, minute=minute_in) \
        + timedelta(minutes=time_elapsed)

    time_elapsed_format = random.choice([num2words(time_elapsed),
                                         int(time_elapsed)])
    answer_format = random.choice([
        ["in 12 hour format", result.strftime("%I:%M")],
        [
            "using words",
            mq.time_to_words(
                int(hour_in + floor((minute_in + time_elapsed)/60)) % 12,
                int((minute_in + time_elapsed) % 60))
        ]
    ])
    question = f"Using the clock, find what time it will be in " \
               f"{time_elapsed_format} minutes? Write this down " \
               f"{answer_format[0]}.\n\n " \
               f"\\begin{{center}}\n " \
               f"{mq.analogue_clock(int(hour_in), int(minute_in))}" \
               f"\\end{{center}}\n "
    answer = answer_format[1]
    return [question, answer]


def me_15(difficulty):
    """ Time sequence question where student fills missing time. Chrys."""
    h_0 = random.randint(0, 23)
    m_0 = ((20 - 5 * difficulty) * random.randint(0, 11)) % 60
    t_0 = datetime(year=2021, month=6, day=20, hour=h_0, minute=m_0)

    steps = [5 * random.randint(2, 6),
             10 * random.randint(1, 3),
             15 * random.randint(1, 2), 60
             ]
    if difficulty == 3:
        step = random.choices(steps, weights=(50, 0, 0, 10), k=1)
    else:
        step = random.choices(steps, weights=(-10 + 10 * difficulty,
                                              50, 40, 10 / difficulty), k=1)

    times = []
    k = random.randint(0, 1)
    for i in range(5):
        times_formats = [
            (t_0 + timedelta(minutes=i * step[0])).strftime("%H:%M"),
            (t_0 + timedelta(minutes=i * step[0])).strftime("%I:%M")
        ][k]
        times.append(times_formats)

    n = random.randint(0, 4)
    answer = times[n]
    times[n] = "\\makebox[0.025\\textwidth]{\\hrulefill}"
    times = ",\\ ".join(times)
    question = f"Fill in the missing time in the sequence: \n\n {times} "
    return [question, answer]


def sh_1(difficulty):
    """Guess the shape, multiple choice. Chrys."""
    upper = [5, 7, 10][difficulty - 1]
    n = random.randint(3, upper)
    if n == 9:
        n = n - 1
    shapes_dict = {3: 'Triangle', 4: 'Square', 5: 'Pentagon',
                   6: 'Hexagon', 7: 'Heptagon', 8: 'Octagon',
                   9: 'Octagon', 10: 'Decagon'}
    shape = "\\begin{center}\n\\begin{tikzpicture}\n\\node[regular polygon, " \
            f"regular polygon sides={n}, minimum size=2cm, draw] at (0," \
            "0) {};\n\\end{tikzpicture}\n\\end{center}"
    question = "What is the name of the shape below?\n\n" \
               + shape
    choices = []
    answer = shapes_dict[n]
    choices.append(answer)

    while len(choices) < 3:
        k = random.randint(3, upper)
        if shapes_dict[k] not in choices:
            choices.append(shapes_dict[k])
    return mq.multiple_choice(question, choices, answer)


def pd_1(difficulty):
    """What type of transformation is occurring. Chrys."""
    size = 6
    n = random.randint(0, 2)
    name = [
        "isosceles triangle",
        "regular polygon,regular polygon sides=5",
        "circle split"
    ][n]
    rotate = [[0, 180], [270, 90], [45, 135]][n]

    k = random.randint(0, 1)
    shape = r'node[%s, minimum size=1cm, rotate=%s, draw, fill=green] {}' \
            % (name, rotate[k])
    reflection = r'node[%s, minimum size=1cm, rotate=%s, draw,fill=green] {}' \
                 % (name, rotate[(k + 1) % 2])

    lower_x = [[1, 4], [0.5, 3.5], [0.5, 3.5]][n]
    upper_x = [[2, 5], [2.5, 4.5], [2.5, 4.5]][n]

    x_0 = 0.5 * random.randint(lower_x[0] * 2, upper_x[0] * 2)
    y_0 = 0.5 * random.randint(1, 5)

    m = random.randint(0, 1)
    if m == 1:
        x_1 = size - x_0
        y_1 = y_0
    else:
        x_1 = random.uniform(lower_x[1], upper_x[1])
        y_1 = random.uniform(0.5, 2.5)

    pic = r'''
    \begin{tikzpicture} \usetikzlibrary{shapes,snakes}
    \draw[step=0.5,gray,thin] (0,0) grid (%s,3);
    \draw (%s,%s) %s; 
    \draw (%s, %s) %s;"
    ''' % (size, x_0, y_0, shape, x_1, y_1, [shape, reflection][m])

    if difficulty == 1:
        pic += r'\draw [ultra thick,red] (3,0) -- (3,3);'
    pic += r'\end{tikzpicture}'

    question = f"What transformation has occurred? \n\n {pic}"
    choices = ["Translation", "Reflection"]
    answer = choices[m]
    return mq.multiple_choice(question, choices, answer)


def st_1(difficulty):
    """Mean of a group of numbers. Chrys."""
    upper = 10 ** difficulty - 1 - 800 * round(difficulty / 10 + 0.3)
    nums = []
    while len(nums) == 0:
        k = random.randint(5, 10 - difficulty)
        values = random.choices(range(0, upper), k=k)
        if sum(values) % k == 0:
            nums = values

    sequence = ",\\ ".join(str(nums[i]) for i in range(len(nums)))
    question = f"Find the mean of the following numbers. \n\n {sequence}"
    answer = f"{mean(nums)}"
    return [question, answer]


def fr_26(difficulty):
    """Money addition/ subtraction using columnar method. Chrys."""
    limit = 2 * difficulty
    a = round(random.uniform(0.51, limit), 2)
    b = round(random.uniform(limit, limit * 2), 2)

    n = random.randint(0, 1)
    result = [b + a, b - a][n]
    op = ['+', '-'][n]
    question = r'''
    \hspace{2cm}{\LARGE$\begin{array}{r} 
    \pounds %s \\ \underline{%s \ \pounds %s} \\ 
    \underline{\phantom{%s \ \pounds %s}}
    \end{array}$} 
    \\ \\ \vspace{1.2ex}
    ''' % (f'{b:.2f}', op, f'{a:.2f}', op, f'{a:.2f}')
    answer = f'\\pounds {result:.2f}'
    return [question, answer]


def fr_27(difficulty):
    """Money subtraction with three numbers. Chrys."""
    limit = 1 + difficulty
    a = round(random.uniform(0.51, limit), 2)
    b = round(random.uniform(1, limit), 1)
    c = round(random.uniform(round(a + b) + 1, 10), difficulty - 1)
    question = r"%s $-$ %s $-$ %s = ?" % (f'{c:.2f}',  f'{b:.2f}', f'{a:.2f}')
    result = c - b - a
    answer = f"\\pounds {result:.2f}"
    return [question, answer]


def as_15(difficulty):
    """mixed operations. Chrys."""
    lower = 10 ** difficulty
    upper = 10 ** (difficulty + 1)
    a = random.randint(lower, upper / 2)
    b = random.randint(lower, upper / 2)
    c = a + b

    n = random.randint(0, 1)
    k = (n + 1) % 2
    op = ['$+$', '$-$']
    values = [((-1) ** n) * a, ((-1) ** k) * b]
    question = r"%s %s %s %s %s = ?" % (c, op[n], a, op[k], b)
    answer = mq.dollar(c + values[0] + values[1])
    return [question, answer]


def fr_28(difficulty):
    """Money question: difference between starting and ending value. Chrys."""
    start_value = round(
        random.uniform(3 * difficulty, 5 * difficulty), difficulty - 1)
    d_p = [1, 1, 2][difficulty - 1]
    end_value = round(random.uniform(1, 2 * difficulty), d_p)

    item = random.choice(["food from a cafe",
                          "items from the shop",
                          "a book"
                          ])
    n = random.randint(0, 1)
    gender = [names.get_first_name(gender='Male'),
              names.get_first_name(gender='Female')][n]
    pronoun = ['He', 'She'][n]
    name = names.get_first_name(gender=gender)

    question = f"{name} has \\pounds{start_value:.2f} in pocket money. " \
               f"{pronoun} decides to buy {item}. Afterwards, " \
               f"{pronoun.lower()} has \\pounds{end_value:.2f} left over. " \
               f"How much did {name} spend in total?"
    result = start_value - end_value
    answer = f"\\pounds{result:.2f}"
    return [question, answer]


def me_16(difficulty):
    """Money question: number to words and vice versa. Chrys."""
    pounds = random.randint(2 * difficulty, 9 * difficulty)
    pence = random.randint(1, 99)
    total = pounds + (pence / 100)
    n = random.randint(0, 1)
    num_words = [f"{num2words(pounds)} pounds and {num2words(pence)} pence",
                 f"\\pounds{total:.2f}"
                 ]
    question = f"Write down {num_words[n]} {['in numbers',' in words'][n]}."
    answer = num_words[(n + 1) % 2]
    return [question, answer]


def me_17(difficulty):
    """Money question: sum of change in coins. Chrys."""
    nums = random.choices(range(1, 3), k=2+difficulty)
    choices = random.sample(range(0, 9), k=2+difficulty)
    choices = sorted(choices)
    my_list = [
        [10, ' ten pound note'],
        [5, ' five pound note'],
        [2, ' two pound coin'],
        [1, ' one pound coin'],
        [0.5, ' fifty pence coin'],
        [0.2, ' twenty pence coin'],
        [0.1, ' ten pence coin'],
        [0.05, ' five pence coin'],
        [0.02, ' two pence coin'],
        [0.01, ' penny'],
    ]
    amount = []
    sums = []
    for i in range(len(choices)):
        if choices[i] == 9 and nums[i] > 1:
            my_list[9][1] = ' pennies'
        elif choices[i] < 9 and nums[i] > 1:
            my_list[choices[i]][1] += 's'

        a = str(nums[i]) + my_list[choices[i]][1]
        amount.append(a)
        sums.append(nums[i] * my_list[choices[i]][0])

    amount_format = ",\\ ".join([amount[i] for i in range(len(amount) - 1)]) \
                    + f" and {amount[len(amount) - 1]}"

    n = random.randint(0, 1)
    name = [
        [names.get_first_name(gender='Male'), 'he'],
        [names.get_first_name(gender='Female'), 'she']
    ][n]

    question = f"{name[0]} has {amount_format}. How much money does " \
               f"{name[1]} have in total?"
    answer = f"\\pounds{sum(sums):.2f}"
    return [question, answer]


def sh_2(difficulty):
    """Decide whether angle is obtuse, acute or right angle. Chrys."""
    angle = random.choices([
        random.randint(20, 60), 90, random.randint(110, 160)],
        weights=(4, 4 - difficulty, 4), k=2)[0]

    x_angle = 90 * random.randint(0, difficulty)
    drawing = mq.angle_drawing(x_angle, x_angle - angle, 4)
    question = "Which of the following best describes the angle? \n\n" \
               r"\begin{center} %s \end{center}" % drawing
    choices = ["Acute", "Obtuse", "Right angle"]
    if angle < 90:
        answer = choices[0]
    elif angle > 90:
        answer = choices[1]
    else:
        answer = choices[2]
    return mq.multiple_choice(question, choices, answer)


def st_2(difficulty):
    """Range of a group of numbers. Chrys."""
    lower = 10 ** (difficulty - 1) - 1
    upper = 10 ** (difficulty + 1) - 1
    k = random.randint(5, 9 - difficulty)
    nums = random.sample(range(lower, upper), k=k)

    sequence = ",\\ ".join(str(i) for i in nums)
    question = "Find the range of the following numbers. \n\n " \
               f"\\begin{{center}} {sequence} \\end{{center}}"
    answer = mq.dollar(max(nums) - min(nums))
    return [question, answer]


def st_3(difficulty):
    """Find the range using data from a table. Chrys."""
    lower = 10 ** (difficulty + 1)
    upper = 10 ** (difficulty + 2) - 1
    nums = random.sample(range(lower, upper), k=5)

    n = random.randint(0, 2)
    city = ['New Central', 'Snowy Capital', 'Artemisia', 'Old Town', 'Aegina']
    title = ['Population', 'Bicycle Journeys', 'Number of Tourists'][n]
    values = [
        ['the populations of'],
        ['amount of bicycles journeys made in'],
        ['the number of tourists visiting']
    ][n][0]
    place = [['Town', 'towns'], ['City', 'cities']][round(difficulty/3)]

    table = [[place[0], title]]
    for i in range(len(nums)):
        table.append([city[i], str(nums[i])])

    question = f"Here is some data on the {values} some {place[1]}. " \
               "What is the range of the data? \n\n " \
               f"\\begin{{center}} {mq.draw_table(table)} \\end{{center}}"
    answer = mq.dollar(max(nums) - min(nums))
    return [question, answer]


def fr_29(difficulty):
    """Money question: Price of combination of items from table. Chrys."""
    my_list = [['Item', 'Price']]
    n = random.randint(0, 2)
    place = ['cafe', 'supermarket', 'sports shop']
    items = [
        ['Coffee', 'Tea', 'Cookie', 'Cake'],
        ['Pear', 'Milk', 'Juice', 'Cabbage'],
        ['Football', 'Bottle', 'Tennis Racket', 'Sports Shirt']
    ][n]
    price = []
    boundaries = [
        [[2.5, 3.2], [1.5, 2], [1, 1.30], [3.7, 4.8]],
        [[0.6, 0.7], [1, 1.30], [0.90, 1.5], [0.50, 0.71]],
        [[13, 25], [3.5, 7], [50, 90], [20, 40]]
    ][n]
    for i in range(4):
        price.append(random.uniform(boundaries[i][1], boundaries[i][0]))

    for j in range(len(items)):
        my_list.append([items[j], f"\\pounds{price[j]:.2f}"])
    table = mq.draw_table(my_list)

    choice_list = []
    value = []
    limit = random.randint(2, 3)
    choice = random.sample(range(0, 3), k=limit)
    quantity = random.choices(
        (1, 2), weights=(difficulty, difficulty - 1), k=limit)

    for m in range(len(choice)):
        if quantity[m] == 1:
            amount = 'a'
        else:
            amount = quantity[m]
            items[choice[m]] += 's'
        choice_list.append(f"{amount} {items[choice[m]].lower()}")
        value.append(quantity[m] * price[choice[m]])

    spend = ",\\ ".join([choice_list[i] for i in range(len(choice_list) - 1)])
    spend += f" and {choice_list[len(choice_list) - 1]}"

    k = random.randint(0, 1)
    name = [names.get_first_name(gender='Male'),
            names.get_first_name(gender='Female')][k]

    question = f"Here are the prices for some items at at a {place[n]}. " \
               f"\n\n {table} \n\n {name} buys {spend}. " \
               f"How much will {['he', 'she'][k]} have to pay in total?"
    answer = f"\\pounds{sum(value):.2f}"
    return [question, answer]


def st_4(difficulty):
    """Probability question, chance of selecting a specified shape. Chrys."""
    r = 'r'
    shapes = []
    choices = ['Circle', 'Square',
               'Equally Likely']

    if difficulty == 3:
        quant_1 = random.choices(range(1, 2), k=2)
        quant_1.append(max(quant_1) + 1)
        shuffle(quant_1)
        a = random.randint(1, 2)
        quant = random.choices((quant_1, [a, a, a]), weights=(5, 1))[0]
        choices.append('Triangle')
    else:
        quant = random.choices(range(1, 1 + difficulty), k=2)
        quant.append(0)

    for i in range(quant[0] + quant[1] + quant[2]):
        r += 'r'
    for j in range(quant[0]):
        shapes.append(mq.draw_circle())
    for m in range(quant[1]):
        shapes.append(mq.draw_square())
    for k in range(quant[2]):
        shapes.append(mq.draw_triangle())
    shuffle(shapes)

    n = quant[0] + quant[1] + quant[2]
    joined_shapes = '&'.join(map(str, [shapes[i] for i in range(n)]))

    model = r'''
    \begin{center}
    {\arraycolsep=2pt\LARGE$\begin{array}{%s} %s \end{array}$} 
    \end{center}
    ''' % (r, joined_shapes)

    if quant[1] < quant[0] and quant[0] > quant[2]:
        answer = choices[0]
    elif quant[0] < quant[1] and quant[1] > quant[2]:
        answer = choices[1]
    elif quant[0] < quant[2] and quant[2] > quant[1]:
        answer = choices[3]
    else:
        answer = choices[2]

    question = "If we were to select one of these shapes at random, " \
               f"which one are we most likely to choose? \n\n {model}"
    return mq.multiple_choice(question, choices, answer)


def st_5(difficulty):
    """Find the mean using data from a table. Chrys."""
    lower = 10 * difficulty
    upper = 2 ** (5 + difficulty)
    values = []
    while len(values) < 4:
        sample = random.sample(range(lower, upper), k=4)
        if sum(sample) % 4 == 0:
            values = sample

    n = random.randint(0, 1)
    items = ["number of cars sold", "number of computers sold"][n]
    shop_type = ["Car Dealerships", "Electronics Stores"][n]
    shop_name = [
        ["Cars for All", "Car City", "United Motors", "Rocket Cars"],
        ["Tech Central", "Turing's Computers",
         "Faraday's Electrics", "Master Tech"]
    ][n]

    data = [[["Dealership", "Store"][n], "Amount Sold"]]
    for i in range(4):
        data.append([shop_name[i], str(values[i])])

    question = f"Here is the results of some market research on the {items} " \
               f"by some {shop_type.lower()}. " \
               f"Find the mean value of the results? \n\n" \
               f"\\begin{{center}} {mq.draw_table(data)} \\end{{center}}"
    answer = mq.dollar(mean(values))
    return [question, answer]


def fr_30(difficulty):
    """Addition and subtraction of both a decimal and a fraction. Chrys."""
    b = random.choices(
        [2, 4, 10, 100],
        weights=(difficulty, difficulty, 4 - difficulty, difficulty), k=1)[0]
    a = random.choice([x for x in range(1, b) if mq.gcd(x, b) == 1])
    fraction = mq.dollar(mq.latex_frac(a, b))

    upper = [10, 10, 100][difficulty - 1]
    c = random.randint(1, upper)
    decimal = c / upper

    values = [[fraction, a / b], [decimal, decimal]]
    n = random.randint(0, 1)
    op = ["$+$", "$-$"][n]
    if n == 0:
        shuffle(values)
    else:
        values.sort(key=lambda x: x[1])

    question = r""" 
    Writing your answer as a decimal, solve the equation. \ 
    \begin{center} %s %s %s = \makebox[2em]{\hrulefill} \end{center}
    """ % (values[1][0], op, values[0][0])

    result = [(a / b + decimal), values[1][1] - values[0][1]][n]
    answer = mq.dollar(round(result, 2))
    return [question, answer]


def me_18(difficulty):
    """Convert units. Chrys."""
    prefixes = ['kilo', '', 'centi', 'milli']

    n = random.randint(0, 2)
    unit = ['meter', 'liter', 'gram'][n]

    m = ''
    k = ''
    while m == '' and k == '':
        a = random.randint(0, 3)
        b = a + (-1) ** random.randint(1, 2) * random.randint(1, 2)
        if 0 <= a < 3 and 0 <= b < 3:
            if a == 2 and b == 0:
                b = b + 1
            if n == 2 and a != 2 and b != 2:
                k = a
                m = b
            elif n == 1 and a != 0 and b != 0:
                k = a
                m = b
            elif n == 0:
                k = a
                m = b

    rand = random.randint(1,  5 * (difficulty - 1))
    num = random.choices([1, rand], weights=(5, difficulty - 1), k=1)[0]
    unit_in = str(prefixes[k][:1] + unit[:1])
    unit_out = str(prefixes[m][:1] + unit[:1])
    convert = mq.convert_measurement(int(num), unit_in, unit_out)
    if convert >= 1:
        convert = int(convert)

    s_1, s_2 = '', ''
    if convert != 1:
        s_2 = "s"
    if num != 1:
        s_1 = "s"
    question = f"Convert the following. \n\n {num} {prefixes[k]}{unit}{s_1} " \
               f"= \\makebox[2em]{{\\hrulefill}} {prefixes[m]}{unit}{s_2}"
    answer = f"{convert}"
    return [question, answer]


def sh_3(difficulty):
    """Compare angles. Chrys."""
    acute = random.randint(10 + 10 * difficulty, 50 + 10 * difficulty)
    obtuse = random.randint(130 - 10 * difficulty, 170)
    n = random.sample(range(3), k=2)
    angles = [acute, 90, obtuse]

    angle_size = ["acute", "a right angle", "obtuse"][n[0]]
    choices = []
    for i in range(2):
        choices.append(mq.angle_drawing(angles[n[i]], 0, 1.7, 0.5))
    answer = choices[0]
    question = f"Which of these angles is {angle_size}? \n\n"
    return mq.multiple_choice(question, choices, answer)


def sh_4(difficulty):
    """Guess how many sides/vertices a 2d shape has. Chrys."""
    upper = [5, 7, 10][difficulty - 1]
    n = random.choices([1, random.randint(2, upper)],
                       weights=(difficulty, upper))[0]
    if n == 1:
        shape = mq.draw_circle(4, 'white', 'black')
        vertices = 0
    elif n == 2:
        shape = r"""
        \begin{tikzpicture} 
        [baseline=(current bounding box.north)] 
        \draw (-1.5,0) -- (1.5,0) arc(0:180:1.5) --cycle; 
        \end{tikzpicture}
        """
        vertices = n
    else:
        shape = r"""
        \begin{tikzpicture} 
        \node[regular polygon, regular polygon sides=%s, minimum size=2cm, 
        draw] at (0, 0) {};
        \end{tikzpicture}
        """ % n
        vertices = n
    k = random.randint(0, 1)
    choice = ["sides", "vertices"][k]
    question = f"How many {choice} does this shape have? \n\n " \
               f"\\begin{{center}} {shape} \\end{{center}}"
    answer = [str(n), str(vertices)][k]
    return [question, answer]


def sh_5(difficulty):
    """Guess how many lines of symmetry a 2d shape has. Chrys."""
    w = difficulty - 1
    n = random.choices([0, 1, 2, 3, 4, 5], weights=(w, w, w, 1, 1, 1))[0]
    if n == 0:
        shape = mq.draw_semi_circle(1.5)
        answer = "1"
    elif n == 1:
        shape = mq.draw_triangle(5, draw="black", fill="white")
        answer = "1"
    elif n == 2:
        shape = r"\tikz \draw (0,0) rectangle (3cm,1.5cm);"
        answer = "2"
    else:
        shape = mq.draw_regular_polygon(n)
        answer = str(n)
    question = "How many lines of Symmetry does this shape have? \n\n" \
               r" \begin{center} %s \end{center}" % shape
    return [question, answer]
