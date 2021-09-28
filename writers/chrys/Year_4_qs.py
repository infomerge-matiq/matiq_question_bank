import random
import roman
import statistics

from datetime import time, datetime, timedelta
from math import floor, ceil
from num2words import num2words

from random import shuffle
import names

import matiq_question_bank.python_code.functions as mq


# NUMBER AND PLACE VALUE_______

def pv_1(difficulty):
    """Choice of fill in missing or find the next number in a sequence"""
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
        n = random.randint(0, 1)
        answer = numbers[n]
        numbers[n] = "\\makebox[1em\\textwidth]{\\hrulefill}"
    else:
        numbers.append("\\fillin[][1em]")
        answer = mq.dollar(step * (k + 1))

    sequence = ",\\ ".join(numbers)
    question = [f"Write the next number in the sequence. \n\n {sequence}",
                f"Fill in the missing number in the sequence."
                f"\n\n {sequence}"][i]
    return [question, answer]


def pv_2(difficulty):
    """Choice of 3 questions involving the addition and subtraction of 1000"""
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
    """Rounding to nearest power of 10"""
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
    """Identify place of a digit in a given number."""
    places = ["Ones place",
              "Tens place",
              "Hundreds place",
              "Thousands place",
              "Ten thousands place"
              ]
    digits = random.sample(range(1, 9), 2+difficulty)
    n = int(''.join(map(str, digits)))
    d = random.randint(1, len(str(n)))
    question = f"Where is the digit {int(str(n)[- d]):g} " \
               f"in the number {mq.dollar(n)}?"
    choices = []
    for i in range(0, len(str(n))):
        choice1 = places[i]
        choices.append(choice1)
    answer = choices[d-1]
    return mq.multiple_choice(question, choices, answer)


def pv_5(difficulty):
    """Identify value of the digit in a given position in a number"""
    places = ["ones", "tens", "hundreds", "thousands", "ten thousands"]
    n = random.randint(10 ** (difficulty + 1), 10 ** (difficulty + 2))
    d = random.randint(1 + round(difficulty / 3), len(str(n)))
    question = f"In the number {mq.dollar(n)}, " \
               f"what is the value of the digit in the {places[d-1]} position?"
    answer = mq.dollar({int(str(n)[- d])})
    return [question, answer]


def pv_6(difficulty):
    """Find the nth smallest or largest number in a sequence"""
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
    """ Use table to find person with largest/smallest score"""
    n = random.randint(0, 1)
    size = ['least', 'most']
    col_2 = random.sample(range(100, 1000 + 10 ** (difficulty + 2)), 5)
    c = []
    for i in range(len(col_2)):
        c.append([names.get_first_name(), col_2[i]])

    table = "\\begin{center}\n\\begin{tabular}{||c c||}\n " \
            "\\hline \n Name & Score \\\\ [0.5ex]\n" \
            f"\\hline\\hline \n {c[0][0]} & {c[0][1]} \\\\ \n " \
            f"\\hline \n  {c[1][0]} & {c[1][1]}  \\\\ \n \\hline \n " \
            f"{c[2][0]} & {c[2][1]} \\\\ \n " \
            f"\\hline \n  {c[3][0]} & {c[3][1]}  \\\\ \n \\hline \n " \
            f" {c[4][0]} & {c[4][1]}  \\\\ " \
            "[1ex]\n \\hline \n \\end{tabular}\n \\end{center}"
    question = f"Some friends are playing a game. " \
               f"The table below shows each of their scores.\n\n{table}\n\n " \
               f"Who has the {size[n]} amount of points?"

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
    """ Use table to nth highest/smallest value. """
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

    table = "\\begin{center}\n\\begin{tabular}{||c c||}\n \\hline\n " \
            f"{['Sport', 'Town'][m]} & {['Attendance', 'Population'][m]} " \
            f"\\\\ [0.5ex]\n \\hline\\hline \n  " \
            f"{c[0][0]} & {c[0][1]} \\\\ \n \\hline \n" \
            f"{c[1][0]} & {c[1][1]}  \\\\ \n \\hline \n " \
            f"{c[2][0]} & {c[2][1]} \\\\ \n \\hline \n " \
            f"{c[3][0]} & {c[3][1]}  \\\\ \n \\hline \n " \
            f"{c[4][0]} & {c[4][1]}  \\\\ " \
            "[1ex]\n \\hline \n \\end{tabular}\n \\end{center}"

    question = [f"A sports competition is happening. "
                f"The table below shows the attendance for each event. \n\n "
                f"{table} \n\n What sport had the "
                f"{order} {size} attendance?",
                f"The table below shows the populations "
                f"for some towns. \n\n  {table}\n\n"
                f"What town has the {order} {size} population?"
                ][m]
    choices = []
    for j in range(len(c)):
        choices.append(c[j][0])

    if n == 0:
        c.sort(key=lambda x: x[1])
    else:
        c.sort(key=lambda x: x[1], reverse=True)
    answer = c[i - 1][0]
    return mq.multiple_choice(question, choices, answer)


def pv_9(difficulty):
    """arranging integers in ascending or descending order"""
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
    """Pick the sign to complete the inequality"""
    lower = 10 ** (difficulty-1)
    upper = 5 * 10 ** difficulty
    a = random.choices(lower, upper)
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
    """Inequalities which include addition and subtraction."""
    upper = 2**(3+difficulty)
    numbers = random.sample(range(2, upper), 4)
    no_3 = random.randint(0, numbers[0])

    question = "Choose the sign that correctly completes the statement. \n\n" \
               f"\\begin{{center}} {numbers[0]} $+$ {numbers[1]} " \
               f"$-$ {no_3} $\\square$ " \
               f"{numbers[2]} $+$ {numbers[3]} \\end{{center}}"

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


def pv_12(difficulty):  # Taken from Year 5 qs and joined two qs into one
    n = random.randint(1, difficulty * 100)
    k = random.randint(0, 1)
    question = [f"What is {n} in Roman numerals?",
                f"What is the value of {roman.toRoman(n)}?"][k]
    answer = [roman.toRoman(n), mq.dollar(n)][k]
    return [question, answer]


def pv_13(difficulty):
    """Inequalities where student fills missing num to make statement true."""
    upper = 2**(4+difficulty)
    no_1 = random.randint(5, upper)
    no_2 = random.randint(no_1 + 10, 2*upper)
    signs = [" $<$ ", " $=$ ", " $>$ "]
    sign = random.choice([" $<$ ", " $=$ ", " $>$ "])
    question = "Choose the number that makes this statement true. \n\n" \
               f"\\begin{{center}}" + mq.dollar(no_1) + sign \
               + mq.dollar(no_2) + " $-$ " \
               + "{\\fboxsep0pt\\fbox{\\rule{2em}{0pt}\\rule{0pt}{2.2ex}}} " \
                 "\\end{center}"
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
    """filling in each square to break down number into powers of ten."""
    upper = 10 ** (difficulty + 2) - 1
    lower = 10 ** (difficulty + 1)
    n = random.randint(lower, upper)
    places = ["ones", "tens", "hundreds", "thousands", "ten-thousands"]
    y = []
    results = []
    for i in reversed(range(2 + difficulty)):
        y.append(f"$\\square$ {places[i]}")
        results.append(f"{mq.dollar({int(str(n)[- (i + 1)])})} {places[i]}")
    values = " $+$\\ ".join(y)
    answer = " $+$\\ ".join(results)

    question = f"Break down the number {num2words(n)} " \
               f"by filling in the gaps. \n\n {mq.dollar(n)}$=$ {values} "
    return [question, answer]


def pv_15(difficulty):
    """Breaking down number into thousands, tens ect. filling in each part"""
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
    square = ''
    for i in range(len(answer) - 2):
        square += "{\\fboxsep0pt\\fbox{\\rule{0.9em}{0pt}\\rule{0pt}{2.4ex}}}"

    question = f"Find the number that completes the statement. " \
               f"\n\n {square} = {x}"
    return [question, answer]

# Addition Subtraction_____________


def as_1(difficulty):
    """addition of numbers up to 4 digits, using columnar method"""
    lower = 2 * (400 * difficulty - 200)
    upper = 2000 * difficulty
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    question = r"\hspace{2cm}{\LARGE$\begin{array}{r}" + str(b) + \
               r"\\\underline{+\ " + str(a) + r"}\end{array}$} \\ \\" \
               + "\\vspace{1.2ex}"
    answer = mq.dollar(b+a)
    return [question, answer]


def as_2(difficulty):
    """fill in missing value to balance equation"""
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
    values[k] = "\\makebox[2.5em\\textwidth]{\\hrulefill}"
    question = f"Find the number that makes the equation true." \
               f"\n\n {values[0]} {sign[0]} {(values[1])} " \
               f"$=$ {values[2]} {sign[1]} {values[3]}"
    return [question, answer]


def as_3(difficulty):
    """addition and subtraction using words"""
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
    """fill in missing number in columnar method for addition & subtraction"""
    lower = 200 * difficulty - 150
    upper = 300 * difficulty
    x = random.sample(range(lower, upper), k=2)
    n, k = random.randint(0, 1), random.randint(0, 1)
    nums = [[x[1], x[0] + x[1]][n], x[0]]
    result = [mq.dollar(nums[1] + nums[0]), mq.dollar(x[1])][n]
    answer = str(nums[k])
    nums[k] = ''
    for i in range(len(answer)):
        nums[k] += "{\\fboxsep0pt\\fbox{\\rule{0.5em}{0pt}\\rule{0pt}{2ex}}}"
    question = "Fill in the missing number. \n\n " \
               r"\hspace{2cm}{\LARGE$\begin{array}{r}" + str(nums[0]) + \
               r"\\\underline{" + ['+', '-'][n] + r"\ " + str(nums[1]) + r"}"\
               + r"\\\underline{" + result + r"} \end{array}$}" \
               + "\\vspace{1ex}"
    return [question, answer]


def as_5(difficulty):
    """add/subtract 3 numbers with up to 3 digits, using columnar method"""
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
    question = r"\hspace{2cm}{\LARGE$\begin{array}{r}" \
               + str(no_2) + r"\\\ " + str(no_1) \
               + r"\\\underline{" + ["+", "-"][k] + r"\ " + str(no_3) +\
               r"} \end{array}$} \\ \\" + "\\vspace{1.2ex}"
    answer = [mq.dollar(no_1 + no_2 + no_3), mq.dollar(no_2 - no_3 - no_1)][k]
    return [question, answer]


def as_6(difficulty):
    """complete table using addition and subtraction rules"""
    lower = 100 + (10 ** difficulty)
    upper = 500 * (2 ** difficulty)
    nums = random.sample(range(lower, upper), k=5)
    col_1 = sorted(nums)

    if difficulty == 1:
        no_plus = 5 * random.randint(30, 150)
        no_minus = -50*random.randint(2, (col_1[0] // 50))
    else:
        no_plus = random.randint(lower/2, upper/2)
        no_minus = 5 * random.randint(1 - (col_1[0] // 5), 1 - (lower // 5))

    n = random.randint(0, 1)
    rule = [[no_plus, 'add'], [no_minus, 'minus']][n]
    col_2 = [i+rule[0] for i in col_1]

    table = "\\begin{center}\n\\begin{tabular}{||c  |  c||}\n " \
            "\\hline\n Input & Output \\\\ [0.4ex]\n" \
            f"\\hline\\hline \n  {col_1[0]} & {col_2[0]} \\\\ \n " \
            f"\\hline \n  {col_1[1]} &   \\\\ \n \\hline \n " \
            f"{col_1[2]} &  \\\\ \n \\hline \n  {col_1[3]} &   " \
            f"\\\\ \n \\hline \n {col_1[4]} &   \\\\ " \
            "[1ex]\n \\hline \n \\end{tabular}\n \\end{center}"
    question = f"Use the rule to complete the table. \n\n " \
               f"Rule: {rule[1]} {abs(rule[0])} \n\n {table}"

    answer = "\n\\begin{tabular}{||c  |  c||}\n " \
             "\\hline\n Input & Output \\\\ [0.4ex]\n \\hline\\hline \n  " \
             f"{col_1[0]} & {col_2[0]} \\\\ \n \\hline \n  " \
             f"{col_1[1]} & \\textbf{{{col_2[1]}}} \\\\ \n \\hline \n " \
             f"{col_1[2]} & \\textbf{{{col_2[2]}}} \\\\ \n \\hline \n " \
             f"{col_1[3]} & \\textbf{{{col_2[3]}}} \\\\ \n \\hline \n " \
             f"{col_1[4]} & \\textbf{{{col_2[4]}}}  \\\\ " \
             "[1ex]\n \\hline \n \\end{tabular}\n"
    return [question, answer]


def as_7(difficulty):
    """Find answer to addition/subtraction question and state if odd/even"""
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
                    "\\makebox[2.5em\\textwidth]{\\hrulefill} is " \
                    "\\makebox[2.5em\\textwidth]{\\hrulefill} \n\n"
        answer += f"{results[i]} is {odd_even[i]} \n\n"
    return [question, answer]


def as_8(difficulty):
    """Worded addition problem"""
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
    """find missing value in table by deducting other values from total"""
    lower = 50 + (100 * (difficulty - 1))
    upper = 180 + (100 * (difficulty - 1))

    col_1 = random.sample(['Oasis Airways',
                           'Artemis Air',
                           'Andromeda Airlines',
                           'Air Alpha',
                           'Air Polaris'
                           ], k=3)
    col_2 = random.sample(range(lower, upper), k=3)
    total = sum(x for x in col_2)
    n = random.randint(0, len(col_2)-1)
    answer = mq.dollar(col_2[n])
    col_2[n] = ""

    table = "\\begin{center}\n\\begin{tabular}{||c  |  c||}\n " \
            "\\hline\n Airline & Passengers \\\\ [0.4ex]\n \\hline\\hline \n" \
            f"{col_1[0]} & {col_2[0]} \\\\ \n \\hline \n" \
            f"{col_1[1]} & {col_2[1]}  \\\\ \n \\hline \n" \
            f"{col_1[2]} & {col_2[2]} \\\\ \n \\hline \n" \
            f"\\textbf{{Total}} &  \\textbf{{{total}}} \\\\ " \
            "[1ex]\n \\hline \n \\end{tabular}\n \\end{center}"

    question = f"Here is some information about the amount of passengers who" \
               f" flew with some airlines. \n\n {table} \n\n Using the " \
               f"table, find how many passengers flew with {col_1[n]}."
    return [question, answer]


def as_10(difficulty):
    """Subtraction patterns"""
    nums = random.sample(range(2*difficulty, 5*difficulty), k=2)
    sums = sum(nums)

    question = "Fill in the missing values.\n\n"
    answer = ""
    if difficulty == 1:
        for i in range(5):
            question += f"{sums * (10 ** i)} " \
                        f"$-$ \\makebox[2.5em\\textwidth]{{\\hrulefill}} " \
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
            values[j][n] = f"\\makebox[2.5em\\textwidth]{{\\hrulefill}}"
            question += f"{values[j][0]} $-$ {values[j][1]} " \
                        f"$=$ {values[j][2]}\n\n"
    return [question, answer]


def as_11(difficulty):
    """Find the missing digit of a number in the columnar method"""
    lower = 100 + (400 * (difficulty - 1))
    upper = 300 + (500 * (difficulty - 1))
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    nums = [a, b, a + b]
    n = random.randint(0, 1)
    d = random.randint(1, len(str(nums[n])))
    answer = f"{int(str(nums[n])[d-1]): g}"
    nums[n] = str(nums[n])[:d-1] \
        + "\\hspace{0.05em}" \
          "\\fboxsep0pt\\fbox{\\rule{1.05ex}{0pt}\\rule{0pt}{0.75em}}" \
          "\\hspace{ 0.05em}" \
        + str(nums[n])[d:]

    values = [str(nums[n]) + "", str(nums[(n + 1) % 2]) + "\\hspace{0.09em}",
              str(nums[2]) + "\\hspace{0.09em}"
              ]
    k = random.sample([0, 1], k=2)
    question = "Find the missing digit. \n\n" + \
               r"\hspace{2cm}{\LARGE$\begin{array}{r}" + values[k[0]] + \
               r"\\\underline{+\ " + values[k[1]] + r"}" \
               + r"\\\underline{\ \ \ " + str(values[2]) + r"}\end{array}$}" \
               + "\\ \\" + r"\\vspace{1.2ex}"
    return [question, answer]


def as_12(difficulty):
    """Subtraction over zero using columnar method"""
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

    question = r"\hspace{2cm}{\LARGE$\begin{array}{r}" + str(a) + \
               r"\\\underline{-" + str(b) + r"}\end{array}$} \\ \\" \
               + "\\vspace{1.2ex}"
    answer = mq.dollar(a - b)
    return [question, answer]


def as_13(difficulty):
    """Worded subtraction problem where values are in word or number format."""
    lower = 200 + 1000 * (difficulty - 1)
    upper = 1000 + 4000 * (difficulty - 1)
    x_1 = random.randint(lower, upper)
    x_2 = random.randint(round(lower * 1/2), round(x_1 * 2/3))
    name = random.choice([["space company", "rockets", "uses"],
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
    """subtraction of numbers up to 4 digits, using columnar method"""
    lower = 100 * difficulty + round(10 ** difficulty + 1)
    upper = 100 * difficulty + round(0.5 * (10 ** (difficulty + 1) - 1))
    b = random.randint(lower, upper)
    a = random.randint(round(0.5*lower), round(0.7*b))
    question = r"\hspace{2cm}{\LARGE$\begin{array}{r}" + str(b) + \
               r"\\\underline{-\ " + str(a) + r"}\end{array}$} \\ \\" \
               + "\\vspace{1.2ex}"
    answer = mq.dollar(b-a)
    return [question, answer]

# Multiplication Division______


def md_1(difficulty):
    """Multiplication of 2 or 3 digit numbers with one digit number"""
    a = random.randint(20 + (difficulty-1) * (difficulty * 150 - 200),
                       100 + (difficulty - 1) * (difficulty * 50 + 300))
    b = random.randint(3, 9)
    question = r"\hspace{2cm}{\LARGE$\begin{array}{r}" + str(a) + \
               r"\\\underline{\times\ " + str(b) + r"}\end{array}$}" \
               "\\vspace{3em}"
    answer = mq.dollar(a * b)
    return [question, answer]


def md_2(difficulty):
    """Fill in missing values in times table"""
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
    """find answer to x*y"""
    x = random.randint(3, 12)
    y = random.randint(4*difficulty, 12*difficulty)
    question = mq.dollar(x) + " $\\times$ " + mq.dollar(y) + " $=$"
    answer = mq.dollar(x * y)
    return [question, answer]


def md_4(difficulty):
    """ Find the missing value, multiplication worded in groups of numbers"""
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
    """Factor pair multiple choice, taken and adapted from year 5 problems"""
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
    """Multiplication of 1 digit and two digit number using area as model"""
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
            f"& \\tikz \\fill [amber] (0,0) rectangle (1.5em, 1.2);"
        ]
        size = [0.8, 0.4]
    else:
        box = ['', '', '']
        size = [1.5, 1]

    model = f"\\definecolor{{ceruleanblue}}{{rgb}}{{0.16, 0.32, 0.75}}" \
            f"\\definecolor{{amaranth}}{{rgb}}{{0.9, 0.17, 0.31}}" \
            f"\\definecolor{{amber}}{{rgb}}{{1.0, 0.75, 0.0}}" \
            f"{{\\arraycolsep=2pt" \
            f"\\LARGE$\\begin{{array}}{{rrr{box[0]}}}\n\n $\\times$ " \
            f"{box[1]} & {tens} \\hspace{{{size[0]}em}} " \
            f"& {ones} \\hspace{{{size[1]}em}} & {x} " \
            f"& \\tikz \\fill [amaranth] (0,0) rectangle (4em, 1.2);" \
            f"& \\tikz \\fill [ceruleanblue] (0,0) rectangle (2.5em, 1.2); " \
            f"{box[2]} \\end{{array}}$ }}\\ "

    question = f"Use the model to solve {mq.dollar(x)}" \
               f" $\\times$ {mq.dollar(y)}." \
               f"\n\n \\textit{{Hint: Find each area first.}} \n\n {model}"
    answer = mq.dollar(x * y)
    return [question, answer]


def md_7(difficulty):
    """Choose the answer that is/is not a multiple of a given number"""
    num = random.randint(2+difficulty, 9 + difficulty)
    multipliers = random.sample(range(2, 12), k=5)

    choices = []
    answer = num * multipliers[4]
    n = random.randint(0, 1)
    if n == 1:
        is_not = ""
        for k in range(4):
            choices.append(num * multipliers[k] + random.randint(1, num-1))
    else:
        is_not = "NOT"
        for k in range(4):
            choices.append(num * multipliers[k])
            answer = answer + random.randint(1, num-1)

    choices.append(answer)
    question = f"Which of these is {is_not} a multiple of {num}?"
    return mq.multiple_choice(question, choices, answer)


def md_8(difficulty):
    """Choose the two numbers that multiply to produce a given answer"""
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

    question = "Choose the two numbers from the list that complete the" \
               f" multiplication. \n\n \\begin{{center}} {choices}" \
               "\\end{center} \n\n" \
               " \\begin{{center}} \\makebox[0.04\\textwidth]{\\hrulefill}" \
               " \\times \\hspace{0.1em} \\makebox[0.04\\textwidth]" \
               f"{{\\hrulefill}} = {str(num)}" \
               "\\end{center}"
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
    sign = ["\\times", "\\div"][n]

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
    question = f"{str(a)} $\\times$ {str(b)} $\\times$ {str(c)} $=$"
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
    more_less = ["as many", "less"][n]
    values = [num, num * factor]

    question = f"{name[0]} has {values[n]} {item}. {name[1]} has " \
               f"{factor} times {more_less} {item} than {name[0]}. " \
               f"How many {item} does {name[1]} have?"
    answer = str(values[(n + 1) % 2])
    return [question, answer]


def md_15(difficulty):
    """complete table using multiplication or division rule"""
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

    table = "\\begin{center}\n\\begin{tabular}{||c  |  c||}\n " \
            "\\hline\n Input & Output \\\\ [0.4ex]\n" \
            f"\\hline\\hline \n  {col_1[0]} & {col_2[0]} \\\\ \n " \
            f"\\hline \n  {col_1[1]} &   \\\\ \n \\hline \n " \
            f"{col_1[2]} &  \\\\ \n \\hline \n  {col_1[3]} &   " \
            f"\\\\ \n \\hline \n {col_1[4]} &   \\\\ " \
            "[1ex]\n \\hline \n \\end{tabular}\n \\end{center}"

    question = f"Use the rule to complete the table. \n\n " \
               f"Rule: {operator} {operand} \n\n {table}"

    answer = "\n\\begin{tabular}{||c  |  c||}\n " \
             "\\hline\n Input & Output \\\\ [0.4ex]\n \\hline\\hline \n  " \
             f"{col_1[0]} & {col_2[0]} \\\\ \n \\hline \n  " \
             f"{col_1[1]} & \\textbf{{{col_2[1]}}} \\\\ \n \\hline \n " \
             f"{col_1[2]} & \\textbf{{{col_2[2]}}} \\\\ \n \\hline \n " \
             f"{col_1[3]} & \\textbf{{{col_2[3]}}} \\\\ \n \\hline \n " \
             f"{col_1[4]} & \\textbf{{{col_2[4]}}}  \\\\ " \
             "[1ex]\n \\hline \n \\end{tabular}\n"
    return [question, answer]


def md_16(difficulty):
    """Multiplication/Division patterns"""
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
        values[j][n] = f"\\makebox[2.5em\\textwidth]{{\\hrulefill}}"
        question += f"{values[j][0]} {operator} {values[j][1]} " \
                    f"$=$ {values[j][2]}\n\n"
    return [question, answer]


def md_17(difficulty):
    """Worded multiplication problem with 3 numbers"""
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
    """find answer to x divided by y"""
    a = random.randint(3, 12)
    b = random.randint(2 * difficulty, 9 + difficulty)
    question = f"What is {a * b} $\\div$ {b}?"
    answer = mq.dollar(a)
    return [question, answer]


def md_19(difficulty):
    """long Division with remainder"""
    m = random.randint(2 * difficulty, 12)
    n = random.randint(200 * difficulty - 100, 450 * difficulty - 350)
    question = f"\\longdivision[stage=0]{{{n}}}{{{m}}}"
    if n % m:
        answer = f"{n // m} r.{n % m}"
    else:
        answer = str(n // m)
    return [question, answer]


def md_20(difficulty):
    """Multiplication using distributive law"""
    a = random.randint(2 * difficulty, 12)
    b = random.randint(2 * difficulty, 9 + difficulty)
    c = random.randint(3 * difficulty, 9 + difficulty)
    d = random.randint(2 * difficulty, 9 + difficulty)
    question = f"What is {a} $\\times$ ({b} $+$ {c} "
    if difficulty == 3:
        question += f"$+$ {d})?"
        answer = mq.dollar(a * (b + c + d))
    else:
        question += ")?"
        answer = mq.dollar(a * (b + c))
    return [question, answer]


def md_21(difficulty):
    """Choose the two numbers that divide to produce a given answer"""
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

    question = "Choose the two numbers from the list that complete the" \
               f" statement. \n\n \\begin{{center}} {choices}" \
               "\\end{center} \n\n" \
               " \\begin{{center}} \\makebox[0.04\\textwidth]{\\hrulefill}" \
               " $\\div$ \\hspace{0.1em} \\makebox[0.04\\textwidth]" \
               f"{{\\hrulefill}} = {str(b)}" \
               "\\end{center}"
    answer = ",\\ ".join([str(num), str(a)])
    return [question, answer]


def md_22(difficulty):
    """Find missing values in division table"""
    col_2 = random.sample(range(2 + difficulty, 9 + difficulty), k=5)
    col_3 = random.choices(range(2 + difficulty, 10 + 2 * difficulty), k=5)

    values = []
    for i in range(5):
        values.append([col_2[i] * col_3[i], col_2[i], col_3[i]])

    answer = "\\begin{tabular}{||c | c | c ||}\n  \\hline\n" \
             "Total & \\shortstack{Number of \\\\ Groups} &" \
             "\\shortstack{Number in \\\\ Each Group} \\\\ [0.4ex]\n \\hline" \
             f"\\hline\n {values[0][0]} & {values[0][1]} & {values[0][2]} \\\\"
    for k in range(1, 5):
        answer += f"\n \\hline \n {values[k][0]} & {values[k][1]} " \
                  f"& {values[k][2]} \\\\ "
    answer += "[1ex]\n \\hline \n \\end{tabular}"

    for k in range(5):
        n = random.randint(0, 2)
        values[k][n] = ""

    table = "\\begin{tabular}{||c | c | c ||}\n  \\hline\n" \
            "Total & \\shortstack{Number of \\\\ Groups} &" \
            "\\shortstack{Number in \\\\ Each Group} \\\\ [0.4ex]\n \\hline" \
            f"\\hline \n {values[0][0]} & {values[0][1]} & {values[0][2]} \\\\"
    for k in range(1, 5):
        table += f"\n \\hline \n {values[k][0]} & {values[k][1]} " \
                 f"& {values[k][2]} \\\\ "
    table += "[1ex]\n \\hline \n \\end{tabular}"

    question = "Complete the table. \n\n \\textit{Hint:} " \
               "\\textit{Total} = \\textit{Number of Groups} \\\\" \
               " $\\times$ \\textit{Number in Each Group}" \
               f" \n\n {table}"
    return [question, answer]


def md_23(difficulty):
    """worded division problem, dividing 3 digit number, includes remainder"""
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
    """worded division problem, which divides 3 digit number into an integer"""
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
                   f"How many {choices[1]} do we need per {choices[3]}?"
    else:
        question = f"A {choices[0]} needs to {choices[1]} {c} {choices[2]} " \
                   f"within {a} months. How many {choices[2]} will they " \
                   f"need to {choices[1]} per month to achieve this target?"
    answer = str(b)
    return [question, answer]


def md_25(difficulty):
    """True or false question whether an integer is divisible by another."""
    b = random.randint(3 + difficulty, 12)
    n = random.randint(0, 1)
    a = [
        b * random.randint(10 * difficulty, 10 + 10 * difficulty),
        b * random.randint(10 * difficulty, 10 + 10 * difficulty)
        + random.randint(1, b - 1)
    ][n]

    choices = []
    answer = ["Yes", "No"][n]
    choices.append(["No", "Yes"][n])
    choices.append(answer)

    question = f"Is {a} divisible by {b}?"
    return mq.multiple_choice(question, choices, answer)


def md_26(difficulty):
    """division using model, with area given"""
    x = random.randint(3, 8 + (difficulty % 3))
    tens = random.randint(1, 3 * difficulty) * 10
    ones = random.randint(1, 9)

    box = "\\fboxsep0pt\\fbox{\\rule{1.7em}{0pt}\\rule{0pt}{1em}}"
    if difficulty == 3:
        rectangle = [
            'r',
            f"& {box} \\hspace{{{1.1}em}} ",
            f"& \\colorbox{{amber}}{{\\makebox(1.5em, 1.2cm)"
            f"{{\\textcolor{{black}}{ones * x}}}}}"
        ]
        size = [0.5, 0]
        values = [100 * x, tens * x, 100 + tens + ones]
    else:
        rectangle = ['', '', '']
        size = [1, 0.5]
        values = [tens * x, ones * x, tens + ones]

    model = f"\\definecolor{{ceruleanblue}}{{rgb}}{{0.16, 0.32, 0.75}}" \
            f"\\definecolor{{amaranth}}{{rgb}}{{0.9, 0.17, 0.31}}" \
            f"\\definecolor{{amber}}{{rgb}}{{1.0, 0.75, 0.0}}" \
            f"{{\\arraycolsep=2pt" \
            f"\\LARGE$\\begin{{array}}{{rrr{rectangle[0]}}}\n\n " \
            f"{rectangle[1]} & {box} \\hspace{{{size[0]}em}} " \
            f"& {box} \\hspace{{{size[1]}em}} & {x} " \
            f"& \\colorbox{{amaranth}}{{\\makebox(4em, 1.2cm)" \
            f"{{\\textcolor{{black}}{values[0]}}}}}" \
            f"& \\colorbox{{ceruleanblue}}{{\\makebox(2.5em, 1.2cm)" \
            f"{{\\textcolor{{black}}{values[1]}}}}}" \
            f"{rectangle[2]} \\end{{array}}$ }}\\ "

    question = f"Use the model to solve {x * values[2]} $\\div$ {x}." \
               f"\n\n \\textit{{Hint: Firstly, use the areas to find the " \
               f"missing lengths of the rectangles.}} \n\n {model}"
    answer = mq.dollar(values[2])
    return [question, answer]


# FRACTION QUESTIONS____________

def fr_1(difficulty):
    """Fraction addition and subtraction question."""
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
        f'$\\frac{{{num_1}}}{{{denominator}}}$',
        f'$\\frac{{{num_2}}}{{{denominator}}}$',
        f'$\\frac{{{num_3}}}{{{denominator}}}$',
    ]

    question = f"\\begin{{LARGE}} {fracs[0]}{op_1}{fracs[1]}{op_2}{fracs[2]}" \
               f" $=$\\end{{LARGE}}"
    answer = f'$\\frac{{{sums[2]}}}{{{denominator}}}$'
    return [question, answer]


def fr_2(difficulty):
    """Write fraction as decimal."""
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
    """Find missing number when converting decimal to fraction."""
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
    """Round number with 1 decimal place to nearest integer."""
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
    """Which decimal is smallest/largest."""
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
    """Arrange fractions from smallest to largest."""
    upper = random.choices([8, 12, 16], weights=(3, difficulty+1, difficulty))
    upper = int(upper[0])
    denominator = [upper, upper, upper // 2, upper // 4]

    numerator = random.sample(range(1, upper - 1), 2)
    numerator.extend([
        random.randint(1, upper // 2 - 1),
        random.randint(1, upper // 4 - 1)
    ])

    values = []
    for k in range(len(numerator)):
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
    """What decimal is the nth smallest/ largest"""
    upper = [8, 819, 819][difficulty - 1]
    m = random.randint(1, upper)
    numbers = random.sample(range(1, 20 * (2 ** (3 - difficulty))), 5)
    dec_places = [100, 1000, 1000][difficulty - 1]
    decimals = [(m + i) / dec_places for i in numbers]

    k = random.randint(0, 1)
    order = ["smallest to largest", "largest to smallest"][k]
    n = random.randint(1, 5)
    question = f"If you order the following decimals from {order}," \
               f" which comes {mq.num2words(n, to='ordinal')}?"

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
    """Identify tenths, hundredths and thousandths digits from decimal."""
    places = ["thousandths", "hundredths", "tenths"]
    integer = random.choice([0, random.randint(0, 99)])
    power = 10 ** difficulty
    decimal = random.randint(power + 1, 10 * power - 1)
    if decimal % 10 == 0:
        decimal = decimal + 1
    n = integer + (decimal / (10 * power))

    d = random.randint(2 - round(difficulty / 3), 3)
    question = f"What is the value of the {places[d - 1]} digit in " \
               f"the number {n}"
    answer = mq.dollar(f"{int(str(n)[- d + (2 - difficulty)]) :g}")
    return [question, answer]


def fr_9(difficulty):
    """find answer to a fraction of a given integer"""
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
    """compare sums and difference of fractions with same denominator"""
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

    question = "Choose the sign that makes the statement true. \n\n" \
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
    """Choose which fraction is equivalent to the one given."""
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
    """Simplify fraction."""
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
    """Identify what fraction of a rectangle is shaded."""
    n = random.randint(3, 8 + 2 ** (difficulty - 1))
    m = random.randint(1, n - 1)
    shaded_boxes = ""
    white_boxes = ""
    r = ""

    if n <= 6:
        size = [2, 2]
    elif 6 < n <= 9:
        size = [1.75 - 0.2 * (n - 7), 2]
    else:
        size = [1.2 - 0.1 * (n - 10), 2]

    colour = random.choice(["ceruleanblue", "amaranth", "amber"])
    for i in range(m):
        shaded_boxes += f"& \\tikz \\draw [fill={colour}] (0,0) " \
                        f"rectangle ({size[0]}em, {size[1]}em);"
    for j in range(n-m):
        white_boxes += f"& \\tikz \\draw [fill=white] (0,0) " \
                       f"rectangle ({size[0]}em, {size[1]}em);"
    for k in range(n):
        r += "r"

    box = f"\\definecolor{{ceruleanblue}}{{rgb}}{{0.16, 0.32, 0.75}}" \
          f"\\definecolor{{amaranth}}{{rgb}}{{0.9, 0.17, 0.31}}" \
          f"\\definecolor{{amber}}{{rgb}}{{1.0, 0.75, 0.0}}" \
          f"{{\\arraycolsep=0" \
          f"\\LARGE$\\begin{{array}}{{r{r}}}\n\n " \
          f"{shaded_boxes} {white_boxes}" \
          f" \\end{{array}}$ }}  \\ "

    question = f"What fraction of the shape is shaded? "
    if difficulty == 1:
        answer = f"${mq.latex_frac(m, n)}$"
    else:
        question += f"Reduce your answer to its lowest form. "
        answer = f"${mq.latex_frac_simplify(m, n)}$"
    question += f"\n\n {box}"
    return [question, answer]


def fr_14(difficulty):
    """Choose which of the shaded rectangles represent the given fraction.."""
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
    colour = ["ceruleanblue", "amaranth", "amber", "orange"]
    shuffle(colour)
    for i in range(quantity):
        shaded_boxes = ""
        white_boxes = ""
        r = ""
        for j in range(m[i]):
            shaded_boxes += f"& \\tikz \\draw [fill={colour[i]}] (0,0) " \
                            f"rectangle (0.9em, 2em);"
        for j in range(n[i] - m[i]):
            white_boxes += f"& \\tikz \\draw [fill=white] (0,0) " \
                           f"rectangle (0.9em, 2em);"
        for k in range(n[i]):
            r += "r"
        box = f"\\definecolor{{ceruleanblue}}{{rgb}}{{0.16, 0.32, 0.75}}" \
              f"\\definecolor{{amaranth}}{{rgb}}{{0.9, 0.17, 0.31}}" \
              f"\\definecolor{{amber}}{{rgb}}{{1.0, 0.75, 0.0}}" \
              f" {{\\arraycolsep=0" \
              f"\\leftmargin\\LARGE$\\begin{{array}}{{r{r}}}\n\n " \
              f"{shaded_boxes} {white_boxes}" \
              f" \\end{{array}}$ }}  \\ \\newline"
        choices.append(box)

    question = f"What model has had ${mq.latex_frac_simplify(m[0], n[0])}$ " \
               f"of it shaded?"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer)


def fr_15(difficulty):
    """Find the proportion of a pattern that is a specified shape."""
    b = random.randint(3 + difficulty, 9 + difficulty)
    a_1 = random.randint(1, b - 2)
    a_2 = random.randint(1, b - a_1 - 1)
    a_3 = b - a_1 - a_2

    k = random.randint(0, 2)
    shape_names = ["circles", "squares", "triangles"][k]

    order = []
    for i in range(a_1):
        circle = "\\tikz \\node[circle,minimum size=1.5em," \
                 "draw=ceruleanblue,fill=ceruleanblue] (c) &"
        order.append(circle)
    for j in range(a_2):
        square = "\\tikz \\node[square, minimum size=1.5em," \
                 "draw=amaranth,fill=amaranth] (S) &"
        order.append(square)
    for n in range(a_3):
        triangle = "\\tikz \\node[isosceles triangle, minimum size=1.5em," \
                   "rotate=90,draw=amber,fill=amber] (T) &"
        order.append(triangle)
    shuffle(order)

    r = ""
    shapes = ""
    if b <= 6 and b % 2 == 1:
        columns = b
    else:
        columns = ceil(b / 2)
    for m in range(columns):
        r += "r"
    for i in range(len(order)):
        shapes += order[i]

    model = f"\\definecolor{{ceruleanblue}}{{rgb}}{{0.16, 0.32, 0.75}} " \
            f"\\definecolor{{amaranth}}{{rgb}}{{0.9, 0.17, 0.31}}" \
            f"\\definecolor{{amber}}{{rgb}}{{1.0, 0.75, 0.0}}" \
            f" {{\\arraycolsep=2" \
            f"\\begin{{center}}\\LARGE$\\begin{{array}}{{{r}}}\n\n {shapes} " \
            f" \\end{{array}}$ }} \\end{{center}}  "
    question = f"What fraction of the shapes are {shape_names}? " \

    if mq.gcd([a_1, a_2, a_3][k], b) != 1 and difficulty > 1:
        question += f"Simplify your answer where possible."
        answer = f"${mq.latex_frac_simplify([a_1, a_2, a_3][k], b)}$"
    else:
        answer = f"${mq.latex_frac([a_1, a_2, a_3][k], b)}$"
    question += f"\n\n {model}"
    return [question, answer]


def fr_16(difficulty):
    """Convert worded version of fraction into numbers."""
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

    question = f"Write down {num2words(a)} {denominator} as a fraction?"
    answer = f"${mq.latex_frac(a, b)}$"
    return [question, answer]


def fr_17(difficulty):
    num_type = random.choice(["decimal", "fraction"])
    b = 10 ** difficulty
    a = random.choice([x for x in range(1, b) if mq.gcd(x, 10) == 1])
    fraction = mq.dollar(mq.latex_frac(a, b))
    decimal = a / b
    if num_type == "decimal":
        num = fraction
        answer = mq.dollar(decimal)
    else:
        num = mq.dollar(decimal)
        answer = fraction
    question = f"What is {num} as a {num_type}?"
    return [question, answer]


def fr_18(difficulty):
    """fill in each square to break down decimal number into powers of tens."""
    upper = 10 ** difficulty
    decimal = random.randint(upper / 10 + 1, upper - 2)
    if decimal % 10 == 0:
        decimal = decimal + 1
    integer = random.randint(1, upper - 1)
    num = integer + decimal / upper

    integer_place = ["ones", "tens", "hundreds", "thousands"]
    decimal_place = ["tenths", "hundredths", "thousandths"]

    y_1 = f"$\\square${integer_place[len(str(integer)) - 1]}"
    y_2 = ""

    result_int = f"{mq.dollar({int(str(integer)[- len(str(integer))])})} " \
                 f"{integer_place[len(str(integer)) - 1]}"
    result_dec = f""

    if len(str(integer)) > 1:
        for i in reversed(range(1, len(str(integer)))):
            y_1 += f" $+$ $\\square${integer_place[i - 1]}"
            result_int += f" $+$ {mq.dollar({int(str(integer)[- i])})} " \
                          f"{integer_place[i - 1]} "

    for j in range(len(str(decimal))):
        y_2 += f" $+$ $\\square${decimal_place[j]}"
        result_dec += f" $+$ {mq.dollar({int(str(decimal)[j])})} " \
                      f"{decimal_place[j]} "

    answer = result_int + result_dec
    question = f"Break down the number " \
               f"by filling in the gaps. \n\n {mq.dollar(num)} $=$ {y_1} {y_2}"
    return [question, answer]


def fr_19(difficulty):
    """Addition/Subtraction of two fractions with same denominator."""
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
    """Find missing value in subtraction/addition of two fractions."""
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
    values[n][0] = "\\fboxsep0pt\\fbox{\\rule{0.8em}{0pt}\\rule{0pt}{0.8em}}"
    values[n][1] = "\\fboxsep0pt\\fbox{\\rule{0.8em}{0pt}\\rule{0pt}{0.8em}}"
    question = f" Fill in the missing fraction: \n\n \\Large " \
               f"${mq.latex_frac(values[0][0], values[0][1])}$ {op} " \
               f"${mq.latex_frac(values[1][0], values[1][1])}$ " \
               f"$=$ ${mq.latex_frac(a_1 + ((-1) ** k) * a_2, b)}$\\large"
    return [question, answer]


def fr_21(difficulty):
    """Worded subtraction problem. Subtracting 2 fractions from 1."""
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
    pronoun = [["He", "he", "his"], ["She", "she", "her"]][i]

    question = [
        f"{name_1} has a full {item} in {pronoun[2]} car before {pronoun[1]} "
        f"leaves for work. {pronoun[0]} uses up {fracs[0]} of a tank on the "
        f"journey to work. On the way back, {pronoun[1]} uses up another "
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
        f" In total, what fraction of the {item} had been {verb}?"
    ][k]
    result = [b - a_1 - a_2, a_1 + a_2][k]
    answer = f"${mq.latex_frac(result, b)}$"
    return [question, answer]


def fr_22(difficulty):
    """Worded subtraction problem. Difference of two fractions."""
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
    """Identify place of a digit in a decimal number."""
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
    """Identify fraction from number line."""
    b = random.randint(1 + difficulty, 3 + 2 ** difficulty)
    a = random.randint(1, b - 1)
    length = 7
    circle = "\\definecolor{ceruleanblue}{rgb}{0.16, 0.32, 0.75}" \
             f"\\fill[fill = ceruleanblue] (({a} * {length}/{b},0) " \
             "circle[radius=3pt]"
    question = "What fraction is shown on the number line? "

    if mq.gcd(b, a) != 1:
        question += "Simplify your answer."
        answer = f"${mq.latex_frac_simplify(a, b)}$"
    else:
        answer = f"${mq.latex_frac(a, b)}$"
    question += f"\n\n {mq.num_line(b, False, circle, length=length)}"
    return [question, answer]


def fr_25(difficulty):
    """Identifying fraction lengths on number line. Multiple choice."""
    b = random.sample(range(3 + difficulty, 8 + 2 ** (difficulty-1)), k=2)
    a = random.sample(range(1, b[0] - 1), k=2)
    length = 6
    values = [a[0] / b[0], a[1] / b[0]]

    choices = []
    for i in range(2):
        start = random.randint(0, b[0] - a[i])
        line = f"\\draw[line width = 2pt, color=red] " \
               f"(({start} * {length}/{b[0]},0) -- " \
               f"(({start + a[i]} * {length}/{b[0]},0);"
        choices.append(
            f"{mq.num_line(b[0], False, line, length=length)} \\vspace{{2em}}"
        )
    while len(choices) < 3:
        c = random.randint(1, b[1] - 1)
        if c/b[1] not in values:
            start = random.randint(0, b[1] - c)
            line = f"\\draw[line width = 2pt, color=red] " \
                   f"(({start} * {length}/{b[1]},0) -- " \
                   f"(({start + c} * {length}/{b[1]},0);"
            choices.append(f"{mq.num_line(b[1], False, line, length=length)} "
                           f"\\vspace{{2em}}")

    question = "Which number line has a coloured segment of length " \
               f"${mq.latex_frac(a[0],b[0])}$?"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer)

# MONEY QUESTIONS______________________


def me_1(difficulty):
    """Money Problem question, subtracting a value from a starting amount"""
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
    """ Convert 24hr into 12hr clock and vice versa"""
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
    """Question: How many minutes is between two 24hr times t1 and t2?"""
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

    question = f"How many minutes after " \
               + time(h1, m1).strftime("%H:%M") \
               + " do we have to wait until it is " \
               + time(h2, m2).strftime("%H:%M") + "?"
    answer = str(int(abs((d2-d1).total_seconds())/60)) + " minutes"
    return [question, answer]


def me_4(difficulty):
    """find how long someone was doing an activity, answer in hrs & mins"""
    activity = random.choice(['studying', 'reading', 'walking', 'painting',
                              'drawing', 'gardening'])

    n = random.randint(0, 1)
    gender = ["male", "female"]
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
        question += "\\begin{center} " \
                    "\\makebox[0.04\\textwidth]{\\hrulefill} minutes" \
                    "\\end{center}"
    else:
        answer = f"{time_elapsed[0]} hours and {time_elapsed[1]} minutes."
        question += "\\begin{center} \\makebox[0.04\\textwidth]{\\hrulefill}" \
                    " hours and \\hspace{0.1em} \\makebox[0.04\\textwidth]" \
                    "{\\hrulefill} minutes \\end{center}"
    return [question, answer]


def me_5(difficulty):
    """Converting units of clock measurements, e.g. 1 week in days"""
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

    result = mq.time_unit_converter(unit_in, unit_out, 1)
    question = f"How many {unit_out} are there in {prefix} {unit_in}?"
    answer = str(result[0]) + result[1]
    return [question, answer]


def me_6(difficulty):
    """Select the correct time in words from a 24hr clock, multiple choice"""
    sample = random.sample(range(0, 11), 3)
    minutes = [5 * i for i in sample]
    hours = random.choices([
        random.sample(range(2, 12), 2),
        random.sample(range(13, 22), 2)
    ],
        weights=(1, difficulty), k=1)[0]
    time_in = [hours[0], minutes[0]]
    question = f"Which option describes the time " \
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
    choice2 = mq.time_to_words(time_2[0], time_2[1])
    choice3 = mq.time_to_words(time_in[1], time_in[0])

    answer = mq.time_to_words(time_in[0], time_in[1])
    choices.extend([choice1, choice2, choice3, answer])
    return mq.multiple_choice(question, choices, answer)


def me_7(difficulty):
    """"Multiple choice, converting time in words to a 12hr or 24hr clock"""
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

    question = f'What is {mq.time_to_words(hour, minutes[0])} ' \
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
    """Simple elapsed time question with mix of time in words and digits """
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
                            mq.time_to_words(hour_out, min_out)
                            ])

    words_or_number = random.choice([
        [time1, num2words(minutes_add)],
        [mq.time_to_words(h1, m1), minutes_add],
        [time1, minutes_add]
    ])
    choices = []
    mins_sample_1 = random.sample(range(min_out-20, min_out-1), k=3)
    mins_sample_2 = random.sample(range(min_out+1, min_out-20+30), k=3)
    for i in range(3):
        m_2 = random.choice([mins_sample_1[i], mins_sample_2[i]])
        choice2 = random.choice([time(hour_out, m_2 % 60).strftime("%H:%M"),
                                 mq.time_to_words(hour_out, m_2 % 60)
                                 ])
        choices.append(choice2)
    ch1 = random.choice([(hour_out + 1) % 24, (hour_out - 1) % 24])
    cm1 = random.randint(0, 59)
    choice1 = random.choice([time(ch1, cm1).strftime("%H:%M"),
                             mq.time_to_words(ch1, cm1)
                             ])
    choices = choices + [choice1, answer]
    question = f"The time is {words_or_number[0]}, " \
               f"what time will it be in {words_or_number[1]} minutes?"
    return mq.multiple_choice(question, choices, answer)


def me_9(difficulty):
    """elapsed time problem, mixture of 12hr, 24hr and worded format."""
    n = random.randint(0, 1)
    gender = ['Female', 'Male'][n]
    name = random.choice([names.get_first_name(gender=gender[n])])
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
    """AM/PM problem where student picks correct time from multiple choice. """
    if difficulty == 3:
        time_in = [random.randint(0, 23), 5 * random.randint(0, 11)]
    else:
        time_in = [random.randint(0, 23),
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
    n = random.choices([0, 1, 2], weights=(1, 4, 2), k=1)
    n = n[0]
    num_or_words = [[mq.time_to_words(time_in[0], time_in[1]), morn_eve[0]],
                    [time_format, ''],
                    [mq.time_to_words(time_in[0], time_in[1]), morn_eve[0]]
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
    return mq.multiple_choice(question, choices, answer)


def me_11(difficulty):
    """ Converting analogue clock to digital times or worded time"""
    hour = random.randint(0, 11)
    minute = ((20-5*difficulty)*random.randint(0, 11)) % 60
    choice = random.choice([['In 12 hour format',
                             time(hour, minute).strftime("%H:%M")
                             ],
                            ['Using words', mq.time_to_words(hour, minute)]
                            ])
    question = f"{choice[0]}, write down the time shown on the clock.\n\n " \
               f"\\begin{{center}}\n {mq.analogue_clock(hour, minute)}" \
               f"\n \\end{{center}}"
    answer = choice[1]
    return [question, answer]


def me_12(difficulty):
    """Multiple choice, converting analogue to digital clock and vice versa"""
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
        mq.time_to_words(hour, minute[0]),
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
        choice1 = mq.analogue_clock((hour + difference) % 12, minute[0])
        choice2 = mq.analogue_clock(minute[0] / 5, (5*hour) % 60)
        choice3 = mq.analogue_clock(
            hour, (minute[0] + 5 * random.randint(1, 11)) % 60)
    else:
        question = f"What is the correct time, in 12 hour format, " \
                   f"that is shown on the clock?\n\n \\begin{{center}}" \
                   f"\n {mq.analogue_clock(hour,minute[0])} \\end{{center}}"
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
        mq.analogue_clock(hour, minute[0]),
        time(hour, minute[0]).strftime("%I:%M")
    ][n]
    choices.extend([answer, choice1, choice2, choice3])
    return mq.multiple_choice(question, choices, answer)


def me_13(difficulty):
    """Draw on clock to get time"""
    hour = random.randint(0, 11)
    minute = ((20-5*difficulty) * random.randint(0, 11)) % 60
    time_in = random.choice([
        time(hour, minute).strftime("%H:%M"),
        mq.time_to_words(hour, minute)
    ])
    blank_clock = "\\begin{center}\n\\begin{tikzpicture}" \
                  "[line cap=rect,line width=3pt]\n \\filldraw [fill=white]" \
                  " (0,0) circle [radius=1.3cm];\n" \
                  "\\foreach \\angle [count=\\xi] in {60,30,...,-270}\n" \
                  "{\n  \\draw[line width=1pt] " \
                  "(\\angle:1.15cm) -- (\\angle:1.3cm);\n " \
                  "\\node[font=\\large] at (\\angle:0.9cm)" \
                  "{\\textsf{\\xi}};\n}\n \\foreach " \
                  "\\angle in {0,90,180,270}\n \\draw[line width=1.5pt] " \
                  "(\\angle:1.1cm) -- (\\angle:1.3cm);\n" \
                  "\\end{tikzpicture}\n\\end{center}"
    question = f"Draw the time {time_in} on the clock.\n\n {blank_clock}"
    answer = mq.analogue_clock(hour, minute)
    return [question, answer]


def me_14(difficulty):
    """elapsed time question using analogue clock"""
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
                hour_in+floor((minute_in+time_elapsed)/60),
                (minute_in+time_elapsed) % 60)
        ]
    ])
    question = f"Using the clock, find what time it will be in " \
               f"{time_elapsed_format} minutes? Write this down " \
               f"{answer_format[0]}.\n\n " \
               f"\\begin{{center}}\n {mq.analogue_clock(hour_in, minute_in)}" \
               f"\\end{{center}}\n "
    answer = answer_format[1]
    return [question, answer]


def me_15(difficulty):
    """ Time sequence question where student fills missing time. """
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
    """Guess the shape, multiple choice."""
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
    """What type of transformation is occurring.."""
    size = 6
    n = random.randint(0, 2)
    name = [
        "isosceles triangle",
        "regular polygon,regular polygon sides=5",
        "circle split"
    ][n]
    rotate = [[0, 180], [270, 90], [45, 135]][n]

    k = random.randint(0, 1)
    shape = f"node[{name}, minimum size=1cm," \
            f" rotate={rotate[k]}, draw, fill=green]"
    reflection = f"node[{name}, minimum size=1cm," \
                 f" rotate={rotate[(k + 1) % 2]}, draw, fill=green]"

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

    pic = f"\\begin{{tikzpicture}} \\usetikzlibrary{{shapes,snakes}} " \
          f"\\draw[step=0.5,gray,thin] (0,0) grid ({size},3);" \
          f"\\draw ({x_0},{y_0}) {shape} ;" \
          f"\\draw ({x_1}, {y_1}) {[shape, reflection][m]} ;"

    if difficulty == 1:
        pic += "\\draw [ultra thick,red] (3,0) -- (3,3); "
    pic += "\\end{tikzpicture}"

    question = f"What transformation has occurred? \n\n {pic}"
    choices = ["Translation", "Reflection"]
    answer = choices[m]
    return mq.multiple_choice(question, choices, answer)


def st_1(difficulty):
    """Mean of a group of numbers."""
    upper = 10 ** difficulty - 1 - 800 * round(difficulty / 10 + 0.3)
    nums = []
    while len(nums) == 0:
        k = random.randint(5, 10 - difficulty)
        values = random.choices(range(0, upper), k=k)
        if sum(values) % k == 0:
            nums = values

    sequence = ",\\ ".join(str(nums[i]) for i in range(len(nums)))
    question = f"Find the mean of these numbers. \n\n {sequence}"
    answer = f"{statistics.mean(nums)}"
    return [question, answer]
