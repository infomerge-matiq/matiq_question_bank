import random
import numpy as np
from datetime import time, datetime, timedelta
from math import floor, ceil
from statistics import mean

import matiq as mq
import names
from num2words import num2words
import roman
import numpy


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


def as_16(difficulty):
    """
    Addition & subtraction of money using decimal and pence format. Chrys.
    """
    a = random.randint(10 * difficulty, 60 * difficulty)
    b = random.randint(30 * difficulty, 65 * difficulty)
    values = [round((a + b) / 100, 2), round(b / 100, 2), round(a / 100, 2)]
    n = random.randint(0, 1)

    values[n] = r"\pounds" + f"{values[n]:.2f}"
    values[(n + 1) % 2] = f"{round(values[(n + 1) % 2] * 100)}p"

    j = random.randint(0, 1)
    answer = [r"\pounds" + f"{values[2]:.2f}", f"{round(values[2] * 100)}p"][j]

    choices = []
    choices.extend([answer, r"\pounds" + f"{round((a + b) / 100, 2):.2f}"])
    while len(choices) < 5:
        num = random.randint(1, 30)
        k = random.randint(0, 1)
        c_0 = a + (-1) ** k * num
        c_1 = r"\pounds" + f"{round(c_0 / 100, 2):.2f}"
        if c_0 > 0 and num not in choices:
            choices.append(random.choice([str(c_0) + "p", c_1]))

    question = f"What is {values[0]} $-$ {values[1]}?"
    return mq.multiple_choice(question, choices, answer)


def as_17(difficulty):
    """
    Find the next number in a sequence, with increasing step size. Chrys
    """
    start = random.randint(1, 10 + 10 * (difficulty - 1))
    step_1 = random.randint(1 * difficulty, 3 * difficulty)
    step_increase = random.randint(1, 1 + difficulty)

    numbers = [start]
    for i in range(1, 5):
        num = numbers[i-1] + step_1 + (step_increase * i)
        numbers.append(num)

    n = random.randint(0, 1)
    if n == 1:
        numbers.sort(reverse=True)

    numbers = [str(j) for j in numbers]
    answer = numbers[len(numbers) - 1]
    numbers[len(numbers)-1] = "\\fillin[][1em]"

    sequence = ",\\ ".join(numbers)
    question = "Find the next number in the sequence. \n\n \\begin{center}" \
               + sequence + "\\end{center}"
    return [question, answer]


def as_18(difficulty):
    """Addition Grid. Chrys."""
    upper = 16 + 25 * (difficulty - 1)
    nums = random.sample(range(2, upper), 6)
    x = np.array([[nums[0]], [nums[1]], [nums[2]]])
    y = np.array([[nums[3], nums[4], nums[5]]])
    result = np.add(x, y)

    title = ["$+$"]
    for i in range(3):
        title.append(r"\textbf{%s}" % nums[i+3])

    data = [title]
    for j in range(3):
        row = [r"\textbf{%s}" % x[j][0]]
        for a in range(3):
            row.append(str(result[j][a]))
        data.append(row)
    answer = mq.draw_table(data)

    if difficulty == 1:
        for m in range(1, len(data)):
            for i in range(1, len(data[m])):
                data[m][i] = ""
    elif difficulty > 1:
        values = []
        a = random.sample(range(1, 3), k=2)
        b = random.randint(1, 3)
        n = random.sample(range(1, 3), k=2)

        check = []
        # Hides values in first column of grid
        for k in range(2):
            data[a[k]][0] = ""
            values.append(data[a[k]][n[k]])
            check.append((a[k], n[k]))
        if difficulty == 3:
            data[0][b] = ""
            while len(values) < 3:
                n_2 = random.randint(1, 3)
                if (n_2, b) not in check:
                    values.append(data[n_2][b])
                    n.append(n_2)
        # Clears Grid elements
        for m in range(1, len(data)):
            for i in range(1, len(data[m])):
                data[m][i] = ""
        # Reinserts some values into clear grid
        for k in range(2):
            data[a[k]][n[k]] = values[k]
        if difficulty == 3:
            data[n[2]][b] = values[2]

    table = mq.draw_table(data)
    question = "Complete the addition grid. \n\n" + table
    return [question, answer]


def as_19(difficulty):
    """Do calculations using data from table to answer questions. Chrys."""
    upper = 100 * difficulty
    lower = 40 * difficulty
    nums = random.sample(range(lower, upper), k=7)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]

    data = [["Day", "Visitors"]]
    values = []
    for i in range(7):
        data.append([days[i], str(nums[i])])
        values.append([days[i], nums[i]])
    table = mq.draw_table(data)

    name = random.choice(["gym", "swimming pool"])
    question = f"The table shows how many people visited a {name} in a week. "
    n = random.randint(0, 2)

    if n == 0:
        result = 0
        for j in range(5):
            result = result + nums[j]
        question += "How many people visited on weekdays " \
                    "(Monday to Friday)? \n"
    elif n == 1:
        result = nums[5] + nums[6]
        question += "How many people visited on the weekend " \
                    "(Saturday and Sunday)? \n"
    else:
        values.sort(key=lambda x: x[1], reverse=True)
        k = sorted(random.sample(range(7), k=2))
        question += f"How many more people went on {values[k[0]][0]} " \
                    f"than on {values[k[1]][0]}? \n"
        result = values[k[0]][1] - values[k[1]][1]

    answer = mq.dollar(result)
    question = question + table
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
    return mq.multiple_choice(question, choices, answer,
                              reorder=False, onepar=False)


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

    question = "Which fraction is equivalent to " \
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
    random.shuffle(colour)
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
    return mq.multiple_choice(question, choices, answer, onepar=False)


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
    random.shuffle(order)

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
    order = [choices[i] for i in range(difficulty, len(choices))]
    order.extend([choices[j] for j in range(difficulty)])
    choices = order
    return mq.multiple_choice(question, choices, answer,
                              onepar=False, reorder=False)


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
    return mq.multiple_choice(question, choices, answer, onepar=False)


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
    answer = r"\pounds" + f"{result:.2f}"
    return [question, answer]


def fr_27(difficulty):
    """Money subtraction with three numbers. Chrys."""
    limit = 1 + difficulty
    a = round(random.uniform(0.51, limit), 2)
    b = round(random.uniform(1, limit), 1)
    c = round(random.uniform(round(a + b) + 1, 10), difficulty - 1)
    question = r"\pounds%s $-$ \pounds%s $-$ \pounds%s = ?" \
               % (f'{c:.2f}',  f'{b:.2f}', f'{a:.2f}')
    result = c - b - a
    answer = r"\pounds" + f"{result:.2f}"
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
    name = [names.get_first_name(gender='male'),
            names.get_first_name(gender='female')][n]
    pronoun = ['He', 'She'][n]
    question = f"{name} has " + r"\pounds" + f"{start_value:.2f} in pocket " \
               f"money. {pronoun} decides to buy {item}. Afterwards, " \
               f"{pronoun.lower()} has " + r"\pounds" + f"{end_value:.2f} " \
               f"left over. How much did {name} spend in total?"
    result = start_value - end_value
    answer = r"\pounds" + f"{result:.2f}"
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
        my_list.append([items[j], r"\pounds" + f"{price[j]:.2f}"])
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
    answer = r"\pounds" + f"{sum(value):.2f}"
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
        random.shuffle(values)
    else:
        values.sort(key=lambda x: x[1])

    question = r""" 
    Writing your answer as a decimal, solve the equation. \ 
    \begin{center} %s %s %s = \makebox[2em]{\hrulefill} \end{center}
    """ % (values[1][0], op, values[0][0])

    result = [(a / b + decimal), values[1][1] - values[0][1]][n]
    answer = mq.dollar(round(result, 2))
    return [question, answer]


def fr_31(difficulty):
    """Identify decimal from number line. Chrys."""
    length = 7
    b = random.choices(
        [10, 4, 2, 5], weights=(2, difficulty, 2, difficulty), k=1)[0]
    a = random.randint(1, b - 1)
    marker = r'''\fill [shift={(%d * %f/%d, 7pt)}, color=red] (0,0) -- 
        (0.2cm, 0.4cm) -- (-0.2cm, 0.4cm) -- cycle;
        ''' % (a, length, b)

    question = "What decimal is shown on the number line? \n\n" \
               + mq.num_line(b, extra=marker, length=length)
    answer = str(round(a / b, 2))
    return [question, answer]


def fr_32(difficulty):
    """
    Find missing number in a decimal sequence. Chrys
    """
    d_p = [1, 2, 2][difficulty - 1]

    if difficulty > 2:
        step = random.randint(10, 25) / 100
    else:
        step = random.randint(2, 9) / 10 ** difficulty
    step = round(step, d_p)

    start = random.randint(0, difficulty) + step * random.randint(0, 2)
    start = round(start, d_p)

    numbers = [start]
    for i in range(1, 5):
        previous = i - 1
        num = numbers[previous] + step
        numbers.append(round(num, d_p))

    numbers = [round(m) if m % 1 == 0 else m for m in numbers]

    n = random.randint(0, 1)
    if n == 1:
        numbers.sort(reverse=True)

    numbers = [str(j) for j in numbers]

    k = random.randint(0, len(numbers)-1)
    answer = numbers[k]
    numbers[k] = "\\fillin[][1em]"

    sequence = ",\\ ".join(numbers)
    question = "Find the next number in the sequence. \n\n \\begin{center}" \
               + sequence + "\\end{center}"
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
    random.shuffle(values)

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


def md_10(difficulty):
    """Find missing number in multiplication/division"""
    a = random.randint(2 + difficulty, 9 + difficulty)
    b = random.randint(2 + difficulty, 9 + difficulty)
    n = random.randint(0, 1)
    values = [[a, b, a * b], [a * b, a, b]][n]
    sign = ["$\\times$", "$\\div$"][n]
    values = [str(i) for i in values]
    k = random.randint(0, 1)
    answer = values[k]
    values[k] = "\\makebox[0.03\\textwidth]{\\hrulefill}"

    question = "Fill in the missing value. \n\n" \
               f"{values[0]} {sign} {values[1]} = {values[2]}"
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
    answer.sort()
    answer = ",\\ ".join(answer)
    sequence = ",\\ ".join(sequence)
    question = f"Fill in the missing numbers in the sequence: \n\n {sequence} "
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
    random.shuffle(choices)
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
    return mq.multiple_choice(question, choices, answer, reorder=False)


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


def md_27(difficulty):
    """Multiplication Grid. Chrys."""
    upper = 6 + 2 * difficulty
    nums_1 = random.sample(range(2, upper), 3)
    nums_2 = random.sample(range(2, 12), 3)
    nums = sorted(nums_1) + sorted(nums_2)
    x = np.array([[nums[0]], [nums[1]], [nums[2]]])
    y = np.array([[nums[3], nums[4], nums[5]]])
    result = np.multiply(x, y)

    title = ["$\\times$"]
    for i in range(3):
        title.append(r"\textbf{%s}" % nums[i+3])

    data = [title]
    for j in range(3):
        row = [r"\textbf{%s}" % x[j][0]]
        for a in range(3):
            row.append(str(result[j][a]))
        data.append(row)
    answer = mq.draw_table(data)

    if difficulty == 1:
        for m in range(1, len(data)):
            for i in range(1, len(data[m])):
                data[m][i] = ""
    elif difficulty > 1:
        values = []
        a = random.sample(range(1, 3), k=2)
        b = random.randint(1, 3)
        n = random.sample(range(1, 3), k=2)

        check = []
        # Hides values in first column of grid
        for k in range(2):
            data[a[k]][0] = ""
            values.append(data[a[k]][n[k]])
            check.append((a[k], n[k]))
        if difficulty == 3:
            data[0][b] = ""
            while len(values) < 3:
                n_2 = random.randint(1, 3)
                if (n_2, b) not in check:
                    values.append(data[n_2][b])
                    n.append(n_2)
        # Clears Grid elements
        for m in range(1, len(data)):
            for i in range(1, len(data[m])):
                data[m][i] = ""
        # Reinserts some values into clear grid
        for k in range(2):
            data[a[k]][n[k]] = values[k]
        if difficulty == 3:
            data[n[2]][b] = values[2]

    table = mq.draw_table(data)
    question = "Complete the multiplication grid. \n\n" + table
    return [question, answer]


def md_28(difficulty):
    """Worded division question. How many x are there in y. Chrys."""
    a = random.randint(1 + difficulty, 12)
    if a < 6 or a == 10:
        b = random.randint(5 * difficulty, 15 * difficulty)
    else:
        b = random.randint(2 * difficulty, 11 + difficulty)
    question = f"How many {a}'s are there in {a * b}?"
    answer = str(b)
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
    """Factor pair multiple choice, Chrys."""
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
    return mq.multiple_choice(question, choices, answer, reorder=False)


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
    random.shuffle(choices)
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
               r"\pounds" + f"{y0:.2f} in pocket money. She spends " \
               r"\pounds" + f"{x:.2f}. " \
               f"How much money does she have left over?"
    answer = r"\pounds" + f"{round(y0 - x, 2):.2f}"
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
    return mq.multiple_choice(question, choices, answer, onepar=False)


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
    hour = random.randint(1, 12)
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


def me_16(difficulty):
    """Money question: number to words and vice versa. Chrys."""
    pounds = random.randint(2 * difficulty, 9 * difficulty)
    pence = random.randint(1, 99)
    total = pounds + (pence / 100)
    n = random.randint(0, 1)
    num_words = [f"{num2words(pounds)} pounds and {num2words(pence)} pence",
                 r"\pounds" + f"{total:.2f}"
                 ]
    question = f"Write down {num_words[n]} " \
               f"{[' using numbers',' using words'][n]}."
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
    answer = r"\pounds" + f"{sum(sums):.2f}"
    return [question, answer]


def me_18(difficulty):
    """Convert units. Chrys."""
    prefixes = ['kilo', '', 'centi', 'milli']

    n = random.randint(0, 2)
    unit = ['metre', 'litre', 'gram'][n]

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


def me_19(difficulty):
    """
    Compare distances between points in mm or cm using ruler. Chrys.
    """
    length = 7
    upper = [10, 20, 30][difficulty - 1]
    scale = [1, 0.5, 0.3][difficulty - 1]

    nums = random.sample(range(1, upper), k=3)
    nums = [round(k * scale, 1) for k in nums]
    nums.sort()

    locate = (length - 0.2) * 0.1
    tags = ['A', 'B', 'C']
    colour = ['red', 'blue', 'green', 'violet']

    additional = ''
    k = [2, 3, 3][difficulty - 1]
    for i in range(k):
        additional += r'''\fill [shift={(%f * %f, 1)}, color=%s] (0,0) -- 
            (0.07cm, 0.3cm) -- (-0.07cm, 0.3cm) -- cycle;
            \draw (%f * %f, 1.3) node[above, text=%s, scale=0.5]{%s};
            ''' % (nums[i], locate, colour[i],
                   nums[i], locate, colour[i], tags[i])

    values = []
    for j in range(1, 3):
        values.append([tags[j - 1] + " to " + tags[j], nums[j] - nums[j - 1]])
    values.append(["A to C", nums[2] - nums[0]])

    ruler = mq.ruler(length, additional)
    n = random.randint(0, 1)
    unit = [['mm', 'millimetres', 10], ['cm', 'centimetres', 1]][n]

    question = "Find the distance between the points." \
               f" Write your answer in {unit[1]}. \n\n {ruler}" \
               r"\ \begin{center} "
    answer = ""

    for j in range(difficulty):
        result = values[j][1] * unit[2]
        if n == 0:
            result = int(result)
        else:
            result = round(result, 1)
        if result % 1 == 0:
            result = round(result)
        question += r"%s = \makebox[1.5em]{\hrulefill} %s \\" \
                    % (values[j][0], unit[0])
        answer += r"%s = %s%s \\" \
                  % (values[j][0], result, unit[0])
    question += r"\end{center}"
    return [question, answer]


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


def me_20(difficulty):
    """
    Choose which two points are farthest/closest from each other on a ruler.
    Chrys.
    """
    length = 7
    upper = [10, 20, 30][difficulty - 1]
    scale = [1, 0.5, 0.3][difficulty - 1]
    tags = ['A', 'B', 'C', 'D']
    n = random.randint(0, 1)

    nums = []
    results = []
    choices = []
    while len(nums) < 4:
        num = random.sample(range(1, upper), k=4)
        num = [round(k * scale, 1) for k in num]
        num.sort()
        values = []
        choice = []
        for j in range(1, 4):
            name = tags[j - 1] + " to " + tags[j]
            values.append([name, num[j] - num[j - 1]])
            choice.append(name)
        if n == 1:
            values.sort(key=lambda x: x[1])
        else:
            values.sort(key=lambda x: x[1], reverse=True)
        if values[0][1] != values[1][1]:
            nums = num
            results = values
            choices = choice

    locate = (length - 0.2) * 0.1
    colour = ['red', 'blue', 'green', 'violet']
    additional = ''
    for i in range(4):
        additional += r'''\fill [shift={(%f * %f, 1)}, color=%s] (0,0) -- 
        (0.07cm, 0.3cm) -- (-0.07cm, 0.3cm) -- cycle;
        ''' % (nums[i], locate, colour[i])

        additional += r'''
        \draw (%f * %f, 1.3) node[above, text=%s, scale=0.5]{%s};
        ''' % (nums[i], locate, colour[i], tags[i])
    ruler = mq.ruler(length, additional)
    size = ['furthest away from', 'closest to'][n]
    answer = results[0][0]
    question = f"Which of these points on the ruler are {size} each other? " \
               + ruler
    return mq.multiple_choice(question, choices, answer,
                              reorder=False, onepar=False)


def me_21(difficulty):
    """
    Multiple choice. Choose which two points are a given distance apart on a
    ruler. Chrys.
    """
    length = 7
    upper = [10, 20, 30][difficulty - 1]
    scale = [1, 0.5, 0.3][difficulty - 1]
    tags = ['A', 'B', 'C']

    nums = []
    values = []
    choices = []
    while len(nums) < 3:
        num = random.sample(range(1, upper), k=3)
        num = [round(k * scale, 1) for k in num]
        num.sort()

        sample = []
        points = []
        for j in range(1, 3):
            name = tags[j - 1] + " to " + tags[j]
            sample.append([name, num[j] - num[j - 1]])
            points.append(name)
        sample.append(['A to C', num[2] - num[0]])
        points.append("A to C")
        if sample[0][1] != sample[1][1] != sample[2][1]:
            nums = num
            values = sample
            choices = points

    locate = (length - 0.2) * 0.1
    colour = ['red', 'blue', 'green']
    additional = ''
    for i in range(3):
        additional += r'''
        \fill [shift={(%f * %f, 1)}, color=%s] (0,0) -- 
        (0.07cm, 0.3cm) -- (-0.07cm, 0.3cm) -- cycle;
        \draw (%f * %f, 1.3) node[above, text=%s, scale=0.5]{%s};
        ''' % (nums[i], locate, colour[i], nums[i], locate, colour[i], tags[i])

    k = random.randint(0, 1)
    unit = [['cm', 1], ['m', 10]][k]
    ruler = mq.ruler(length, additional, unit[0])

    m = random.randint(0, 2)
    choice = round(values[m][1] * unit[1], 1)
    if choice % 1 == 0:
        choice = round(choice)
    question = "Which two points on the ruler are " \
               f"{choice}cm apart? \n\n {ruler}"
    answer = values[m][0]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_22(difficulty):
    """Measure length of side of shape in cm using ruler. Chrys."""
    length = 7
    upper = [7, 14, 20][difficulty - 1]
    lower = [1, 2, 3][difficulty - 1]
    scale = [1, 0.5, 0.3][difficulty - 1]
    a = round(scale * random.randint(lower, upper), 1)
    coordinate = a * (length - 0.2) * 0.1

    square = r'\filldraw[fill=cyan] (0,1) rectangle (%f,2.5);' % coordinate
    triangle = r'\filldraw[fill=cyan] (0,1) -- (%f,1) -- (%f,2.5);' \
               % (coordinate, coordinate)
    semi_circle = r'\filldraw[fill=red] (0,1)  arc(180:0:%s) --cycle;' \
                  % (coordinate / 2)
    additional = random.choice([square, triangle, semi_circle])

    question = "Using the ruler, measure the length of the side of the " \
               "shape. Give your answer in centimetres. \n\n" \
               + mq.ruler(length, additional)
    if a % 1 == 0:
        a = round(a)
    answer = f"{a}cm"
    return [question, answer]


def me_23(difficulty):
    """Comparing size of different metric units. Multiple Choice. Chrys."""
    units = ['mm', 'cm', 'm', 'km', 'ml', 'l']
    n = random.choices([1, 2, 3, 5], k=1)[0]
    unit_choice = [units[n], units[n - 1]]
    sample_size = 5

    lower = [1, 10, 10]
    upper = [10, 100, 100]
    if n > 1:
        lower[2] = lower[2] * 10
        upper[2] = upper[2] * 10
    lower = lower[difficulty - 1]
    upper = upper[difficulty - 1]
    deviation = ceil((lower * sample_size) / 2)

    mid = random.randint(deviation, upper)

    choices = []
    values = []
    nums = []
    while len(choices) < sample_size:
        a = random.sample(range(mid - deviation, mid + deviation),
                          k=sample_size)
        a = [j / lower for j in a]
        for i in range(sample_size):
            unit_out = unit_choice[(i + 1) % 2]
            convert = mq.convert_measurement(a[i], unit_choice[0], unit_out)

            num = round(convert, difficulty - 1)
            if num % 1 == 0 or difficulty == 1:
                num = round(num)
            if num not in nums:
                values.append([f"{num}{unit_out}", a[i]])
                choices.append(f"{num}{unit_out}")
                nums.append(num)

    k = random.randint(0, 1)
    if k == 0:
        values.sort(key=lambda x: x[1])
    else:
        values.sort(key=lambda x: x[1], reverse=True)

    question = f"Which of these is the {['smallest' ,'largest'][k]}?"
    answer = values[0][0]
    return mq.multiple_choice(question, choices, answer)


def me_24(difficulty):
    """Worded distance question. Chrys."""
    n = random.randint(0, 1)
    lower = [100, 400][n]
    upper = [lower + 33 * difficulty, lower + 66 * difficulty][n]
    nums = sorted(random.sample(range(lower, upper), k=2))

    difference = nums[1] - nums[0]
    k = random.choices([0, 1], weights=(difficulty, 1))[0]
    difference = [difference, round(difference * 0.01, 2)][k]
    cm_m = ["cm", "m"][k]
    nums = [round(0.01 * i, 2) for i in nums]

    sport = ["high jump", "long jump"][n]
    high_far = [["high", "higher"], ["far", "further"]][n]
    name = [names.get_first_name(), names.get_first_name()]

    question = f"{name[0]} and {name[1]} are competing in the {sport}. " \
               f"{name[0]} jumps {nums[0]}m. {name[1]} jumps " \
               f"{difference}{cm_m} {high_far[1]} than {name[0]}. " \
               f"How {high_far[0]} did {name[1]} jump?"
    answer = f"{nums[1]}m"
    return [question, answer]


def me_25(difficulty):
    """Worded question, find height by multiplying height of single item by
    quantity. Chrys."""
    n = random.randint(0, 2)
    lower = [6, 10, 20][n]
    upper = [10, 20, 40][n]
    if n == 2:
        lower_2 = 2 + difficulty
        upper_2 = 9 + difficulty
    else:
        lower_2 = 3 * difficulty
        upper_2 = 7 * difficulty

    thickness = random.randint(lower, upper)
    quantity = random.randint(lower_2, upper_2)

    k = round(n * 0.4)
    unit = ["mm", "cm", "m"]
    unit_format = ["centimetres", "metres"][k]
    items = [["books", "book"], ["tiles", "tile"], ["boxes", "box"]][n]

    question = f"There are {quantity} {items[0]} in a stack. " \
               f"Each {items[1]} is {thickness}{unit[k]} thick. " \
               f"How high is the stack in {unit_format}?"
    result = mq.convert_measurement(quantity * thickness, unit[k], unit[k+1])
    result = round(result, 2)
    if result % 1 == 0:
        result = round(result)
    answer = f"{result}{unit[k+1]}"
    return [question, answer]


def me_26(difficulty):
    """Worded question, find how many items fit within a given width. Chrys."""
    n = random.choices([0, 1, 2], weights=(difficulty, 1, 2), k=1)[0]
    thickness = random.randint(3, 5)
    quantity = random.randint(3 + difficulty, 9 + difficulty) * [1, 1, 3][n]
    width = thickness * quantity
    cm_m = ["cm", "m", "m"][n]
    if n == 0:
        width = round(0.1 * width, 1)
        if width % 1 == 0:
            width = round(width)
    items = ["shelf", "bridge", "car park"][n]
    objects = ["book", "lane", "parking space"][n]
    question = f"A {items} is {width}m wide. Each {objects} is " \
               f"{thickness}{cm_m} wide. How many {objects}s can we fit " \
               f"across the {items}? Write your answer in metres."
    answer = mq.dollar(quantity)
    return [question, answer]


#todo error in question below
def me_27(difficulty):
    """Worded question, find distance travelled over a period of time by
    firstly working out distance travelled per minute. Chrys."""
    n = random.randint(0, 2)
    lower = [250, 800, 10000][n]
    upper = [500, 1000, 13000][n]

    dist_per_min = random.randint(lower, upper)
    if difficulty < 3:
        dist_per_min = round(dist_per_min * 0.01) * 100 \
                       + 50 * (difficulty - 1)

    start_min = random.randint(1 + difficulty, 5 + difficulty)
    start_distance = round((start_min * dist_per_min) * 0.001, 2)
    if start_distance % 1 == 0:
        start_distance = round(start_distance)

    minute = "minute"
    if difficulty == 3:
        end_min = random.randint(1, round(0.5 * start_min))
    else:
        end_min = 1
    if end_min > 1:
        minute += "s"

    result = end_min * dist_per_min
    m_km = ["m", "metres"]
    if result > 2500:
        result = round(result * 0.001, 2)
        m_km = ["km", "kilometres"]
        if result % 1 == 0:
            result = round(result)

    item = ["cyclist", "train", "plane"][n]
    they_it = ["they", "it", "it"][n]
    question = f"A {item} travelled {start_distance}km in {start_min} " \
               f"minutes. How far did {they_it} travel in " \
               f"{end_min} {minute}?. Write your answer in {m_km[1]}."
    answer = f"{result}{m_km[0]}"
    return [question, answer]


def me_28(difficulty):
    """Worded question, find halfway or quarter distance between two locations.
     Chrys."""
    n = random.randint(0, 2)
    vehicle = ["spacecraft", "plane", "train"][n]

    k = random.randint(0, 1)
    location = [
        [["the moon", 38440], ["the international space station", 340]],
        [["Athens", 2400], ["New York", 5400]],
        [["Glasgow", 640], ["Manchester", 312]]
    ][n][k]

    if difficulty > 1:
        location[1] = location[1] + 4 * random.randint(1, 1 + difficulty)

    m = random.choices([0, 1, 2], weights=(2, difficulty + 1, difficulty), k=1
                       )[0]
    travelled = [
        ["halfway", 0.5],
        ["a quarter of the way", 0.25],
        ["three quarters", 0.75]
    ][m]

    question = f"A {vehicle} is on a journey to {location[0]}. " \
               f"The total distance of the journey is {location[1]}km. " \
               f"The {vehicle} is {travelled[0]} into the journey. " \
               f"How far has the {vehicle} travelled? Write your answer in km."
    answer = f"{round(location[1] * travelled[1])}km"
    return [question, answer]


def me_29(difficulty):
    """Find quantity needed of an item to bake a cake or using left over amount
     to find further quantities. Requires converting mass from kg to g. Chrys.
    """
    upper = [3, 9, 99][difficulty - 1]
    a = [25, 10, 1][difficulty - 1]
    num_1 = 100 * random.randint(1, 3) + a * random.randint(1, upper)
    num_2 = random.choice([750, 1000, 2000])
    quant = random.randint(1 + difficulty, 6 + difficulty)

    item = random.choice(["sugar", "flour"])
    gender = random.choice([['Male', 'He'], ['Female', 'She']])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} is baking {quant} cakes. " \
               f"Each cake needs {num_1}g of {item}. "

    total = num_1 * quant
    result_1 = ceil(total / num_2)
    result_2 = floor((result_1 * num_2 - total) / num_1)

    if result_2 > 0:
        n = random.randint(0, 1)
    else:
        n = 0

    answer = [str(result_1), str(result_2)][n]
    num_2 = round(0.001 * num_2, 2)
    if num_2 % 1 == 0:
        num_2 = round(num_2)

    num_3 = result_2 + random.randint(0, 1)
    s = "s" if num_3 > 1 else ""
    question = question + [
        f"How many {num_2}kg bags of {item} does {name} need?",
        f"{gender[1]} has {num_3} bag{s} of {num_2}kg {item}. "
        f"How many more cakes could {name} bake with the left over {item}?"
    ][n]
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


def me_30(difficulty):
    """Table, conversion of units and find quantity to match proportion. Chrys.
    """
    values_start = []
    values_end = []
    quant_start = 0
    quant_end = 0
    items = ["Flour", "Milk", "Eggs"]

    flour = random.randint(50 * difficulty, 100 * difficulty)
    a = [100, 10, 5][difficulty - 1]
    lower = [1, 7, 14][difficulty - 1]
    upper = [3, 25, 50][difficulty - 1]
    milk = a * random.randint(lower, upper)
    eggs = random.randint(1, 2)

    while len(values_start) < 3:
        quant_start = random.randint(4 + difficulty, 10 + difficulty)
        quant_end = random.randint(2, quant_start - 1)
        my_list = [flour, milk, eggs]
        if quant_start % quant_end == 0:
            quant_start = quant_start
            quant_end = quant_end
            for i in range(3):
                values_start.append(my_list[i] * quant_start)
                values_end.append(my_list[i] * quant_end)

    units = [["g", "g"], [" litres", "ml"], ["", ""]]
    values_start[1] = \
        round(mq.convert_measurement(values_start[1], "ml", "l"), 2)
    if values_start[0] > 1000:
        values_start[0] = \
            round(mq.convert_measurement(values_start[0], "g", "kg"), 3)
        units[0][0] = "kg"
    for n in range(2):
        if values_start[n] % 1 == 0:
            values_start[n] = round(values_start[n])

    data = [["Ingredients", f"{quant_start} People", f"{quant_end} People"]]
    for j in range(3):
        data.append([
            items[j],
            str(values_start[j]) + units[j][0],
            str(values_end[j]) + units[j][1]
        ])
    table = mq.draw_table(data)
    answer = table
    for m in range(1, 3):
        data[m][2] = r"\makebox[1em]{\hrulefill}%s" % units[m - 1][1]
    data[3][2] = ""
    question = f"Change this recipe for {quant_start} people to a recipe for" \
               f" {quant_end} people. \n {mq.draw_table(data)}"
    return [question, answer]


def me_31(difficulty):
    """Choose suitable unit for distance measurements in certain scenarios.
    Chrys."""
    n = random.choices(
        [0, 1, 2, 3], weights=(difficulty, difficulty, 2, 4 - difficulty), k=1
    )[0]
    vehicle = random.choice(["plane", "train"])
    items = [
        ["size of an ant", "width of a pencil",
         "thickness of a magazine", "width of a battery",
         "length of a paperclip"],

        ["length of a spoon", "length of a pen",
         "width of a piece of paper", "width of a computer screen"],

        ["height of a building", "length of a bus",
         "length of a running track", "width of a football pitch",
         "height of a tree", "width of a room"],

        [f"length of a {vehicle} journey", "distance to the moon",
         "length of a coastline", "length of a motorway"]
    ][n]
    item = random.choice(items)
    choices = ["Millimetres", "Centimetres",
               "Metres\\hspace{10.5ex}", "Kilometres"]
    question = f"What metric unit is most suitable at measuring the {item}?"
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def me_32(difficulty):
    """Find price for single item using the price for a larger quantity. Chrys.
    """
    start_value = 0
    result = ""
    quantity = ""
    while start_value < 1:
        price = random.randint(2 * difficulty, 5 * difficulty)
        quantity = random.randint(3 + difficulty, 7 * difficulty)
        upper = [1, floor(0.5 * quantity), (quantity - 1)][difficulty - 1]
        additional = random.randint(1, upper)
        if (additional * 100) % quantity == 0:
            quantity = quantity
            start_value = price * quantity + additional
            result = price + additional / quantity

    item = random.choice(["shirt", "book", "game", "hat"])
    name = names.get_first_name()
    question = f"{name} buys {quantity} {item}s for " \
               r"\pounds" + f"{start_value:.2f}. " \
               f"How much does one {item} cost?"
    answer = r"\pounds" + f"{result:.2f}"
    return [question, answer]


def me_33(difficulty):
    """Arrange different distances in ascending/descending order. Chrys.
    """
    n = random.randint(1, 2)
    units = ["mm", "cm", "m", "km"]
    size = [3, 4, 4][difficulty - 1]
    nums = random.sample(range(10, 99), k=size)
    values = []
    for i in range(len(nums)):
        convert = mq.convert_measurement(nums[i], units[n], units[i])
        convert = round(convert, 4)
        if convert % 1 == 0:
            convert = round(convert)
        values.append([convert, units[i], nums[i]])

    convert_2 = mq.convert_measurement(nums[0], units[n-1], units[n])
    values.append([nums[0], units[n-1], convert_2])
    sequence_1 = ', '.join(
        [str(values[i][0]) + values[i][1] for i in range(len(values))]
    )
    k = random.randint(0, 1)
    order = ["ascending", "descending"][k]
    if k == 1:
        values.sort(key=lambda x: x[2], reverse=True)
    else:
        values.sort(key=lambda x: x[2])

    sequence_2 = ', '.join(
        [str(values[j][0]) + values[j][1] for j in range(len(values))]
    )
    question = f"Arrange these distances in {order} order. \n\n {sequence_1}"
    answer = sequence_2
    return [question, answer]


def me_34(difficulty):
    """Estimate mass on number line. Chrys."""
    n = random.choices([0, 1], weights=(1, difficulty))[0]
    unit = ["g", "kg"][n]
    length = 6

    values = []
    while len(values) < 1:
        points = random.randint(2, 10)

        upper = [1000, 100 + 50 * (difficulty - 1)][n]
        lower = 2

        point_diff = [2, 4, 5, 10, 20]
        if difficulty == 1:
            start = 0
            end = random.randint(lower, upper)
            if (end - start) / points in point_diff:
                values.extend([points, start, end])
        else:
            k = random.choices([0, 1], weights=(12, n), k=1)[0]
            m = random.choices([0, 1], weights=(7, (difficulty - 2) * n),
                               k=1)[0]
            end = [random.randint(lower, upper), 1][k]
            start = [random.randint(0, end - 2 + n), end - 1][m]
            point_diff = [5, 8, 25, 4, 3, 4]
            if n == 1:
                point_diff = [8, 25, 4, 0.5, 0.25]
            if end - start == 1:
                points = random.choice([2, 4, 5, 10])
                values.extend([points, start, end])
            elif end - start > 1 and (end - start) / points in point_diff:
                values.extend([points, start, end])
    start = f"{values[1]}{unit}"
    end = f"{values[2]}{unit}"

    a = random.randint(1, values[0] - 1)
    marker = r'''\fill [shift={(%d * %f/%d, 7pt)}, color=red] (0,0) -- 
    (0.2cm, 0.4cm) -- (-0.2cm, 0.4cm) -- cycle;''' % (a, length, values[0])
    line = mq.num_line(values[0], extra=marker,
                       length=length, start=start, end=end)

    result = values[1] + round((a / values[0]) * (values[2] - values[1]), 2)
    if result % 1 == 0:
        result = int(result)
    question = "Determine the value on the scale. " \
               f"Give your answer in {unit}. \n\n {line}"
    answer = f"{result}{unit}"
    return [question, answer]


def me_35(difficulty):
    """Choose suitable unit for mass or volume measurements in certain
    scenarios. Chrys."""
    n = random.choices([0, 1], weights=(2, difficulty), k=1)[0]
    unit_type = ["mass", "volume"][n]
    choices = [["Grams", "Kilograms"], ["Millilitres", "Litres"]][n]
    k = random.randint(0, 1)
    items = [
        [
            ["an orange", "a mobile phone", "a ladybug",
             "a screw", "a slice of cake"],
            ["a piano", "a table", "a stack of bricks",
             "a sack of potatoes", "a human"]
        ],

        [
            ["a glass of water", "a can of soda", "a sachet of vinegar"],
            ["an aquarium", "a swimming pool", "a tank of fuel", "a pond"]
        ]
    ][n][k]
    item = random.choice(items)
    question = f"What metric unit would you use to measure the {unit_type} " \
               f"of {item}?"
    answer = choices[k]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def me_36(difficulty):
    """complete inequalities with volume/mass. Chrys."""
    n = random.randint(0, 1)
    unit = [["g", "kg"], ["ml", "l"]][n]

    k = random.choices([0, 1], weights=(1, 3))[0]
    lower = 201 * difficulty
    upper = 2000 * difficulty
    a = random.randint(lower, upper)
    a = [round(a / 1000, difficulty) * 1000, a][k]
    if a % 1 == 0:
        a = round(a)

    limit = lower - 1
    difference = [0, random.randint(-limit, limit)][k]
    b = random.choices([a + difference, a * 10], weights=(7, difficulty-1))[0]
    b = round(b / 1000, difficulty) * 1000
    b_convert = round(mq.convert_measurement(b, unit[0], unit[1]), difficulty)
    if b_convert % 1 == 0:
        b_convert = round(b_convert)
    question = "Choose the sign that correctly completes the statement. \n\n" \
               r"\begin{center} %s%s $\square$ %s%s \end{center}" \
               % (a, unit[0], b_convert, unit[1])
    choices = ["$<$", "$=$", "$>$"]
    if a > b:
        answer = choices[2]
    elif a < b:
        answer = choices[0]
    else:
        answer = choices[1]
    return mq.multiple_choice(question, choices, answer,
                              reorder=False, onepar=False)


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
    return mq.multiple_choice(question, choices, answer, onepar=False)


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
        choice2 = time((hour + 1) % 24, 60 - minutes[0])
    elif minutes[0] == 30 or minutes[0] == 0:
        choice2 = time((hour + 1) % 24, minutes[4])
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
    return mq.multiple_choice(question, choices, answer, onepar=False)


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
    return mq.multiple_choice(question, choices, answer, onepar=False)


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
    return mq.multiple_choice(question, choices, answer, reorder=False)


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
        answer = mq.dollar(step * k)

    sequence = ",\\ ".join(numbers)
    question = f"Find the {['missing', 'next'][i]} number in the sequence. " \
               f"\n\n {sequence}"
    return [question, answer]


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
    return mq.multiple_choice(question, choices, answer,
                              reorder=False, onepar=False)


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
    return mq.multiple_choice(question, choices, answer,
                              reorder=False, onepar=False)


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
    return mq.multiple_choice(question, choices, answer,
                              onepar=False, reorder=False)


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
    return mq.multiple_choice(question, choices, answer, onepar=False)


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


def sh_10(difficulty):
    """Multiple Choice, choose the shape that is/isn't a polygon. Chrys."""
    n = random.randint(0, 1)
    is_not = ["", "not"][n]
    k = [[1, 3], [3, 1]][n]
    poly = []
    non_poly = []

    for i in range(4):
        sides_1 = random.randint(3, 4)
        poly.append(mq.draw_random_shape(polygon=True, sides=sides_1))
    if difficulty < 3:
        b = random.sample(range(5, 10), k=(5-difficulty))
        for j in range(len(b)):
            poly.append(mq.draw_regular_polygon(b[j]))
    for m in range(4):
        sides_2 = random.randint(3, 4)
        non_poly.append(mq.draw_random_shape(polygon=False, sides=sides_2))

    a = random.randint(0, 1)
    flip = random.choices(["", "-"], k=2)
    parabola_line = [["parabola", "--", "parabola", "--"],
                     ["--", "--", "--", "--"]][a]
    x = []
    while len(x) < 4:
        nums = random.choices([1, 2, 3, 4, 5], k=4)
        nums.sort(reverse=True)
        if nums[3] != nums[2] and nums[2] != nums[1]:
            x = nums
    y = random.choice([[3, 3, 2], [1, 2, 3], [1, 4, 3], [3, 2, 3]])
    x = [i/2 for i in x]
    y = [j/2 for j in y]
    shape_1 = r"""\begin{tikzpicture} 
    \draw (0,0) -- (%s%s,0) %s (%s%s,%s%s) %s 
    (%s%s,%s%s) %s (%s%s, %s%s) %s cycle; \end{tikzpicture}
    """ % (flip[0], x[0], parabola_line[0],
           flip[0], x[1], flip[1], y[0], parabola_line[1],
           flip[0], x[2], flip[1], y[1], parabola_line[2],
           flip[0], x[3], flip[1], y[2], parabola_line[3])
    if a == 0:
        poly.append(shape_1)
    else:
        non_poly.append(shape_1)

    choices = random.sample(poly, k=k[0]) + random.sample(non_poly, k=k[1])
    question = f"Which one of these shapes is {is_not} a polygon?"
    answer = choices[[0, 3][n]]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_11(difficulty):
    """Multiple Choice, choose the shape that is/isn't a polygon. Chrys."""
    n = random.randint(0, 1)
    options = ["perpendicular", "parallel"][n]
    k = random.randint(0, 1)
    true_false = [[True, False], [False, True]][(n + k) % 2]
    if k == 1:
        if difficulty < 2:
            is_false = [False, False]
        else:
            is_false = random.choices([true_false, [False, False]],
                                      weights=(5, difficulty), k=1)[0]
        true_false = is_false

    upper = [0, 9, 270][difficulty - 1]
    rotate = [1, 10][(difficulty - 1) % 2] * random.randint(0, upper)
    size = 2
    choices = ["Yes", "No"]
    drawing = mq.draw_two_lines(size, rotate, true_false[0], true_false[1])
    question = f"Are these lines {options}? \n\n" \
               r"\begin{center} %s \end{center}" % drawing
    answer = choices[k]
    return mq.multiple_choice(question, choices, answer)


def sh_12(difficulty):
    """Multiple Choice, True or false if lines are perpendicular or parallel.
    Chrys."""
    n = random.randint(0, 1)
    options = ["perpendicular", "parallel"][n]
    k = random.randint(0, 1)
    true_false = [[True, False], [False, True]][(n + k) % 2]
    if k == 1:
        is_false = random.choices(
            [true_false, [False, False]], weights=(difficulty, 3), k=1)[0]
        true_false = is_false

    upper = [0, 9, 270][difficulty - 1]
    rotate = [1, 10][(difficulty - 1) % 2] * random.randint(0, upper)
    m = 0
    if difficulty == 1:
        choices = ["Yes", "No"]
        question = f"Are these lines {options}? \n\n"
    else:
        choices = ["True", "False"]
        m = random.randint(0, 1)
        is_not = ["", "NOT"][m]
        question = f"True or False, the two lines are {is_not} {options}? \n\n"

    drawing = mq.draw_two_lines(1.5, rotate, true_false[0], true_false[1])
    question += r"\hspace{2em} %s" % drawing
    answer = choices[(k + m) % 2]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def sh_13(difficulty):
    """Multiple Choice, decide whether lines are perpendicular, parallel or
    neither. Chrys."""
    upper = [1, 45, 270][difficulty - 1]
    rotate = [90, 6, 1][difficulty - 1] * random.randint(0, upper)
    choices = ["Perpendicular", "Parallel"]
    n = random.randint(0, 1)
    if difficulty > 1:
        n = random.randint(0, 2)
        choices.append("Neither Parallel or Perpendicular")
    true_false = [[True, False], [False, True], [False, False]][n]
    drawing = mq.draw_two_lines(1.5, rotate, true_false[0], true_false[1])
    question = "Choose the option that best describes these lines. \n\n" \
               r"\begin{center} %s \end{center}" % drawing
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, False, False)


def sh_14(difficulty):
    """Multiple Choice. Choose out of a selection which lines are either
    parallel perpendicular or neither. Chrys."""
    upper = [1, 45, 270][difficulty - 1]
    rotate = [90, 6, 1][difficulty - 1] * random.randint(0, upper)

    b = 1
    option = ["perpendicular", "parallel"]
    if difficulty == 3:
        option.append("neither parallel nor perpendicular")
        b = 2
    n = random.randint(0, b)
    true_false = [[True, False], [False, True], [False, False]]
    choices = [
        mq.draw_two_lines(1, rotate, true_false[n][0], true_false[n][1])]
    true_false.remove(true_false[n])
    for j in range(2):
        rotate = [90, 6, 1][difficulty - 1] * random.randint(0, upper)
        if n == 2:
            k = true_false[j]
        else:
            k = random.choice(true_false)
        drawing = mq.draw_two_lines(1, rotate, k[0], k[1])
        choices.append(drawing)
    question = f"Which option contains two lines which are {option[n]} " \
               "to each other? "
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer)


def sh_15(difficulty):
    """Guess how many vertices a 2d shape has. Chrys."""
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
    question = f"How many vertices does this shape have? \n\n " \
               f"\\begin{{center}} {shape} \\end{{center}}"
    answer = str(vertices)
    return [question, answer]


def sh_2(difficulty):
    """Decide whether angle is obtuse, acute or right angle. Chrys."""
    angle = random.choices([
        random.randint(20, 60), 90, random.randint(110, 160)],
        weights=(4, 4 - difficulty, 4), k=2)[0]

    x_angle = 90 * random.randint(0, difficulty)
    drawing = mq.draw_angle(x_angle, x_angle - angle, 4)
    question = "Which of the following best describes the angle? \n\n" \
               r"\begin{center} %s \end{center}" % drawing
    choices = ["Acute", "Obtuse", "Right angle"]
    if angle < 90:
        answer = choices[0]
    elif angle > 90:
        answer = choices[1]
    else:
        answer = choices[2]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def sh_3(difficulty):
    """Compare angles. Chrys."""
    acute = random.randint(10 + 10 * difficulty, 50 + 10 * difficulty)
    obtuse = random.randint(130 - 10 * difficulty, 170)
    n = random.sample(range(3), k=2)
    angles = [acute, 90, obtuse]

    angle_size = ["acute", "a right angle", "obtuse"][n[0]]
    choices = []
    for i in range(2):
        choices.append(mq.draw_angle(angles[n[i]], 0, 1.7, 0.5))
    answer = choices[0]
    question = f"Which of these angles is {angle_size}? \n\n"
    return mq.multiple_choice(question, choices, answer)


def sh_4(difficulty):
    """Guess how many sides a 2d shape has. Chrys."""
    upper = [5, 7, 10][difficulty - 1]
    n = random.choices([1, random.randint(2, upper)],
                       weights=(difficulty, upper))[0]
    if n == 1:
        shape = mq.draw_circle(4, 'white', 'black')
    elif n == 2:
        shape = r"""
        \begin{tikzpicture} 
        [baseline=(current bounding box.north)] 
        \draw (-1.5,0) -- (1.5,0) arc(0:180:1.5) --cycle; 
        \end{tikzpicture}
        """
    else:
        shape = r"""
        \begin{tikzpicture} 
        \node[regular polygon, regular polygon sides=%s, minimum size=2cm, 
        draw] at (0, 0) {};
        \end{tikzpicture}
        """ % n
    choice = "sides"
    question = f"How many {choice} does this shape have? \n\n " \
               f"\\begin{{center}} {shape} \\end{{center}}"
    answer = str(n)
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


def sh_6(difficulty):
    """Order shape into quadrilateral or not."""
    n = random.randint(0, 1)
    size = 3
    rectangle = r"\tikz \draw (0,0) rectangle (3cm,1.5cm);"
    rhombus = r"\tikz \draw (0,0) -- (%f,0) -- (%f, 1) -- (0.5,1) -- (0,0);" \
              % (size - 0.5, size)
    shape_1 = r"""
    \tikz \draw (0,0) -- (%f,0) -- (%f, 0.5) -- (%f,1) -- (0,1) -- (0, 0);
    """ % (size - 0.5, size, size - 0.5)

    quad = random.choice([
        mq.draw_regular_polygon(4, size),
        rectangle,
        rhombus,
        mq.draw_square(size=size, draw='black', fill="white", rotate=45)
    ])

    non_quad = random.choices([
        mq.draw_semi_circle(radius=size / 2),
        mq.draw_regular_polygon(sides=random.randint(5, 8), size=size),
        mq.draw_triangle(size=size, fill='white', draw='black'),
        shape_1
    ], weights=(1, 5, 1, 1))[0]

    k = random.choices([0, 1], weights=(1, difficulty))[0]
    shape = [quad, non_quad][n]
    is_not = ["", "NOT"][k]
    choices = ["True", "False"]
    question = f"The shape below is {is_not} a quadrilateral? \n\n" \
               r"\begin{center} %s \end{center}" % shape
    answer = choices[(n + k) % 2]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def sh_7(difficulty):
    """Multiple Choice, Choose which shape is/isn't a quadrilateral. Chrys."""
    n = random.choices([0, 1], weights=(difficulty, 2), k=1)[0]
    size = 1.5

    rectangle = r"\tikz \draw (0,0) rectangle (1.5cm,1cm);"
    rhombus = r"\tikz \draw (0,0) -- (%f,0) -- (%f, 1) -- (0.5,1) -- (0,0);" \
              % (size-0.5, size)
    shape_1 = r"""
    \tikz \draw (0,0) -- (%f,0) -- (%f, 0.5) -- (%f,1) -- (0,1) -- (0, 0);
    """ % (size-0.5, size, size-0.5)

    is_not = ["", "NOT"][n]
    k = [[1, 3], [3, 1]][n]
    quad = [
        mq.draw_regular_polygon(4, size),
        rectangle,
        rhombus,
        mq.draw_square(size=size, draw='black', fill="white", rotate=45)
    ]
    non_quad = [
        mq.draw_circle(size=3.2, fill='white', draw='black'),
        mq.draw_regular_polygon(3, size),
        shape_1
    ]
    for i in range(5, 9):
        shape = mq.draw_regular_polygon(sides=random.randint(5, 8), size=size)
        non_quad.append(shape)

    choices = random.sample(quad, k=k[0]) + random.sample(non_quad, k=k[1])
    question = f"Which one of these shapes is {is_not} a quadrilateral?"

    answer = choices[[0, 3][n]]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_8(difficulty):
    """Multiple Choice, Choose which shape is/isn't a regular polygon.
    Chrys."""
    n = random.randint(0, 1)
    size = 1.3

    rectangle = r"\tikz \draw (0,0) rectangle (1.5cm,1cm);"
    rhombus = r"\tikz \draw (0,0) -- (%f,0) -- (%f,0.9) -- (%f,0.9) -- (0,0);"\
              % (size-0.4, size + 0.4, 0.8)
    shape_1 = r"""
    \tikz \draw (0,0) -- (%f,0) -- (%f, 0.5) -- (%f,1) -- (0,1) -- (0, 0);
    """ % (size-0.6, size + 0.4, size-0.6)
    irregular_pent = r"""
    \tikz \draw (0.5,0) -- (%f,0) -- (%f,0.8) -- (%f, 1.5) -- (0, 0.8) -- 
    (0.5,0);""" % (size - 0.5, size, size * 0.5)

    is_not = ["", "NOT"][n]

    regular = [mq.draw_square(size + 2, "black", "white", rotate=45)]
    non_reg = [
        mq.draw_triangle(size=size+1, draw="black", fill="white"),
        rhombus,
        irregular_pent,
        rectangle,
        shape_1
    ]
    weights_1 = (72,)
    for i in range(3, 5 + 2 * difficulty):
        shape = mq.draw_regular_polygon(sides=i, size=size)
        regular.append(shape)
        weights_1 = weights_1 + (100 - 7 * i,)

    weights_2 = (difficulty, difficulty, difficulty, 1, 1)

    b = [2, 2, 3][difficulty - 1]
    k = [[1, b], [b, 1]][n]
    choices = []
    while len(choices) != (k[0] + k[1]):
        if difficulty == 1:
            choices = random.sample(regular, k=k[0]) \
                      + random.sample(non_reg, k=k[1])
        else:
            choices_1 = []
            choices_2 = []
            for i in range(k[0]):
                shape_1 = random.choices(regular, weights=weights_1, k=1)[0]
                if shape_1 not in choices_1:
                    choices_1.append(shape_1)
            for j in range(k[1]):
                shape_2 = random.choices(non_reg, weights=weights_2, k=1)[0]
                if shape_2 not in choices_2:
                    choices_2.append(shape_2)
            if len(choices_1) == k[0] and len(choices_2) == k[1]:
                choices = choices_1 + choices_2

    question = f"Which one of these shapes is {is_not} a regular polygon?"
    answer = choices[[0, b][n]]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_9(difficulty):
    """Decide Whether a shape is a polygon or not. Chrys."""
    n = random.randint(0, 1)
    true_false = [True, False]
    polygon = true_false[n]
    if difficulty < 2:
        k = 0
        sides = 4
    else:
        k = random.randint(0, 1)
        sides = random.randint(3, 4)
    shape = mq.draw_random_shape(polygon, curves=(4 - difficulty), sides=sides)
    is_not = ["", "NOT"][k]
    question = f"True or False, this shape is {is_not} a polygon? \n\n {shape}"
    answer = str(true_false[(n + k) % 2])
    choices = [str(i) for i in true_false]
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

    sample = ",\\ ".join(str(nums[i]) for i in range(len(nums)))
    question = f"Find the mean of the following numbers. \n\n {sample}"
    answer = f"{mean(nums)}"
    return [question, answer]


def st_10(difficulty):
    """Find nth Largest/Smallest value using pictogram. Chrys."""
    power = 2 ** (difficulty - 1)
    num_key = random.randint(1, 7 - power) * power
    t = random.randint(0, 1)
    item = [
        ["research company", "scientists", "department"],
        ["shipping company", "ships", "region"]
    ][t]
    col_1 = [
        ["Physics", "Mathematics", "Engineering", "Chemistry"],
        ["Europe", "Asia", "Africa", "Americas"]
    ][t]
    data = [[item[2].capitalize(), f"Number of {item[1].capitalize()}"]]

    angle = [-90, 90, 180]
    values = []
    my_list = []
    k = 0
    choices = col_1
    while len(values) < 4:
        for i in range(4):
            n = random.randint(1, 6)
            if difficulty > 1:
                k = random.randint(0, 1)
            num = n * num_key + (1 - difficulty / 4) * k * num_key
            col_2 = []
            m = []
            for j in range(n):
                m.append(0)
            for r in range(k):
                m.append(difficulty - 1)
            for h in range(len(m)):
                circle = r'''\ \begin{tikzpicture} 
                \filldraw[fill=red, draw=red] (0,0)  arc(%d:270:0.2) --cycle; 
                \end{tikzpicture}''' % angle[m[h]]
                if m[h] > 1:
                    circle = r''' %s
                    \filldraw[fill=red, draw=red] (0,0) -- (0.2,0) -- 
                    (0.2, -0.2); %s ''' % (circle[:21], circle[21:])
                col_2.append(circle)
            if num not in values:
                values.append(num)
                col_2 = "\\ ".join(col_2)
                data.append([col_1[i], col_2])
                my_list.append([col_1[i], num])

    key = r"\textbf{Key}: %s\textbf{ = %s %s}" \
          % (mq.draw_circle(0.2, 'red', 'red'), num_key, item[1].capitalize())
    table = mq.draw_table(data, centered=False)

    m = random.randint(0, len(my_list) - 2)
    a = random.randint(0, 1)
    order = ["smallest", "largest"][a]
    if m == 0:
        ordinal = ""
    else:
        ordinal = num2words(m + 1, ordinal=True)
    if a == 0:
        my_list.sort(key=lambda x: x[1])
    else:
        my_list.sort(key=lambda x: x[1], reverse=True)
    question = f"A {item[0]} made a pictogram to show the number of " \
               f"{item[1]} it has in each {item[2]}. What {item[2]} has " \
               f"the {ordinal} {order} amount of {item[1]}? " \
               f"\n {table} \n\n {key}"
    answer = my_list[m][0]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def st_11(difficulty):
    """Identify smallest/largest value from bar chart. Chrys."""
    k = random.randint(0, 1)
    months = [["May", "June", "July", "August"],
              ["Thursday", "Friday", "Saturday", "Sunday"]][k]
    data = []
    a = random.sample(range(difficulty, 10 * difficulty), k=len(months))
    a = [i * 20 for i in a]
    for i in range(len(months)):
        data.append([r'\small %s' % months[i], str(a[i])])
    label = ["Trees Planted", "Coffees Sold"][k]
    bar_chart = mq.bar_chart(data, size=(6, 7), horizontal=False, label=label)
    n = random.randint(0, 1)
    least_most = ["least", "most"][n]
    true_false = [False, True][n]
    data.sort(key=lambda x: x[1], reverse=true_false)

    items = [
        ["wildlife charity", "trees they planted in each month of summer",
         "month", f"plant the {least_most} trees"],
        ["coffee shop", "coffees they sold each day", "day",
         f"sell the {least_most} coffees"]
        ][k]
    question = f"A {items[0]} made a bar chart showing the number of " \
               f"{items[1]}. What {items[2]} did they {items[3]}? \n\n" \
               + bar_chart
    answer = str(data[0][0])
    return [question, answer]


def st_12(difficulty):
    """Bar chart, identify value of given entry on bar chart. Chrys."""
    data = []
    upper = [10, 10, 20][difficulty-1]
    power = [10, 10, 5][difficulty-1]
    steps = [10, 20, 10][difficulty-1]
    name_bank = []
    for i in range(4):
        a = power * random.randint(1, upper)
        name = names.get_first_name()
        data.append([r'\small %s' % name, str(a)])
        name_bank.append(name)
    n = random.randint(0, len(data) - 1)
    k = random.randint(0, 1)
    horizontal_or_vertical = [True, False][k]
    x_or_y = ["x", "y"][k]
    axis_scale = r'''%stick={0,%s,...,100}, %smin=0, %smajorgrids=true, 
    %s tick label style={font=\small}
    ''' % (x_or_y, steps, x_or_y, x_or_y, x_or_y)
    chart = mq.bar_chart(data, horizontal=horizontal_or_vertical,
                         axis_adj=axis_scale, sym_axis=True, size=(6.5, 7.5))
    question = "The bar chart shows the number of laps swum by " \
               "different swimmers this weekend. How many laps did " \
               f"{name_bank[n]} swim? \n\n {chart}"
    answer = data[n][1]
    return [question, answer]


def st_13(difficulty):
    """Bar chart. Two step money question where student has o work out money
    left over using bar chart. Chrys.
    """
    data = []
    upper = [7, 12, 14][difficulty-1]
    power = [10, 5, 5][difficulty-1]
    steps = [10, 5, 10][difficulty-1]
    lower = [2, 4, 4][difficulty-1]
    cities = ["York", "Glasgow", "Liverpool", "Cardiff"]
    a = random.sample(range(lower, upper+1), k=4)
    a = [power * i for i in a]
    for i in range(4):
        data.append([r'\scriptsize %s' % cities[i], a[i]])
    axis_scale = r'''xtick={0,%s,...,80}, xmin=0, xmajorgrids=true, 
    x tick label style={font=\small}, bar width = 10pt, enlarge y limits=0.25
    ''' % steps
    chart = mq.bar_chart(data, horizontal=True, axis_adj=axis_scale,
                         sym_axis=True, size=(4, 7), fill='red',
                         label="\\small Price in \\textsterling")
    data.sort(key=lambda x: x[1])
    option = ["cheapest", "most expensive"]
    if difficulty == 1:
        m = random.randint(0, 2)
        values = [data[0][1], data[3][1]]
        if m < 2:
            price = values[m]
            choice = f"the {option[m]}"
            s = ""
        else:
            price = sum(values)
            choice = f"both the {option[0]} and the {option[1]}"
            s = "s"
    else:
        n = random.sample(range(len(data)), k=2)
        order = []
        choice = []
        s = "s"
        for i in n:
            if i+1 in [1, 4]:
                order.append(option[i % 2])
                choice.append("")
            else:
                if i+1 < 3:
                    choice.append(option[0])
                    order.append(mq.ordinal(i + 1))
                else:
                    choice.append(option[1])
                    order.append(mq.ordinal(4-i))
        price = data[n[0]][1] + data[n[1]][1]
        choice = f"both the {order[0]} {choice[0]} and the " \
                 f"{order[1]} {choice[1]}"
    num = random.randint(price + 1, 2 * price)
    result = num - price
    gender = random.choice([['male', 'he'], ['female', 'she']])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} has \\textsterling{num:.2f} to spend on travelling. " \
               f"The bar chart shows the prices it will cost to travel to " \
               f"different cities. \n {chart} \nHow much money will " \
               f"{gender[1]} have left over if {gender[1]} travels to " \
               f"{choice} destination{s}."
    answer = f"\\textsterling{result:.2f}"
    return [question, answer]


def st_14(difficulty):
    """Bar chart, difference of two values on bar chart. Chrys."""
    data = []

    n = random.randint(0, 1)
    power = [1, 1, 2][difficulty - 1]
    upper = [14, 25, 12][difficulty - 1]
    lower = [3, 6, 1][difficulty - 1]
    steps = [2, 2, 4][difficulty - 1]

    nums = random.sample(range(lower, upper + 1), k=4)
    nums = [i * power for i in nums]
    today = datetime.today()
    for i in range(4):
        if n == 1:
            day = today - timedelta(days=(i+1))
            title = day.strftime("%A")
        else:
            title = names.get_first_name()
        data.append([r"%s" % title, nums[i]])
    label = ["Number of Articles read", "Number of new customers"][n]

    k = random.randint(0, 1)
    horizontal_or_vertical = [True, False][k]
    x_or_y = ["x", "y"][k]
    axis_scale = r'''%stick={0,%s,...,80}, %smin=0, %smajorgrids=true, 
    tick label style={font=\footnotesize}
    ''' % (x_or_y, steps, x_or_y, x_or_y)
    chart = mq.bar_chart(data, horizontal=horizontal_or_vertical,
                         axis_adj=axis_scale, sym_axis=True, size=(6.5, 7),
                         label=r"\footnotesize %s" % label, fill='yellow')
    item = [
        ["Some students", "in preperation for science fair",
         "articles were read by"],
        ["An electricity company analyst", "they received the past few days",
         "new customers did they receive on"]
    ][n]
    m_1 = random.randint(0, 1)
    values = random.sample(data, k=2)
    by_on = ["by", "on"][n]

    if m_1 == 1:
        m_2 = random.randint(0, 1)
        is_true = [False, True][m_2]
        more_less = ["more", "fewer"][m_2]
        values.sort(key=lambda x: x[1], reverse=is_true)
        item[2] = f"{more_less} {item[2]} {values[1][0]} " \
                  f"than {by_on} {values[0][0]}"
    else:
        item[2] += f" {values[0][0]} and {values[1][0]}"

    result = [values[0][1] + values[1][1],
              abs(values[1][1] - values[0][1])][m_1]

    question = f"{item[0]} kept track of the {label.lower()} {item[1]}. " \
               f"How many {item[2]}? \n" + chart
    answer = mq.dollar(result)
    return [question, answer]


def st_15(difficulty):
    """Bar chart, Find range. Chrys."""
    data = []
    n = random.randint(0, 1)
    upper = [[7, 7, 14], [15, 15, 30]][n][difficulty - 1]
    power = [[1000, 1000, 500], [1, 1, 0.5]][n][difficulty - 1]
    lower = [[1, 1, 2], [11, 11, 22]][n][difficulty - 1]
    steps = [[1000, 2000, 1000], [1, 2, 1]][n][difficulty - 1]
    limit = [8000, 15][n]

    nums = random.choices(range(lower, upper + 1), k=4)
    nums = [power * i for i in nums]

    today = datetime.today()
    for i in range(4):
        if n == 0:
            col_1 = today - timedelta(days=365 * (i + 1))
            col_1 = col_1.strftime("%Y")
        else:
            col_1 = r"Lap %s" % (i + 1)
        data.append([r'\scriptsize %s' % col_1, nums[i]])

    item = random.choice(["wind turbines", "solar panels"])
    label = "\\footnotesize " \
            + [f"Number of {item.title()}", "Time (Seconds)"][n]
    k = random.randint(0, 1)
    horizontal_or_vertical = [True, False][k]
    x_or_y = ["x", "y"][k]
    axis_scale = r'''%stick={0,%s,...,%s}, %smin=0, %smajorgrids=true, 
    %s tick label style={font=\scriptsize}
    ''' % (x_or_y, steps, limit, x_or_y, x_or_y, x_or_y)
    chart = mq.bar_chart(data, horizontal=horizontal_or_vertical, label=label,
                         axis_adj=axis_scale, sym_axis=True, size=(6.5, 7.5))

    question = [
        "An engineering company wants to find out how many "
        f"{item} they created in the past few years. ",
        "A sprinter times how fast how fast they can do a 100m sprint. "][n]
    question += f"What is the range of the {['data', 'timings'][n]}?\n" + chart
    result = round(max(nums) - min(nums), n)
    if result % 1 == 0:
        result = int(result)
    answer = str(result)
    return [question, answer]


def st_16(difficulty):
    """Bar chart, Find the frequency of values more / less than a given number.
    Chrys."""
    data = []
    n = random.randint(0, 1)
    upper = [5, 10, 20][difficulty - 1]
    lower = [1, 1, 2][difficulty - 1]
    power = [4, 2, 1][difficulty - 1]
    steps = [4, 2, 2][difficulty - 1]
    limit = 32

    nums = random.choices(range(lower, upper + 1), k=6)
    nums = [power * i for i in nums]

    for i in range(len(nums)):
        col_1 = i + n
        data.append([r'\scriptsize %s' % col_1, nums[i]])

    label = "\\footnotesize Frequency"
    label_x = "\\footnotesize " + ["Goals", "Dice Number"][n]

    k = random.randint(0, 1)
    horizontal_or_vertical = [True, False][k]
    x_y = ["x", "y"]
    x_or_y = x_y[k]
    axis_scale = r'''%stick={0,%s,...,%s}, %smin=0, %smajorgrids=true, 
    %s tick label style={font=\scriptsize}, %slabel=%s
    ''' % (x_or_y, steps, limit, x_or_y, x_or_y,
           x_or_y, x_y[(k + 1) % 2], label_x)
    colour = random.choice(["red", "blue", "green", "teal"])
    chart = mq.bar_chart(data, horizontal=horizontal_or_vertical, label=label,
                         axis_adj=axis_scale, sym_axis=True, size=(6.5, 7.5),
                         fill=colour)

    a = random.randint(1, 4)
    m = random.randint(0, 1)
    more_less = ["less", "more"][m]
    result = 0
    for j in range(a + m):
        result += nums[j]
    result = [result, sum(nums) - result][m]

    question = "The bar chart shows the number of "

    question += [
        "goals scored by athletes in a sports competition.",
        "times each number was thrown when a dice was thrown repeatedly."][n]
    item = [["people scored", " goals"], ["times did they role", ""]][n]
    question += f"How many {item[0]} {more_less} than {a + n}{item[1]}? \n" \
                + chart
    answer = str(result)
    return [question, answer]


def st_17(difficulty):
    """Bar chart, find mean using bar chart. Chrys."""
    data = []
    n = random.randint(0, 1)
    upper = [[12, 10, 20], [10, 10, 15]][n][difficulty - 1]
    power = [[1, 2, 1], [10, 10, 5]][n][difficulty - 1]
    lower = [2, 1, 2][difficulty - 1]
    steps = [[1, 2, 2], [10, 20, 10]][n][difficulty - 1]
    limit = [32, 120][n]

    nums = []
    while len(nums) < 4:
        values = random.choices(range(lower, upper + 1), k=4)
        values = [power * i for i in values]
        if mean(values) % 1 == 0:
            nums = values

    book_genre = random.sample(["Sci-Fi", "Fantasy", "Action",
                                "History", "Mythology", "Science"], k=4)
    for i in range(len(nums)):
        if n == 0:
            col_1 = names.get_first_name()
        else:
            col_1 = book_genre[i]
        data.append([r'\scriptsize %s' % col_1, nums[i]])

    label = "\\footnotesize " \
            + ["Distance (Kilometres)", "Number of Books Sold"][n]

    k = random.randint(0, 1)
    horizontal_or_vertical = [True, False][k]
    x_or_y = ["x", "y"][k]
    axis_scale = r'''%stick={0,%s,...,%s}, %smin=0, %smajorgrids=true, 
    %s tick label style={font=\scriptsize}
    ''' % (x_or_y, steps, limit, x_or_y, x_or_y, x_or_y)
    colour = random.choice(["red", "blue", "green", "teal"])
    chart = mq.bar_chart(data, horizontal=horizontal_or_vertical, label=label,
                         axis_adj=axis_scale, sym_axis=True, size=(6.5, 7.5),
                         fill=colour)
    item = [
        ["group of cyclists", "distance they cycled today", "distance cycled"],
        ["bookshop",
         "amount of books sold today from their most popular genres",
         "amount of books sold"]
    ][n]
    question = f"A {item[0]} made a bar chart recording the {item[1]}." \
               f"What is the mean {item[2]}? \n" + chart
    answer = str(mean(nums))
    return [question, answer]


def st_2(difficulty):
    """Range of a group of numbers. Chrys."""
    lower = 10 ** (difficulty - 1) - 1
    upper = 10 ** (difficulty + 1) - 1
    k = random.randint(5, 9 - difficulty)
    nums = random.sample(range(lower, upper), k=k)

    sample = ",\\ ".join(str(i) for i in nums)
    question = "Find the range of the following numbers. \n\n " \
               f"\\begin{{center}} {sample} \\end{{center}}"
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


def st_4(difficulty):
    """Probability question, chance of selecting a specified shape. Chrys."""
    r = 'r'
    shapes = []
    choices = ['Circle', 'Square',
               'Equally Likely']

    if difficulty == 3:
        quant_1 = random.choices(range(1, 2), k=2)
        quant_1.append(max(quant_1) + 1)
        random.shuffle(quant_1)
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
    random.shuffle(shapes)

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
    return mq.multiple_choice(question, choices, answer, onepar=False)


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

    question = f"Here are the results of some market research on the {items}" \
               f" by some {shop_type.lower()}. " \
               f"Find the mean value of the results? \n\n" \
               f"\\begin{{center}} {mq.draw_table(data)} \\end{{center}}"
    answer = mq.dollar(mean(values))
    return [question, answer]


def st_6(difficulty):
    """Read the values from a pictogram. Chrys."""
    power = 2 ** (difficulty - 1)
    num_key = random.randint(1, 7 - power) * power

    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']
    data = [['Day', 'Number Sold']]
    values = []

    angle = [-90, 90, 180]

    k = 0
    for i in range(7):
        n = random.randint(1, 6)
        if difficulty > 1:
            k = random.randint(0, 1)
        num = n * num_key + (1 - difficulty / 4) * k * num_key
        values.append(num)

        col_2 = []
        m = []
        for j in range(n):
            m.append(0)
        for r in range(k):
            m.append(difficulty - 1)
        for h in range(len(m)):
            circle = r'''\ \begin{tikzpicture} 
            \filldraw[fill=red, draw=red] (0,0)  arc(%d:270:0.2) --cycle; 
            \end{tikzpicture}''' % angle[m[h]]
            if m[h] > 1:
                circle = r''' %s
                \filldraw[fill=red, draw=red] (0,0) -- (0.2,0) -- (0.2, -0.2);
                 %s ''' % (circle[:21], circle[21:])
            col_2.append(circle)
        col_2 = "\\ ".join(col_2)
        data.append([day_name[i], col_2])

    key = r"\textbf{Key}: %s\textbf{ = %s Pizzas}" \
          % (mq.draw_circle(0.2, 'red', 'red'), num_key)
    table = mq.draw_table(data, centered=False)

    a = random.randint(0, 6)
    question = "A restaurant made a pictogram to show the number of pizzas " \
               "sold in a day. How many pizzas did they sell on " \
               f"{day_name[a]}? \n {table} \n\n {key}"
    answer = str(int(values[a]))
    return [question, answer]


def st_7(difficulty):
    """Find total using pictogram. Chrys."""
    multiplier = [1, 2, 2][difficulty - 1]
    key_value = random.randint(difficulty, 2 + difficulty) * multiplier
    data = [['Week', 'Number Sold']]

    square = mq.draw_square(0.1, 'cyan', 'cyan', rotate=45)
    total = 0
    for i in range(4):
        n = random.randint(1, 5)
        k = 0
        if difficulty > 1:
            k = random.randint(0, 1)
        num = n * key_value + 0.5 * k * key_value
        total = total + num

        col_2 = []
        for j in range(n):
            col_2.append(square)
        for r in range(k):
            half = r'''\tikz 
            \filldraw[fill=cyan, draw=cyan] (0,0.3) -- (0.3,0) -- (0.6,0.3);'''
            col_2.append(half)

        col_2 = "\\ ".join(col_2)
        data.append([f"Week {i + 1}", col_2])

    item = random.choice([['pet', 'hamsters'], ['jewellery', 'rings']])
    key = r"\textbf{Key}: %s\textbf{ = %s %s}" \
          % (square, key_value, item[1].capitalize())
    table = mq.draw_table(data, centered=False)
    question = f"A {item[0]} shop made a pictogram to show how many {item[1]}"\
               f" they sold in each week of last month. Find the total " \
               f"amount of {item[1]} sold in the month. \n {table} \n {key}"
    answer = mq.dollar(int(total))
    return [question, answer]


def st_8(difficulty):
    """Find mean using pictogram. Chrys."""
    multiplier = [1, 2, 2][difficulty - 1]
    key_value = random.randint(difficulty, 3 + difficulty) * multiplier

    m = random.randint(0, 1)
    item = [["zoo", "exhibit"], ["town", "park"]][m]
    data = [[item[1].capitalize(), "Visitors"]]

    col_1 = [
        ["Lions", "Tigers", "Pandas", "Elephants"],
        [
            ["Mossy", "Gardens"], ["Castle", "Plaza"],
            ["Willows", "Grounds"], ["Forest", "Lake"]
         ]
    ][m]
    square = mq.draw_square(0.1, 'orange', 'orange', rotate=45)

    result = 0
    col_2 = []
    while result < 1:
        values = []
        col_2 = []
        for i in range(4):
            n = random.randint(1, 5)
            k = 0
            if difficulty > 1:
                k = random.randint(0, 1)
            values.append(n * key_value + 0.5 * k * key_value)
            my_list = []
            for j in range(n):
                my_list.append(square)
            for r in range(k):
                half = r'''\tikz \filldraw[fill=orange, draw=orange] 
                (0,0.3) -- (0.3,0) -- (0.6,0.3);'''
                my_list.append(half)
            my_list = "\\ ".join(my_list)
            col_2.append(my_list)
        if mean(values) % 1 == 0:
            result = int(mean(values))
            col_2 = col_2

    for h in range(4):
        if m == 1:
            data.append(
                [r"\shortstack{%s\\%s}" % (col_1[h][0], col_1[h][1]), col_2[h]]
            )
        else:
            data.append([col_1[h], col_2[h]])
    key = r"\textbf{Key}: %s\textbf{ = %s %s}" \
          % (square, key_value, 'Visitors')
    table = mq.draw_table(data, centered=False)
    question = f"A {item[0]} made a pictogram to show how many visitors"\
               f" each {item[1]} received in an hour. Find the mean " \
               f"amount of visitors. \n {table} \n {key}"
    answer = mq.dollar(result)
    return [question, answer]


def st_9(difficulty):
    """Find range using pictogram. Chrys."""
    multiplier = [1, 2, 2][difficulty - 1]
    key_value = random.randint(difficulty * 3, 6 * difficulty) * multiplier

    m = random.randint(0, 1)
    item = [
        ["farmer", "animals", "live on the farm"],
        ["racing team", "points", "they won each race"]][m]
    title = ["Animal", "Race"][m]
    data = [[title, f"Number of {item[1].capitalize()}"]]

    col_1 = [
        ["Pigs", "Sheep", "Hens", "Cows"],
        [["The", "Oval"], ["Bay", "Circuit"],
         ["Heritage", "Track"], ["Bracknell", "Course"]]
    ][m]
    square = mq.draw_square(0.1, 'red', 'red', rotate=45)

    values = []
    for i in range(4):
        n = random.randint(1, 5)
        k = 0
        if difficulty > 1:
            k = random.randint(0, 1)
        num = n * key_value + 0.5 * k * key_value
        values.append(num)
        col_2 = []
        for j in range(n):
            col_2.append(square)
        for r in range(k):
            half = r'''\tikz \filldraw[fill=red, draw=red] 
            (0,0.3) -- (0.3,0) -- (0.6,0.3);'''
            col_2.append(half)
        col_2 = "\\ ".join(col_2)
        if m == 1:
            data.append(
                [r"\shortstack{%s\\%s}" % (col_1[i][0], col_1[i][1]), col_2])
        else:
            data.append([col_1[i], col_2])
    values.sort()
    result = values[len(values) - 1] - values[0]

    key = r"\textbf{Key}: %s\textbf{ = %s %s}" \
          % (square, key_value, item[1].capitalize())
    table = mq.draw_table(data, centered=False)
    question = f"A {item[0]} made a pictogram to show how many {item[1]}"\
               f" {item[2]}. Find the range " \
               f"of the data. \n {table} \n {key}"
    answer = mq.dollar(int(result))
    return [question, answer]


def st_18(difficulty):
    """Find mean from tally chart. Chrys."""
    data = []
    n = random.randint(2 + difficulty, 3 + difficulty)
    towns = ["Northfield", "Lunatown", "Postport", "Highborough",
             "Hardstead", "Roseville", "Fayview", "Capville", "Maytown"]
    towns = random.sample(towns, k=n)
    item = random.choice([["Train", "train operator"],
                          ["Fire", "fire service"]])

    k = random.randint(0, 1)
    title = [["Name", "Score"], ["Town", f"Number of Stations"]][k]
    data.append(title)
    col_2 = []
    while len(col_2) < n:
        nums = random.sample(range(2, 10 * difficulty), k=n)
        if mean(nums) % 1 == 0:
            col_2 = nums
    colour = random.choice(['blue', 'red', 'teal'])
    for i in range(n):
        if k == 0:
            col_1 = names.get_first_name()
        else:
            col_1 = towns[i]
        tally = mq.draw_tally(col_2[i], colour)
        data.append([col_1, tally])
    table = mq.draw_table(data, centered=False)

    items = [
        ["Some friends", "their scores in a quiz"],
        [f"A {item[1]}",
         f"the amount of {item[0].lower()} stations they have in some cities"]
    ][k]
    question = f"{items[0]} recorded {items[1]}. " \
               f"What is the mean of the results? \n\n" + table
    answer = mq.dollar(mean(col_2))
    return [question, answer]


def st_19(difficulty):
    """Find range from tally chart. Chrys."""
    data = []
    k = random.randint(0, 1)
    col_1 = [["North", "East", "South", "West", "Central"],
             ["Ice Valley", "Editfield", "Stellar City",
              "Metro Town", "Mountain North"]][k]
    title = [["Region", "Number of Hotels"], ["Town", "Number of Houses"]][k]
    data.append(title)

    nums = random.choices(range(4 * difficulty, 11 * difficulty), k=5)
    colour = random.choice(['blue', 'red', 'teal'])
    for i in range(5):
        tally = mq.draw_tally(nums[i], colour)
        data.append([col_1[i], tally])
    table = mq.draw_table(data, centered=False)
    question = ["A tourism company wanted to find out how"
                " many hotels are in each region in a town.",
                "An estate agent records how many houses "
                "have been sold in different towns."][k]
    question += " What is the range of the results? \n\n" + table
    answer = mq.dollar(max(nums) - min(nums))
    return [question, answer]


def st_20(difficulty):
    """Tally Chart, Find quantity of entries that are more/less than a given
    amount. Chrys."""
    data = []
    k = random.randint(0, 1)
    col_1 = [
        ["Robins", "Squirrels", "Rabbits",
         "Butterflies", "Blackbirds", "Deers"],
        ["Maths", "Science", "Art", "Music",
         "English", "Physical Education"]][k]

    title = [["Animal", "Amount Seen"], ["Subject", "Exam Score"]][k]
    data.append(title)

    nums = random.sample(range(4 * difficulty, 10 * difficulty), k=5)
    colour = random.choice(['blue', 'red', 'teal'])
    values = []
    for i in range(5):
        tally = mq.draw_tally(nums[i], colour)
        data.append([col_1[i], tally])
        values.append([col_1[i], nums[i]])
    table = mq.draw_table(data, centered=False)
    values.sort(key=lambda x: x[1])
    a = random.randint(min(nums) + 1, max(nums) - 1)
    m = random.randint(0, 1)
    more_less = ["more", "less"][m]
    result = 0
    if m == 1:
        for j in range(5):
            if nums[j] < a:
                result = result + 1
            else:
                result = result
    else:
        for j in range(5):
            if nums[j] > a:
                result = result + 1
            else:
                result = result
    gender = random.choice([["male", "his", "he"], ["female", "her", "she"]])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} records"
    question += ["the different types of animal seen "
                 "whilst on a walk through through the forest. ",
                 f"{gender[1]} exam scores for different subjects. "][k]
    item = [
        f"different animals did {gender[2]} "
        f"see {more_less} than {a} times",
        f"times did {gender[2]} score {more_less} than {a} marks?"
    ][k]
    question += f"How many {item} \n\n" + table
    answer = str(result)
    return [question, answer]


def st_21(difficulty):
    """Find nth highest and different between two values. Chrys."""
    data = []
    k = random.randint(0, 1)
    col_1 = [
        ["Red", "Yellow", "Blue", "Green", "Purple", "Pink", "Grey"],
        ["Apple", "Banana", "Mango", "Pear", "Orange", "Melon", "Pineapple"]
    ][k]
    col_1 = random.sample(col_1, k=5)
    title = [["Colour", "Frequency"],
             ["Fruit", "Frequency"]][k]
    data.append(title)

    nums = random.sample(range(4 * difficulty, 15 * difficulty), k=5)
    colour = random.choice(['blue', 'red', 'teal'])
    values = []
    for i in range(5):
        tally = mq.draw_tally(nums[i], colour)
        data.append([col_1[i], tally])
        values.append([col_1[i], nums[i]])
    table = mq.draw_table(data, centered=False)

    item = ["colour", "fruit"][k]
    question = f"Some people were asked what their favourite {item} is. " \
               "The results are presented in a tally chart. "

    values.sort(key=lambda x: x[1], reverse=True)
    n = random.sample(range(0, 4), k=2)
    n.sort(reverse=True)
    ordinal = []
    order = []
    for j in range(2):
        if n[j] > 2:
            order.append("least")
            if n[j] == 3:
                ordinal.append("2nd")
            else:
                ordinal.append("")
        else:
            order.append("most")
            if n[j] == 0:
                ordinal.append("")
            else:
                ordinal.append(mq.ordinal(n[j]+1))

    if difficulty == 1:
        question += f"What is the {ordinal[0]} {order[0]} popular {item}?"
        result = values[n[0]][0]
    else:
        question += f"How much more people prefer the {ordinal[1]} " \
                    f"{order[1]} popular {item} than the {ordinal[0]} " \
                    f"{order[0]} popular {item}?"
        result = values[n[1]][1] - values[n[0]][1]
    question += "\n\n" + table
    answer = mq.dollar(result)
    return [question, answer]


def me_37(difficulty):
    """Find journey time using timetable"""
    no_trains = difficulty + 3
    departures = []
    durations = []

    trains = [['Train', 'Departure', 'Arrival']]

    while len(durations) < no_trains:
        check = []
        start_time = random.sample(range(0, 1438), k=no_trains)
        start_time.sort()
        for i in range(no_trains):
            length = random.randint(1, 1439 - start_time[i])
            if length not in check:
                check.append(length)
        if len(check) == no_trains:
            durations = check
            departures = start_time
    values = []
    for j in range(no_trains):
        trains.append([str(j + 1), mq.minutes_to_time(departures[j]),
                       mq.minutes_to_time(departures[j] + durations[j])])
        values.append([str(j + 1), mq.minutes_to_time(departures[j]),
                       mq.minutes_to_time(departures[j] + durations[j]),
                       durations[j]])
    table = mq.draw_table(trains)
    n = random.randint(0, 1)
    if n == 1:
        choice = random.choice(values)
        question = f"In minutes, how long is the journey for " \
                   f"Train {choice[0]}?"
        hour = floor(choice[3] / 60)
        minutes = choice[3] - hour * 60
        if hour == 0:
            answer = f"{choice[3]} minutes"
        elif hour == 1:
            answer = f"{hour} hour and {minutes} minutes"
        else:
            answer = f"{hour} hours and {minutes} minutes"
    else:
        choice = random.choice(['shortest', 'longest'])
        question = f"Which train has the {choice} journey time?"
        values.sort(key=lambda x: x[3])
        if choice == 'shortest':
            answer = f"Train {values[0][0]}"
        else:
            answer = f"Train {values[no_trains-1][0]}"
    question += f"\n\n {table}"
    return [question, answer]


def me_38(difficulty):
    """Identify start/end time of a given event from a timetable. Chrys."""
    no_events = difficulty + 2

    data = [['Event', 'Start', 'End']]
    events = ['Ski Jumping', 'Snowboarding', 'Bobsled', 'Curling', 'Biathlon',
              'Figure Skating', 'Hockey', 'Speed Skating', 'Cross Country']
    events = random.sample(events, k=no_events)

    start_time = random.sample(range(540, 1080), k=no_events)
    start_time.sort()
    end_time = []
    while len(end_time) < no_events:
        list_1 = []
        list_2 = []
        for i in range(no_events):
            length = random.randint(30, 120 + 60 * difficulty)
            end = start_time[i] + length
            if end not in list_1:
                list_1.append(end)
                list_2.append(length)
        if len(list_1) == no_events:
            end_time = list_1

    values = []
    for j in range(no_events):
        data.append([events[j], mq.minutes_to_time(start_time[j]),
                    mq.minutes_to_time(end_time[j])])
        values.append([events[j], mq.minutes_to_time(start_time[j]),
                       mq.minutes_to_time(end_time[j])])
    table = mq.draw_table(data)

    choice = random.choice(values)
    n = random.randint(0, 1)
    result = [['start', choice[1]], ['end', choice[2]]][n]
    question = f"When does the {choice[0]} event {result[0]}? \n\n {table}"
    answer = result[1]
    return [question, answer]


def me_39(difficulty):
    """Find gap between two events on a timetable. Chrys."""
    no_events = 4 + difficulty

    start = []
    end = []
    durations = []
    gap = []

    data = [['Class', 'Start', 'End']]
    n = random.randint(0, 1)
    col_1 = [['Tennis', 'Badminton', 'Gymnastics', 'Boxing'
              'Squash', 'Spin', 'Dance', 'Rock Climbing', 'Yoga'],
             ['Math', 'Physics', 'Chemistry', 'Biology', 'Computing', 'P.E.',
              'English', 'Psychology', 'Religion', 'Philosophy', 'Business']
             ][n]
    col_1 = random.sample(col_1, k=no_events)

    start_0 = random.randint(420, 480)
    my_list = [start_0]
    lengths = random.sample(range(20, 80), k=2*no_events - 1)
    for i in range(2 * no_events - 1):
        my_list.append(my_list[i] + lengths[i])
    for j in range(0, len(my_list), 2):
        start.append(my_list[j])
        end.append(my_list[j+1])
    for m in range(0, len(lengths), 2):
        durations.append(lengths[m])
    for k in range(1, len(lengths), 2):
        gap.append(lengths[k])
    values = []
    for q in range(no_events):
        data.append([col_1[q], mq.minutes_to_time(start[q]),
                    mq.minutes_to_time(end[q])])
        values.append([col_1[q], mq.minutes_to_time(start[q]),
                      mq.minutes_to_time(end[q])])
    table = mq.draw_table(data)
    choice_1 = random.randint(0, len(values) - 1 - difficulty)
    choice_2 = choice_1 + difficulty
    gender = random.choice([['male', 'his', 'he'], ['female', 'her', 'she']])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} has just finished {values[choice_1][0]} class. How " \
               f"long will {gender[2]} have to wait until {gender[1]} " \
               f"{values[choice_2][0]} class starts? Write your answer in " \
               f"minutes. \n\n {table}"
    result = start[choice_2] - end[choice_1]
    answer = f"{result} minutes."
    return [question, answer]


def me_40(difficulty):
    """Find time until an event on a timetable. Chrys."""
    no_events = 5 + difficulty
    n = random.randint(0, 1)
    item = [['Flight', 'airport'], ['Train', 'station']][n]
    col_1 = [['Athens', 'Rome', 'Madrid', 'Prague', 'Sydney', 'Manila',
              'Dubai', 'Dublin', 'Toronto', 'Cape Town', 'Mexico City',
              'Moscow', 'Nairobi', 'Lisbon', 'Hong Kong'],
             ['Glasgow', 'Edinburgh', 'Manchester', 'Liverpool', 'Canterbury',
              'Brighton', 'Cambridge', 'Oxford', 'Leeds', 'Bradford', 'Hull',
              'Nottingham', 'Sunderland', 'Newcastle', 'Leicester']][n]
    col_1 = random.sample(col_1, k=no_events)

    option = random.choice([['Departure', 'depart', 'Destination', 'to'],
                            ['Arrival', 'arrive', 'Arriving From', 'from']])
    data = [[f'{option[2]}', f'{option[0]} Time']]
    start = random.sample(range(240, 1339), k=no_events)
    start.sort()
    values = []
    for i in range(no_events):
        data.append([col_1[i], mq.minutes_to_time(start[i])])
        values.append([col_1[i], mq.minutes_to_time(start[i])])
    choice = random.randint(0, len(values) - 1)
    length = random.randint(30 * difficulty, 60 * difficulty)
    x = mq.minutes_to_time(start[choice] - length)

    hour = floor(length / 60)
    minutes = length - hour * 60
    if hour == 0:
        time_1 = f"{minutes} minute"
    else:
        if hour == 1:
            time_1 = f"{hour} hour"
        else:
            time_1 = f"{hour} hours"
        if minutes > 0:
            time_1 += f" and {minutes} minute"
    if minutes > 1:
        time_1 += 's'

    gender = random.choice([['male', 'He'], ['female', 'She']])
    name = names.get_first_name(gender=gender[0])
    table = mq.draw_table(data)
    question = f"{name} is waiting for the {item[0].lower()} {option[3]} " \
               f"{values[choice][0]} to {option[1]}. {gender[1]} arrives at " \
               f"the {item[1]} at {x}. How long will {gender[1].lower()} " \
               f"have to wait until the {item[0].lower()} " \
               f"{option[1]}s? \n\n {table}"
    answer = time_1
    return [question, answer]


def sh_16(difficulty):
    angle = random.randint(10, 50 * difficulty)
    shape = r'''
    \begin{tikzpicture}
    \draw[fill=blue!30] (0,0) -- (%d:.8cm) arc (%d:180:.8cm);
    \draw[fill=green!30] (0,0) -- (0:.8cm) arc (0:%d:.8cm);
    \draw (0,0) -- (%d:2.5cm);
    \draw (-2,0) -- (2,0);
    \draw(%f:0.4cm) node {$%d\degree$};
    \draw(%f:0.5cm) node {$x$};
    \end{tikzpicture}
    ''' % (angle, angle, angle, angle, (180 + angle) / 2, 180 - angle,
           angle / 2)
    question = "Calculate the missing angle.\n\n" \
               + shape
    answer = mq.dollar(f"{angle}\\degree")
    return [question, answer]


def st_22(difficulty):
    """Probability question, how likely is it to select a certain colour.
    Multiple choice. Chrys."""
    r = 'r'
    shapes = []
    no_shapes = [3, 5, 7][difficulty - 1]

    quant_0 = random.randint(0, no_shapes)
    quant = [quant_0, no_shapes - quant_0]

    colour = random.sample(['red', 'blue', 'green', 'yellow'], k=2)

    for i in range(quant[0] + quant[1]):
        r += 'r'
    for j in range(quant[0]):
        shapes.append(mq.draw_circle(fill=colour[0]))
    for m in range(quant[1]):
        shapes.append(mq.draw_circle(fill=colour[1]))

    random.shuffle(shapes)
    n = quant[0] + quant[1]
    joined_shapes = '&'.join(map(str, [shapes[i] for i in range(n)]))

    model = r'''
    \begin{center}
    {\arraycolsep=2pt\LARGE$\begin{array}{%s} %s \end{array}$} 
    \end{center}
    ''' % (r, joined_shapes)

    choices = ['Certain', 'Probable', 'Unlikely', 'Impossible']
    if quant[0] == no_shapes:
        result = choices[0]
    elif quant[0] == 0:
        result = choices[3]
    elif 0 < quant[0] < quant[1]:
        result = choices[2]
    else:
        result = choices[1]

    question = "If you were to pick one circle, how likely is it that the " \
               f"circle would be coloured {colour[0]}? \n\n {model}"
    answer = result
    return mq.multiple_choice(question, choices, answer, reorder=False)


def st_23(difficulty):
    """Interpret line graph to find value for specific x parameter. Chrys."""
    data = []
    n = random.randint(0, 1)
    months = [['January', 'February', 'March', 'April'],
              ['September', 'October', 'November', 'December']][n]
    time_of_year = ['first', 'last'][n]

    for i in range(len(months)):
        if difficulty == 1:
            a = random.randint(1, 10)
        elif difficulty == 2:
            a = round(random.randint(1, 10) / 2, 1)
        else:
            a = round(random.randint(2, 14) / 2, 1)
        data.append([months[i], a])
    increments = [1, 0.5, 1][difficulty - 1]

    axis_adj = r'''
    ytick={0,%s,...,10}, ymin=0, 
    x tick label style={font=\small, rotate=45}, 
    y tick label style={font=\small},
    y label style={font=\small, yshift=-12pt}, height=7cm, width = 9cm
    ''' % increments
    title = '\\normalsize \\textbf{Average Monthly Rainfall in London}'
    y_label = 'Average Rainfall (cm)'
    model = mq.draw_line_graph(data, sym_axis=True, scale=0.85, grid=True,
                               axis_adj=axis_adj, title=title, y_label=y_label)

    choice = random.choice(data)

    question = f"A meteorologist keeps track of the average monthly " \
               f"rainfall in london for the {time_of_year} four months of " \
               f"the year. On average, how much did it rain in {choice[0]}?" \
               f"\n\n {model}"
    if choice[1] % 1 == 0:
        choice[1] = round(choice[1])
    answer = f"{choice[1]}cm"
    return [question, answer]


def st_24(difficulty):
    """Interpret line chart to find largest/smallest of two given values and
    find difference in size. Chrys."""
    data = []
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    upper = [10, 6, 10][difficulty - 1]
    nums = random.sample(range(1, upper), k=5)
    a = [2, 5, 5][difficulty - 1]
    nums = [i * a for i in nums]

    for i in range(len(day)):
        data.append([day[i], nums[i]])
    increments = [2, 5, 10][difficulty - 1]

    axis_adj = r'''
    ytick={0,%s,...,100}, ymin=0, 
    x tick label style={font=\small, rotate=45}, 
    y tick label style={font=\small},
    y label style={font=\small, yshift=-12pt}, height=7cm, width = 9cm
    ''' % increments
    title = '\\normalsize \\textbf{Cakes Left Over Each Day}'
    y_label = 'Number of Cakes'
    model = mq.draw_line_graph(data, sym_axis=True, scale=0.85, grid=True,
                               axis_adj=axis_adj, title=title, y_label=y_label)

    values = random.sample(data, k=2)
    values.sort(key=lambda x: x[1])

    question = "A bakery keeps track of the cakes they have left " \
               "over in the past week. "

    n = random.randint(0, 1)
    more_less = ["less", 'more'][n]

    additional_text = [f"What day has {more_less} cakes left over, "
                       f"{values[0][0]} or {values[1][0]}?",
                       f"How many {more_less} cakes are left over "
                       f"on {values[n][0]} than on {values[(n + 1) % 2][0]}?"]
    result = [[values[0][0], values[1][0]][n], values[1][1] - values[0][1]]

    k = [0, random.choices([0, 1], weights=(1, 4), k=1)[0], 1][difficulty - 1]
    question += additional_text[k]

    answer = str(result[k])
    question = question + model
    return [question, answer]


def st_25(difficulty):
    """Find range using line graph. Chrys."""
    data = []

    no_years = 4
    upper = [10, 10, 10][difficulty - 1]
    nums = random.choices(range(1, upper), k=5)
    a = [5, 10, 20][difficulty - 1]
    nums = [i * a for i in nums]

    today = datetime.today()
    for i in range(no_years):
        year = today - timedelta(weeks=52 * i)
        year = year.strftime("%Y")
        data.append([year, nums[i]])
    increments = [5, 10, 20][difficulty - 1]

    item = random.choice(["chess competition", "football tournament",
                          "science fair"])
    axis_adj = r'''
    ytick={0,%s,...,200}, ymin=0, 
    x tick label style={font=\small, rotate=45}, 
    y tick label style={font=\small},
    y label style={font=\small, yshift=-12pt}, height=7cm, width = 9cm
    ''' % increments
    title = r'\small \textbf{%s Entries Per Year.}' \
            % item.title()
    y_label = 'Number of People'
    model = mq.draw_line_graph(data, sym_axis=True, scale=0.85, grid=True,
                               axis_adj=axis_adj, title=title, y_label=y_label)

    name = names.get_first_name()

    question = f"{name} keeps track of the number of people who take part in" \
               f"a {item} over the past 4 years. Find the range of the data." \
               f"\n{model}"
    answer = str(max(nums) - min(nums))
    return [question, answer]


def st_26(difficulty):
    """Interpret line graph to find which x entry matches a given y value.
    Chrys."""
    data = []

    no_months = 2 + difficulty
    upper = [7, 12, 12][difficulty - 1]
    nums = random.sample(range(1, upper), k=5)
    a = [100, 50, 50][difficulty - 1]
    nums = [i * a for i in nums]

    months = ["January", "February", "March", "April", "May"]
    for i in range(no_months):
        data.append([months[i], nums[i]])
    increments = [100, 50, 50][difficulty - 1]

    axis_adj = r'''
    ytick={0,%s,...,1000}, ymin=0, 
    x tick label style={font=\small, rotate=0}, 
    y tick label style={font=\small},
    y label style={font=\small, yshift=-12pt}, height=8.5cm, width = 9cm
    ''' % increments
    title = r'\small \textbf{Cost of Bills by Month}'

    y_label = 'Amount Spent (\\textsterling)'
    model = mq.draw_line_graph(data, sym_axis=True, scale=0.85, grid=True,
                               axis_adj=axis_adj, title=title, y_label=y_label)

    gender = random.choice([['male', 'he'], ['female', 'she']])
    name = names.get_first_name(gender=gender[0])
    choices = [months[i] for i in range(no_months)]
    result = random.choice(data)

    question = f"{name} is keeping track of the amount {gender[1]} spends on" \
               f" bills in the first {no_months} months of the year. " \
               f"On what month did {gender[1]} spend " \
               f"\\textsterling{result[1]} on bills? \n{model}"
    answer = result[0]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def st_27(difficulty):
    """Use line graph to find nth largest/smallest value. Chrys."""
    data = []

    no_weeks = 4
    upper = [8, 8, 12][difficulty - 1]
    nums = random.sample(range(1, upper), k=5)
    a = [200, 1000, 500][difficulty - 1]
    nums = [i * a for i in nums]

    weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]

    for i in range(no_weeks):
        data.append([weeks[i], nums[i]])
    increments = [200, 1000, 500][difficulty - 1]
    item = random.choice(['cars', 'fridges', 'telephones', 'tablets'])

    axis_adj = r'''
    ytick={0,%s,...,10000}, ymin=0, 
    x tick label style={font=\small, rotate=0}, 
    y tick label style={font=\small},
    y label style={font=\small, yshift=-2.5pt}, height=8.5cm, width = 8.2cm
    ''' % increments
    title = r'\small \textbf{Amount of %s Sold in a Month}' % item.title()

    y_label = 'Number Sold'
    model = mq.draw_line_graph(data, sym_axis=True, scale=0.85, grid=True,
                               axis_adj=axis_adj, title=title, y_label=y_label)
    data.sort(key=lambda x: x[1])
    n = random.randint(0, len(data) - 1)
    if n == 1 or n == 2:
        ordinal = mq.ordinal(2)
    else:
        ordinal = ''
    if n < 2:
        order = 'least'
    else:
        order = 'most'
    choices = weeks
    question = f"A salesman keeps track of the amount of {item} sold over " \
               f"a month. What week did the salesman sell the {ordinal} " \
               f"{order} {item}? \n{model}"
    answer = data[n][0]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def st_28(difficulty):
    """Find mean using data from line graph. Chrys."""
    data = []

    no_days = 3 + difficulty
    upper = [10, 12, 12][difficulty - 1]
    nums = []
    while len(nums) < no_days:
        values = random.choices(range(1, upper), k=no_days)
        a = [2, 1, 1][difficulty - 1]
        values = [i * a for i in values]
        if mean(values) % 1 == 0:
            nums = values

    for i in range(no_days):
        data.append([f"{i + 1}", nums[i]])
    increments = [2, 1, 1][difficulty - 1]
    item = random.choice(['cycled', 'walked', 'swam'])

    axis_adj = r'''
    ytick={0,%s,...,40}, ymin=0, 
    x tick label style={font=\small, rotate=0}, 
    y tick label style={font=\small},
    y label style={font=\normalsize, yshift=-12pt}, height=8.5cm, width=8.2cm,
    x label style = {font=\normalsize}
    ''' % increments
    title = r'\normalsize \textbf{Distance Travelled Each Day}'

    y_label = 'Distance (km)'
    x_label = 'Day'
    model = mq.draw_line_graph(data, sym_axis=True, scale=0.85, grid=True,
                               axis_adj=axis_adj, title=title, y_label=y_label,
                               x_label=x_label)
    gender = random.choice([['male', 'he', 'his'], ['female', 'she', 'her']])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} keeps track of the distance {gender[1]} {item} on " \
               f"each day of {gender[2]} holiday. What is the mean of the " \
               f"data? \n{model}"
    answer = mq.dollar(mean(nums))
    return [question, answer]


def pv_16(difficulty):
    """Are the values in a sequence increasing or decreasing. Multiple Choice.
     Chrys."""
    no_values = 3 + difficulty
    if difficulty <= 2:
        nums = random.sample(range(1, 10 * 10 ** difficulty), k=no_values)
    else:
        nums = random.sample(range(1, 50), k=no_values)
        nums = [round(i / 10, 1) for i in nums]
        for j in range(len(nums)):
            if nums[j] % 1 == 0:
                nums[j] = round(nums[j])
    n = random.randint(0, 1)
    if n == 0:
        nums.sort()
    else:
        nums.sort(reverse=True)
    sequence = ",\\ ".join(str(j) for j in nums)
    choices = ['Increasing', 'Decreasing']
    question = f"Are the numbers in the sequence increasing or " \
               f"decreasing in size? \n" \
               r"\begin{center} %s \end{center}" % sequence
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def st_29(difficulty):
    """Determine if the values in the graph have an increasing or
    decreasing trend. Chrys."""
    no_values = 4
    data = []
    k = random.randint(0, 1)

    if k == 0:
        upper = [10, 6, 13][difficulty - 1]
        a = [1, 2, 2][difficulty - 1]
        increments = [1, 2, 2][difficulty - 1]
    else:
        upper = [6, 8, 10][difficulty - 1]
        a = [5, 4, 2][difficulty - 1]
        increments = [5, 4, 2][difficulty - 1]

    nums = random.sample(range(1, upper), k=no_values)
    nums = [i * a for i in nums]
    n = random.randint(0, 1)
    nums.sort() if n == 0 else nums.sort(reverse=True)

    months = ["May", "June", "July", "August"]
    week_month = ['week', 'month'][k]
    for i in range(no_values):
        col_1 = [f"Week {i + 1}", months[i]][k]
        data.append([col_1, nums[i]])

    m = random.choices([0, 1], weights=(2, difficulty), k=1)[0]
    item = random.choice(["number of books read", "number of tests completed"])
    y_label = item.title()
    title = r"\textbf{%s per %s}" % (item.title(), week_month.title())
    colour = random.choice(['red', 'blue', 'green'])
    if m == 0:
        axis_scale = r'''ytick={0,%s,...,100}, ymin=0, ymajorgrids=true,
        y label style={font=\small, yshift=-12pt}, 
        y tick label style={font=\small},
        x tick label style={font=\small},
        title={%s}, title style={font=\small}''' % (increments, title)
        chart = mq.bar_chart(data, axis_adj=axis_scale, label=y_label,
                             sym_axis=True, size=(6.5, 7.5), fill=colour)
    else:
        axis_adj = r'''
        ytick={0,%s,...,100}, ymin=0, 
        x tick label style={font=\small}, 
        y tick label style={font=\small}, title style={font=\small},
        y label style={font=\small, yshift=-12pt}, height=7.5cm, width = 8.2cm,
        ''' % increments
        chart = mq.draw_line_graph(data, sym_axis=True, scale=0.85, grid=True,
                                   axis_adj=axis_adj, title=title,
                                   y_label=y_label, colour=colour)
    chart_type = ["bar chart", "line graph"][m]
    choices = ['Increasing', 'Decreasing']
    question = f"Are the values in the {chart_type} increasing or " \
               f"decreasing in size as the {week_month}s progress? \n {chart}"
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, reorder=False)


def md_29(difficulty):
    """Fill in missing number to balance multiplication and division equation.
     Chrys."""
    box = r"\makebox[2.5em]{\hrulefill}"

    n = random.choices([2, 3], weights=(3, -2 + difficulty))[0]
    if 1 < difficulty and n == 3:
        s = 's'
    else:
        s = ''
    question = f"Find the missing number{s} to balance the equation. \n" \
               "\\begin{center}"

    nums = random.sample(range(2, 12), k=2)
    nums.append(nums[0] * nums[1])
    if difficulty == 1:
        n = random.choice([1, 2])
        result = nums[n]
        nums[n] = box
        question += r"""%s $\times$ %s $=$ %s \\ %s $\div$ %s $=$ %s""" \
                    % (nums[0], nums[1], nums[2], nums[2],  nums[1], nums[0])
    else:
        a = random.randint(2, 5)
        nums.extend([nums[2] * a, a])
        result = [nums[2], ",\\ ".join([str(nums[2]), str(nums[3])])][n - 2]
        nums[2] = box
        question += r"%s $\times$ %s $=$ %s " % (nums[0], nums[1], nums[2])
        if n == 3:
            nums[3] = box
            question += r"$=$ %s $\div$ %s" % (nums[3], nums[4])
        else:
            question += r"\\ %s $=$ %s $\div$ %s" % (nums[2], nums[3], nums[4])
    question += r"\end{center}"
    answer = str(result)
    return [question, answer]


def st_30(difficulty):
    """Determine frequency by finding how many times a word appears in a text.
     Chrys."""
    base = 5
    no_values = base * difficulty
    no_colours = [2, 3, 4][difficulty - 1]

    freq = []
    while len(freq) < no_colours:
        values = random.choices(range(1, no_values), k=no_colours)
        if int(sum(values)) == no_values:
            freq = values
    colours = random.sample(["Red", "Blue", "Yellow", "Green", "Black"],
                            k=no_colours)
    list_1 = []
    for i in range(freq[0]):
        list_1.append(colours[0])
    for j in range(freq[1]):
        list_1.append(colours[1])
    if no_colours > 2:
        for m in range(freq[2]):
            list_1.append(colours[2])
    if no_colours > 3:
        for m in range(freq[3]):
            list_1.append(colours[3])
    random.shuffle(list_1)

    m = no_values // base
    list_2 = []
    for i in range(m):
        end = base * (i + 1)
        start = i * base
        my_list = list_1[start:end]
        row = " & \\ ".join(my_list)
        list_2.append(row)

    rows = r"\\ \hline ".join(list_2)
    array = r'''{\footnotesize $\begin{tabular}{|c|c|c|c|c|}
    \hline %s \\ \hline \end{tabular}$ }''' % rows
    choice = random.randint(0, len(colours) - 1)

    gender = random.choice([['male', 'he'], ['female', 'she']])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} writes down all the different colours of cars " \
               f"{gender[1]} sees passing her by. " \
               f"\n \\begin{{center}} {array} \\end{{center}} \n " \
               f"How many {colours[choice]} cars did {name} see?"
    answer = str(freq[choice])
    return [question, answer]


def st_31(difficulty):
    """Complete frequency chart using raw data. Chrys."""
    base = 4
    no_values = base * (difficulty+1)
    no_colours = [3, 3, 4][difficulty - 1]

    freq = []
    while len(freq) < no_colours:
        values = random.choices(range(1, no_values + 1), k=no_colours)
        if int(sum(values)) == no_values:
            freq = values
    colours = random.sample(["Fox", "Deer", "Squirrel", "Rabbit", "Hedgehog",
                             "Vole", "Mouse"],
                            k=no_colours)
    list_1 = []
    data = [["Animal", "Frequency"]]
    for i in range(no_colours):
        data.append([colours[i], str(freq[i])])
    for i in range(freq[0]):
        list_1.append(colours[0])
    for j in range(freq[1]):
        list_1.append(colours[1])
    if no_colours > 2:
        for m in range(freq[2]):
            list_1.append(colours[2])
    if no_colours > 3:
        for m in range(freq[3]):
            list_1.append(colours[3])
    random.shuffle(list_1)

    m = no_values // base
    list_2 = []
    for i in range(m):
        end = base * (i + 1)
        start = i * base
        my_list = list_1[start:end]
        row = " & \\ ".join(my_list)
        list_2.append(row)

    rows = r"\\ \hline ".join(list_2)
    array = r'''{\footnotesize $\begin{tabular}{|c|c|c|c|}
    \hline %s \\ \hline \end{tabular}$ }''' % rows

    answer = mq.draw_table(data)
    k = random.sample(range(1, len(data) - 1), k=[1, 2, 3][difficulty - 1])
    for j in k:
        data[j][1] = r'\phantom{10}'
    chart = mq.draw_table(data)
    gender = random.choice([['male', 'he'], ['female', 'she']])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} writes down all the different animals " \
               f"{gender[1]} sees while on a hike in the forest. " \
               f"\n \\begin{{center}} {array} \\end{{center}} \n " \
               f"Using the table above, complete the frequency chart. " \
               f"\n {chart}"
    return [question, answer]


def st_32(difficulty):
    """Find nth most/least occuring frequency from raw data. Chrys."""
    base = 4
    no_values = base * (difficulty+2)
    no_colours = [3, 4, 5][difficulty - 1]

    freq = []
    while len(freq) < no_colours:
        values = random.sample(range(1, no_values + 1), k=no_colours)
        if int(sum(values)) == no_values:
            freq = values
    colours = random.sample(["Bulldog", "Beagle", "Labrador", "Spaniel",
                             "Poodle", "Terrier", "Pug"], k=no_colours)
    list_1 = []
    data = []
    for i in range(no_colours):
        data.append([colours[i], freq[i]])
    for i in range(freq[0]):
        list_1.append(colours[0])
    for j in range(freq[1]):
        list_1.append(colours[1])
    if no_colours > 2:
        for m in range(freq[2]):
            list_1.append(colours[2])
    if no_colours > 3:
        for m in range(freq[3]):
            list_1.append(colours[3])
    if no_colours > 4:
        for m in range(freq[4]):
            list_1.append(colours[4])
    random.shuffle(list_1)

    m = no_values // base
    list_2 = []
    for i in range(m):
        end = base * (i + 1)
        start = i * base
        my_list = list_1[start:end]
        row = " & \\ ".join(my_list)
        list_2.append(row)

    rows = r"\\ \hline ".join(list_2)
    array = r'''{\footnotesize $\begin{tabular}{|c|c|c|c|}
    \hline %s \\ \hline \end{tabular}$ }''' % rows

    if difficulty == 1:
        n = random.choice([0, no_colours - 1])
    else:
        n = random.randint(0, no_colours - 1)

    if n + 1 == 1 or n + 1 == no_colours:
        ordinal = ''
    elif ceil(no_colours / 2) < n + 1 < no_colours:
        ordinal = mq.ordinal(no_colours - n)
    else:
        ordinal = mq.ordinal(n + 1)

    if n + 1 > ceil(no_colours / 2):
        order = 'least'
    else:
        order = 'most'

    data.sort(key=lambda x: x[1], reverse=True)

    gender = random.choice([['male', 'his', 'He'], ['female', 'her', 'She']])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} asks {gender[1]} friends what their favourite dog " \
               f"breeds are. {gender[2]} records their responses in a table." \
               f" What is the {ordinal} {order} occurring response? \n\n" \
               r"\begin{center} %s \end{center}" % array
    answer = data[n][0]
    return [question, answer]


def st_33(difficulty):
    """Are the values in a sequence increasing or decreasing. Chrys."""
    upper = 5 + 2 ** difficulty
    no_flowers = [3, 4, 5][difficulty - 1]
    weights = (3 - difficulty, difficulty - 1,
               difficulty, difficulty, difficulty)
    frac_base = random.choices([2, 3, 4, 5, 10], weights=weights, k=1)[0]

    flowers = ["Poppies", "Lilies", "Orchids", "Roses", "Iris", "Snapdragon",
               "Carnations", "Chrysanthemums", "Dahlias", "Tulips"]
    flowers = random.sample(flowers, k=no_flowers)

    data = [["Type", "Frequency"]]
    freq = []
    while len(freq) < no_flowers:
        values = random.choices(range(1, upper), k=no_flowers)
        if sum(values) % frac_base == 0:
            freq = values
    result = sum(freq) // frac_base

    for i in range(no_flowers):
        data.append([flowers[i], str(freq[i])])
    table = mq.draw_table(data)
    frac = mq.latex_frac(1, frac_base)

    colour = random.choice(["pink", "red", "yellow", "white", "blue"])
    name = names.get_first_name()
    question = f"{name} picks some flowers to make a bouquet. The different " \
               f"flowers used are presented in a frequency table. \n {table}" \
               f"\n If {mq.dollar(frac)} of the flowers are {colour}, how " \
               f"many {colour} flowers are there in total?"
    answer = str(result)
    return [question, answer]


def st_34(difficulty):
    """Identify trend from line graph. Multiple Choice. Chrys."""
    n = random.randint(0, 4 * difficulty)
    types = ["Stays the same", "Rises steadily", "Falls steadily",
             "Rises more and more quickly", "Falls faster and faster",
             "Stays the same then falls quickly",
             "Stays the same then rises quickly",
             "Rises then falls quickly", "Falls then rises quickly",
             "Rises steadily then stays the same then rises quickly",
             "Falls steadily then stays the same then falls quickly",
             "Falls steadily then stays the same then rises quickly",
             "Rises steadily then stays the same then falls quickly"
             ]
    function = [
        ["1"], ["x"], ["-x"], ["x^2"], ["-x^2"], ["1", "-x^2 + 2"],
        ["1", "x^2"], ["x", "2-x^2"], ["-x", "-2+x^2"], ["x", "1", "x^2 - 3"],
        ["-x", "-1", "-x^2+3"], ["-x", "-1", "x^2-5"], ["x", "1", "5-x^2"]
    ][n]

    x_max = len(function)
    add_plot = ""
    for i in range(len(function)):
        if i == 0:
            smoothness = "solid"
        else:
            smoothness = "smooth"
        add_plot += r"""
                \addplot[domain = %s:%s, samples = 5, %s, thick, black,] {%s};
        """ % (i, i + 1, smoothness, function[i])

    graph = r"""
    \begin{tikzpicture}
    \begin{axis}[xmin=0, xmax=%s+0.1, scale=0.8, axis y line*=left,
      axis x line*=bottom, xlabel={Time (t)}, ylabel={Temperature},
      xlabel style={font=\small, anchor=south west},
      ylabel style={font=\small, xshift=20, yshift=-30},
      xticklabels={}, yticklabels={}, tick style={draw=none}, 
      ]
        %s
    \end{axis}
    \end{tikzpicture}
    """ % (x_max, add_plot)

    answer = types[n]
    choices = [types[n]]
    types.remove(types[n])
    choices.extend(random.sample(types, k=3))
    types.append(answer)

    question = f"What option best describes how the temperature on the " \
               f"graph is changing over time? \n {graph} \n {answer}"
    return mq.multiple_choice(question, choices, answer, onepar=False)


def st_35(difficulty):
    """What line graph matches the trend. Multiple Choice. Chrys."""
    k = [2, 4, 4][difficulty - 1]
    upper = [7, 7, 13][difficulty - 1]

    n = random.sample(range(0, upper), k=k)
    types = ["staying the same", "rising steadily", "falling steadily",
             "rising more and more quickly", "falling faster and faster",
             "staying the same then falling quickly",
             "staying the same then rising quickly",
             "rising then falling quickly", "falling then rising quickly",
             "rising steadily then staying the same then rising quickly",
             "falling steadily then staying the same then falling quickly",
             "falling steadily then staying the same then rising quickly",
             "rising steadily then staying the same then falling quickly"
             ]
    function = [
        ["1"], ["x"], ["-x"], ["x^2"], ["-x^2"], ["1", "-x^2 + 2"],
        ["1", "x^2"], ["x", "2-x^2"], ["-x", "-2+x^2"], ["x", "1", "x^2 - 3"],
        ["-x", "-1", "-x^2+3"], ["-x", "-1", "x^2-5"], ["x", "1", "5-x^2"]
    ]
    choices = []
    for j in n:
        x_max = len(function[j])
        add_plot = ""
        for i in range(len(function[j])):
            if i == 0:
                smoothness = "solid"
            else:
                smoothness = "smooth"
            add_plot += r"""
                \addplot[domain = %s:%s, samples = 5, %s, thick, black,] {%s};
            """ % (i, i + 1, smoothness, function[j][i])
        graph = r"""
        \begin{tikzpicture}
        \begin{axis}[xmin=0, xmax=%s+0.1, scale=0.3, axis y line*=left,
          axis x line*=bottom, xlabel={Time (t)}, ylabel={Speed},
          xlabel style={font=\tiny, anchor=south west},
          ylabel style={font=\tiny, yshift=-30},
          xticklabels={}, yticklabels={}, tick style={draw=none}, 
          ]
            %s
        \end{axis}
        \end{tikzpicture}
        """ % (x_max, add_plot)
        choices.append(graph)
    answer = choices[0]
    question = f"Which of these graphs shows the speed {types[n[0]]} " \
               "over time?"
    return mq.multiple_choice(question, choices, answer)


def me_41(difficulty):
    """What is the temperature shown on the thermometer. Chrys."""
    multiplier = [10, 5, 5][difficulty - 1]
    lower = [0, 0, 1][difficulty - 1]
    upper = [10, 20, 19][difficulty - 1]
    step = [1, 1, 2][difficulty - 1]
    show_half_increments = [False, True, True][difficulty - 1]

    temp = multiplier * random.randrange(lower, upper, step)
    thermometer = mq.draw_thermometer(temp, scale=0.6, text_size="tiny",
                                      show_celsius=True, horizontal=True,
                                      half_increments=show_half_increments)
    question = f"What temperature is showing on the thermometer? \n" \
               r"\begin{center} %s \end{center}" % thermometer
    answer = f"{temp}\\textdegree C"
    return [question, answer]


def me_42(difficulty):
    """Thermometer question. Choose the thermometer that matches the
    corresponding temperature. Multiple Choice. Chrys"""
    multiplier = [10, 5, 5][difficulty - 1]
    upper = [11, 21, 21][difficulty - 1]

    k = 2 if difficulty < 3 else 3
    temps = random.sample(range(0, upper), k=k)
    temps = [multiplier * j for j in temps]

    width = [1.3, 1.3, 1][difficulty - 1]
    half_increments = [False, True, True][difficulty - 1]

    choices = []
    for i in range(len(temps)):
        thermometer = mq.draw_thermometer(temps[i], text_size="tiny",
                                          scale=0.4, length=1.7, width=width,
                                          half_increments=half_increments)
        choices.append(thermometer)

    question = "Which thermometer is showing the temperature " \
               f"{temps[0]}\\textdegree C?"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_43(difficulty):
    """Thermometer question. Choose the thermometer with the nth highest
    reading. Multiple Choice. Chrys."""
    no_values = 3
    multiplier = [10, 5, 5][difficulty - 1]

    if difficulty == 1:
        limits = [0, 11]
    else:
        lower = [5, 3][difficulty - 2]
        upper = [16, 18][difficulty - 2]
        deviation = [5, 3][difficulty - 2]
        mid = random.randint(lower, upper)
        limits = [mid - deviation, mid + deviation]

    temps = random.sample(range(limits[0], limits[1]), k=no_values)
    temps = [multiplier * j for j in temps]
    half_increments = [False, True, True][difficulty - 1]

    choices = []
    values = []
    for i in range(len(temps)):
        thermometer = mq.draw_thermometer(temps[i], text_size="tiny",
                                          scale=0.5, length=1.5, width=1,
                                          horizontal=True,
                                          half_increments=half_increments)
        choices.append(thermometer)
        values.append([temps[i], thermometer])

    values.sort(key=lambda x: x[1])

    n = random.choice([0, 2]) if difficulty == 1 else random.randint(0, 2)
    ordinal = mq.ordinal(n + 1) if n == 1 else ""
    order = "lowest" if n == 2 else "highest"

    question = f"Which thermometer is showing the {ordinal} {order} " \
               "temperature?"
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_44(difficulty):
    """Time elapsed question. Who got there first. Chrys."""
    hour_start = random.randint(6, 19)
    bounds = random.choice([[0, 30], [30, 60]])
    lower = [0, 0, bounds[0]][difficulty - 1]
    upper = [7, 59, bounds[1]][difficulty - 1]
    multiplier = [5, 1, 1][difficulty - 1]
    minute_start = random.sample(range(lower, upper), k=2)
    minute_start = [multiplier * i for i in minute_start]

    a = random.randint(30, 120)
    delta_range = [[3, 25], [a - 15, a + 16], [a - 7, a + 8]][difficulty - 1]

    while True:
        time_elapsed = random.sample(range(delta_range[0], delta_range[1]), 2)
        check = [minute_start[0] + time_elapsed[0],
                 minute_start[1] + time_elapsed[1]]
        if check[0] != check[1]:
            break

    values = []
    for i in range(2):
        t_0 = datetime(year=2021, month=6, day=20,
                       hour=hour_start, minute=minute_start[i])
        t_1 = (t_0 + timedelta(minutes=time_elapsed[i])).strftime("%H:%M")
        values.append([t_0.strftime("%H:%M"), t_1,
                       time_elapsed[i], names.get_first_name()])

    question = f"{values[0][3]} and {values[1][3]} are both travelling to a " \
               f"party. {values[0][3]} will at {values[0][0]} and travel " \
               f"for {values[0][2]} minutes to get to the party. On the " \
               f"other hand {values[1][3]} will leave at {values[1][0]} and " \
               f"travel for {values[1][2]} minutes. " \
               f"Who will arrive at the party first?"
    values.sort(key=lambda t: t[1])
    answer = values[0][3]
    return [question, answer]


def pd_2(difficulty):
    """Identify coordinate position of a shape on a grid. Chrys."""
    no_shapes = difficulty
    colour = ["black", "blue", "green", "yellow", "red"]
    random.shuffle(colour)

    circle = r'''node[circle, minimum size=1cm, scale=0.33, 
                      draw=black, fill=%s] (c) {};''' % colour[0]
    star = r'''node[star,star points=5, star point ratio=3, draw=black, 
                    fill=%s, minimum size=0.5cm, scale=0.4] (s) {}
                    ''' % colour[1]

    shapes = [[circle, "circle", colour[0]], [star, "star", colour[1]]]
    upper = 6 if difficulty == 3 else 5
    for i in range(3, upper):
        name = ["triangle", "square", "pentagon"]
        reg_poly = r'''node[regular polygon, regular polygon sides=%s, 
                            minimum size=1cm, scale=0.4, draw=black, 
                            fill=%s, rotate=0]  (S) {}''' % (i, colour[i - 1])
        shapes.append([reg_poly, name[i - 3], colour[i - 1]])
    nodes = random.sample(shapes, k=no_shapes)

    coordinates = []
    while len(coordinates) < no_shapes:
        values = []
        for i in range(no_shapes):
            coords = (random.randint(1, 9), random.randint(1, 9))
            if coords not in values:
                values.append(coords)
        if len(values) == no_shapes:
            coordinates = values

    grid = r"""
    \begin{center}
    \begin{tikzpicture}
    \begin{axis}[scale = 1,
    ytick={0,1,...,10}, ymin = 0, ymax = 10,
    xtick={0,1,...,10}, xmin = 0, xmax = 10,
    xlabel={x}, ylabel={y}, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    width = 6cm, height = 6cm,
    tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]"""
    for j in range(no_shapes):
        grid += r"\draw (axis cs:%s,%s) %s;" % (coordinates[j][0],
                                                coordinates[j][1], nodes[j][0])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    n = random.randint(0, no_shapes - 1)
    question = f"On what coordinates do we find the {nodes[n][2]} " \
               f"{nodes[n][1]}? \n {grid}"
    answer = f"{coordinates[n]}"
    return [question, answer]


def pd_3(difficulty):
    """Identify which shape is on given coordinates on a grid. Chrys."""
    no_shapes = difficulty + 1
    colour = ["black", "blue", "green", "yellow", "red"]
    random.shuffle(colour)

    circle = r'''node[circle, minimum size=1cm, scale=0.33, 
                      draw=black, fill=%s] (c) {};''' % colour[0]
    star = r'''node[star,star points=5, star point ratio=3, draw=black, 
                    fill=%s, minimum size=0.5cm, scale=0.4] (s) {}
                    ''' % colour[1]

    shapes = [[circle, "circle", colour[0]], [star, "star", colour[1]]]
    upper = 6 if difficulty == 3 else 5
    for i in range(3, upper):
        name = ["triangle", "square", "pentagon"]
        reg_poly = r'''node[regular polygon, regular polygon sides=%s, 
                            minimum size=1cm, scale=0.4, draw=black, 
                            fill=%s, rotate=0]  (S) {}''' % (i, colour[i - 1])
        shapes.append([reg_poly, name[i - 3], colour[i - 1]])
    nodes = random.sample(shapes, k=no_shapes)

    coordinates = []
    while len(coordinates) < no_shapes:
        values = []
        for i in range(no_shapes):
            coords = (random.randint(1, 9), random.randint(1, 9))
            if coords not in values:
                values.append(coords)
        if len(values) == no_shapes:
            coordinates = values

    grid = r"""
    \begin{tikzpicture}
    \begin{axis}[scale = 1,
    ytick={0,1,...,10}, ymin = 0, ymax = 10,
    xtick={0,1,...,10}, xmin = 0, xmax = 10,
    xlabel={x}, ylabel={y}, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    width = 6cm, height = 6cm,
    tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]"""
    for j in range(no_shapes):
        grid += r"\draw (axis cs:%s,%s) %s;" % (coordinates[j][0],
                                                coordinates[j][1], nodes[j][0])
    grid += r" \end{axis} \end{tikzpicture}"

    n = random.randint(0, no_shapes - 1)
    question = f"What shape do we find on the coordinates {coordinates[n]}?" \
               f"\n {grid}"
    choices = [nodes[i][1].capitalize() for i in range(no_shapes)]
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer)


def pd_4(difficulty):
    """Identify how far away. Chrys."""
    no_shapes = difficulty + 1
    colour = ["black", "blue", "green", "yellow", "red", "lightgray"]
    random.shuffle(colour)

    circle = r'''node[circle, minimum size=1cm, scale=0.33, 
                      draw=black, fill=%s] (c) {};''' % colour[0]
    star = r'''node[star,star points=5, star point ratio=3, draw=black, 
                    fill=%s, minimum size=0.5cm, scale=0.4] (s) {}
                    ''' % colour[1]

    shapes = [[circle, "circle"], [star, "star"]]
    upper = 6 if difficulty == 3 else 5
    for i in range(3, upper):
        name = ["triangle", "square", "pentagon"]
        reg_poly = r'''node[regular polygon, regular polygon sides=%s, 
                            minimum size=1cm, scale=0.4, draw=black, 
                            fill=%s, rotate=0]  (S) {}''' % (i, colour[i - 1])
        shapes.append([reg_poly, name[i - 3]])
    nodes = random.sample(shapes, k=no_shapes)

    coordinates = []
    k = random.randint(0, 1)
    a = random.sample(range(1, 9), k=no_shapes-1)
    b = random.sample(range(1, 10), k=2)
    for i in range(2):
        coordinates.append((a[0], b[i]) if k == 0 else (b[i], a[0]))
    if no_shapes > 2:
        for j in range(1, no_shapes-1):
            c = random.randint(1, 9)
            coordinates.append((a[j], c) if k == 0 else (c, a[j]))

    grid = r"""
    \begin{center}
    \begin{tikzpicture}
    \begin{axis}[scale = 1,
    ytick={0,1,...,10}, ymin = 0, ymax = 10,
    xtick={0,1,...,10}, xmin = 0, xmax = 10,
    xlabel={x}, ylabel={y}, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    width = 6cm, height = 6cm,
    tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]"""
    for j in range(no_shapes):
        grid += r"\draw (axis cs:%s,%s) %s;" % (coordinates[j][0],
                                                coordinates[j][1], nodes[j][0])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    question = f"How many units is the distance from the {nodes[0][1]} to " \
               f"the {nodes[1][1]}? \n {grid}"
    answer = str(abs(b[1] - b[0]))
    return [question, answer]


def pd_5(difficulty):
    """find how far away two places are on a grid, and use key to convert
    distance from grids to distance measurement. Chrys."""
    no_places = [2, 3, 3][difficulty - 1]
    places = mq.random_place_symbols(n=no_places)

    coordinates = []
    k = random.randint(0, 1)
    a = random.sample(range(1, 9), k=no_places-1)
    b = []
    while len(b) < 2:
        coord = random.sample(range(1, 10), k=2)
        if abs(coord[1] - coord[0]) > difficulty:
            b = coord
    for i in range(2):
        coordinates.append((a[0], b[i]) if k == 0 else (b[i], a[0]))
    if no_places > 2:
        for j in range(1, no_places-1):
            c = random.randint(1, 9)
            coordinates.append((a[j], c) if k == 0 else (c, a[j]))

    grid = r"""
    \begin{center}
    \begin{tikzpicture}
    \begin{axis}[scale=1, ytick={0,1,...,10}, xtick={0,1,...,10}, 
    ymin = 0, ymax = 10, xmin = 0, xmax = 10, width = 6cm, height = 6cm, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    xlabel={x}, ylabel={y}, tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]
    """
    for j in range(no_places):
        grid += r"""\draw (axis cs:%s,%s) 
        node[regular polygon, regular polygon sides=4, scale=0.8] (s) {%s};""" \
                % (coordinates[j][0], coordinates[j][1], places[j][1])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    key_2 = r"""{\tabcolsep=3pt \tiny$ \begin{tabular}[c!]{l|%sl} 
    \multicolumn{1}{l}{\textbf{Key:}} \\[1ex]
    """ % (r"|c||c" if difficulty > 1 else "c")
    for i in range(0, no_places):
        key_2 += r"\resizebox{1.5em}{1.1em}{%s} = %s & " \
                 % (places[i][1], places[i][0])
    key_2 += r"\end{tabular}$}"

    n = random.randint(0, 1)
    unit = random.choice([["miles", "kilometers"], ["meters", "yards"]][n])
    upper = [5 * difficulty, 3 * difficulty][n]
    multiplier = [1, [100, 50, 50][difficulty - 1]][n]
    conversion = multiplier * random.randint(difficulty, upper)
    result = abs(b[1] - b[0]) * conversion
    name = names.get_first_name()
    question = f"{name} is travelling from the {places[0][0]} to the " \
               f"{places[1][0]}. If each grid line stands for " \
               f"\\makebox{{{conversion} {unit}}}, how far did " \
               f"{name} travel? \n {grid} \n {key_2}"
    answer = f"{result} {unit}"
    return [question, answer]


def pd_6(difficulty):
    """Identify x or y coordinate of an object on a grid. Chrys."""
    no_shapes = difficulty + 1
    weights = (3 - difficulty, 4 - difficulty, difficulty, difficulty)
    increments = random.choices([1, 2, 5, 10], weights=weights, k=1)[0]
    colour = ["black", "blue", "green", "yellow", "red"]
    random.shuffle(colour)

    circle = r'''node[circle, minimum size=1cm, scale=0.33, 
                      draw=black, fill=%s] (c) {};''' % colour[0]
    star = r'''node[star,star points=5, star point ratio=3, draw=black, 
                    fill=%s, minimum size=0.5cm, scale=0.4] (s) {}
                    ''' % colour[1]

    shapes = [[circle, "circle", colour[0]], [star, "star", colour[1]]]
    upper = 6 if difficulty == 3 else 5
    for i in range(3, upper):
        name = ["triangle", "square", "pentagon"]
        reg_poly = r'''node[regular polygon, regular polygon sides=%s, 
                            minimum size=1cm, scale=0.4, draw=black, 
                            fill=%s, rotate=0]  (S) {}''' % (i, colour[i - 1])
        shapes.append([reg_poly, name[i - 3], colour[i - 1]])
    nodes = random.sample(shapes, k=no_shapes)

    coordinates = []
    while len(coordinates) < no_shapes:
        values = []
        for i in range(no_shapes):
            coords = (random.randint(1, 9), random.randint(1, 9))
            if coords not in values:
                values.append(coords)
        if len(values) == no_shapes:
            coordinates = values
    coordinates = [(increments * i[0], increments * i[1]) for i in coordinates]
    grid = r"""
    \begin{center}
    \begin{tikzpicture}
    \begin{axis}[scale = 1,
    ytick={0,%s,...,%s*10}, ymin = 0, ymax = 10*%s,
    xtick={0,%s,...,%s*10}, xmin = 0, xmax = 10*%s,
    xlabel={x}, ylabel={y}, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    width = 6cm, height = 6cm,
    tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]
    """ % (increments, increments, increments,
           increments, increments, increments)
    for j in range(no_shapes):
        grid += r"\draw (axis cs:%s,%s) %s;" % (coordinates[j][0],
                                                coordinates[j][1], nodes[j][0])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    n = random.randint(0, 1)
    k = random.randint(0, len(nodes) - 1)
    question = f"What is the {['x','y'][n]}-coordinate of the {nodes[n][2]} " \
               f"{nodes[n][1]}? \n {grid}"
    answer = f"{coordinates[k][n]}"
    return [question, answer]


def pd_7(difficulty):
    """Use compass points and conversion of distance units to find destination
    of travel on a grid. Chrys."""
    no_places = [3, 6, 6][difficulty - 1]
    places = mq.random_place_symbols(n=no_places)

    coord = []
    x = random.sample(range(1, 10), k=no_places)
    y = random.sample(range(1, 10), k=no_places)
    for i in range(no_places):
        coord.append((x[i], y[i]))

    grid = r"""
    \begin{center}
    \begin{tikzpicture}
    \begin{axis}[scale=1, ytick={0,1,...,10}, xtick={0,1,...,10}, 
    ymin = 0, ymax = 10, xmin = 0, xmax = 10, width = 6cm, height = 6cm, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    xlabel={x}, ylabel={y}, tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]
    """
    for j in range(no_places):
        grid += r"""\draw (axis cs:%s,%s) 
        node[regular polygon, regular polygon sides=4, scale=0.8] (s) {%s};"""\
                % (coord[j][0], coord[j][1], places[j][1])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    my_list = []
    rows = []
    for i in range(no_places):
        my_list.append(r"\resizebox{1.5em}{1.1em}{%s} = %s"
                       % (places[i][1], places[i][0]))
    for i in range(0, len(my_list), 3):
        rows.append(' & '.join(my_list[i:i+3]))
    rows = r' \\ '.join(rows) if len(rows) > 1 else rows[0]
    key_2 = r"""{\tabcolsep=3pt \tiny$ \begin{tabular}[c!]{l||l||l} 
    \multicolumn{1}{l}{\textbf{Key:}} \\[1ex] %s \\ \end{tabular}$}""" % rows

    k = random.sample(range(0, len(coord)), k=2)
    x_units = coord[k[1]][0] - coord[k[0]][0]
    y_units = coord[k[1]][1] - coord[k[0]][1]

    if x_units > 0:
        x_dir = "west"
    elif x_units == 0:
        x_dir = ""
    else:
        x_dir = "east"

    if y_units > 0:
        y_dir = "south"
    elif y_units == 0:
        y_dir = ""
    else:
        y_dir = "north"

    n = random.randint(0, 1)
    unit = random.choice([["miles", "kilometres"], ["metres", "yards"]][n])
    multiplier = [[1, 2, 5][difficulty - 1], [100, 50, 50][difficulty - 1]][n]

    travel = [f"{abs(multiplier * x_units)} {unit} {x_dir}",
              f"{abs(multiplier * y_units)} {unit} {y_dir}"]
    if y_dir == "":
        travel.remove(travel[1])
    if x_dir == "":
        travel.remove(travel[0])
    random.shuffle(travel)
    if len(travel) > 1:
        travel = " and ".join(str(i) for i in travel)
    else:
        travel = travel[0]
    gender = random.choice([['male', 'He'], ['female', 'She']])
    name = names.get_first_name(gender=gender[0])
    question = f"{name} is at the {places[k[1]][0]}. {gender[1]} travels " \
               f"{travel}. Where did {name} end up travelling to? \n\n " \
               f" \\makebox{{Note: 1 grid line = {multiplier} {unit}}} \n" \
               f"{grid} \n {key_2}"
    answer = f"{places[k[0]][0]}"
    return [question, answer]


def pd_8(difficulty):
    """Determine how long it would take to travel between places on a grid when
     given the time taken per grid line. Chrys."""
    no_places = [3, 6, 6][difficulty - 1]
    places = mq.random_place_symbols(n=no_places, text_size="large")

    x_0 = random.sample(range(1, 9), k=2)
    y_0 = random.sample(range(1, 9), k=2)
    coord = [(x_0[0], y_0[1]), (x_0[0], y_0[0]), (x_0[1], y_0[0])]
    while len(coord) < no_places:
        coordinates = []
        for i in range(no_places - 3):
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            if (x, y) not in coord and (x, y) not in coordinates:
                coordinates.append((x, y))
        if len(coordinates) == no_places - 3:
            coord.extend(coordinates)

    grid = r"""
    \begin{center} 
    \begin{tikzpicture}
    \begin{axis}[scale=1, ytick={0,1,...,10}, xtick={0,1,...,10}, 
    ymin = 0, ymax = 10, xmin = 0, xmax = 10, width = 6cm, height = 6cm, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    xlabel={x}, ylabel={y}, tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]
    """
    for j in range(no_places):
        grid += r"""\draw (axis cs:%s,%s) 
        node[regular polygon, regular polygon sides=4, scale=0.8] (s) {%s};"""\
                % (coord[j][0], coord[j][1], places[j][1])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    my_list = []
    rows = []
    for i in range(no_places):
        my_list.append(r"\resizebox{1.5em}{1.1em}{%s} = %s"
                       % (places[i][1], places[i][0]))
    for i in range(0, len(my_list), 3):
        rows.append(' & '.join(my_list[i:i+3]))
    rows = r' \\ '.join(rows) if len(rows) > 1 else rows[0]
    key_2 = r"""{\tabcolsep=3pt \tiny$ \begin{tabular}[c!]{l||l||l} 
    \multicolumn{1}{l}{\textbf{Key:}} \\[1ex] %s \\ \end{tabular}$}""" % rows

    t = random.randint(2 * difficulty, 5 * difficulty)
    result = t * (abs(y_0[1] - y_0[0]) + abs(x_0[1] - x_0[0]))

    n = [0, 2]
    random.shuffle(n)
    transport = random.choice(["walk", "cycle"])
    name = names.get_first_name()

    question = f"It takes {t} minutes for {name} to {transport} each block " \
               f"on the grid. How many minutes would it take {name} to " \
               f"{transport} from the {places[n[0]][0]} to the " \
               f"{places[1][0]} and then to the {places[n[1]][0]}? \n\n " \
               f"{grid} \n\n {key_2}"
    answer = f"{result} minutes"
    return [question, answer]


def pd_9(difficulty):
    """Find distance to finishing point after given compass and distance
    directions from starting points on a grid. Chrys."""
    no_places = 3 * difficulty
    places = mq.random_place_symbols(n=no_places, text_size="large")
    start = ()
    coord = []
    delta = []
    while len(coord) < 1:
        x_0 = random.randint(3, 7)
        y_0 = x_0 if difficulty == 1 else random.randint(3, 7)
        x_1, y_1 = random.randint(1, 9), random.randint(1, 9)
        d_x, d_y = (x_1 - x_0), (y_1 - y_0)
        if abs(d_x) > difficulty and abs(d_y) > difficulty and d_x != d_y:
            coord.append((x_1, y_1))
            start = (x_0, y_0)
            delta = [[d_x, "x", y_0, y_1], [d_y, "y", x_0, x_1]]

    while len(coord) < no_places:
        coordinates = []
        for i in range(no_places - 1):
            x_y = (random.randint(1, 9), random.randint(1, 9))
            if x_y != start and x_y not in coordinates and x_y not in coord:
                coordinates.append(x_y)
        if len(coordinates) == no_places - 1:
            coord.extend(coordinates)

    grid = r"""
    \begin{center} 
    \begin{tikzpicture}
    \begin{axis}[scale=1, ytick={0,1,...,10}, xtick={0,1,...,10}, 
    ymin = 0, ymax = 10, xmin = 0, xmax = 10, width = 6cm, height = 6cm, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    xlabel={x}, ylabel={y}, tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]
    """
    for j in range(no_places):
        grid += r"""\draw (axis cs:%s,%s) 
        node[regular polygon, regular polygon sides=4, scale=0.8] (s) {%s};"""\
                % (coord[j][0], coord[j][1], places[j][1])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    my_list = []
    rows = []
    for i in range(no_places):
        my_list.append(r"\resizebox{1.5em}{1.1em}{%s} = %s"
                       % (places[i][1], places[i][0]))
    for i in range(0, len(my_list), 3):
        rows.append(' & '.join(my_list[i:i+3]))
    rows = r' \\ '.join(rows) if len(rows) > 1 else rows[0]
    key = r"""{\tabcolsep=3pt \tiny$ \begin{tabular}[c!]{l||l||l} 
    \multicolumn{1}{l}{\textbf{Key:}} \\[1ex] %s \\ \end{tabular}$}""" % rows

    directions = []
    delta.sort(key=lambda x: abs(x[0]))
    if delta[0][1] == "x":
        dir_1 = "east" if delta[0][0] > 0 else "west"
    else:
        dir_1 = "north" if delta[0][0] > 0 else "south"
    directions.append([abs(delta[0][0]), dir_1])

    distance = 0
    while len(directions) < 2:
        end = random.randint(1, 9)
        if end != delta[0][2] and end != delta[0][3]:
            delta_end = end - delta[0][2]
            if delta[0][1] == "x":
                dir_2 = "north" if delta_end > 0 else "south"
            else:
                dir_2 = "east" if delta_end > 0 else "west"
            directions.append([abs(delta_end), dir_2])
            distance = abs(end - delta[0][3])

    n = random.randint(0, 1)
    unit = random.choice([["miles", "kilometres"], ["metres", "yards"]][n])
    upper = [2 * difficulty, difficulty][n]
    multiplier = [1, [100, 100, 50][difficulty - 1]][n]
    conversion = multiplier * random.randint(difficulty, upper)
    result = distance * conversion

    gender = random.choice([['male', 'he'], ['female', 'she']])
    name = names.get_first_name(gender=gender[0])
    random.shuffle(directions)
    for i in range(2):
        directions[i][0] = directions[i][0] * conversion
    question = f"{name} is travelling to the {places[0][0]}. Starting from " \
               f"{start},  {gender[1]} travels {directions[0][0]} {unit} " \
               f"{directions[0][1]} and then {directions[1][0]} {unit} " \
               f"{directions[1][1]}. If each grid line represents " \
               f"{conversion} {unit}, how far is {name} from the " \
               f"{places[0][0]}? \n\n {grid} \n\n {key}"
    answer = f"{result} {unit}"
    return [question, answer]


def pd_10(difficulty):
    """Determine direction needed to travel to get to final point after
    following compass directions on coordinate grid. Multiple Choice. Chrys."""
    no_places = 3 * difficulty
    places = mq.random_place_symbols(n=no_places, text_size="large")
    start = ()
    coord = []
    delta = []
    while len(coord) < 1:
        x_0 = random.randint(1, 9)
        y_0 = x_0 if difficulty == 1 else random.randint(1, 9)
        x_1, y_1 = random.randint(3, 7), random.randint(3, 7)
        d_x, d_y = (x_1 - x_0), (y_1 - y_0)
        if abs(d_x) > difficulty and abs(d_y) > difficulty and d_x != d_y:
            coord.append((x_1, y_1))
            start = (x_0, y_0)
            delta = [[d_x, "x", y_0, y_1], [d_y, "y", x_0, x_1]]

    while len(coord) < no_places:
        coordinates = []
        for i in range(no_places - 1):
            x_y = (random.randint(1, 9), random.randint(1, 9))
            if x_y != start and x_y not in coordinates and x_y not in coord:
                coordinates.append(x_y)
        if len(coordinates) == no_places - 1:
            coord.extend(coordinates)

    grid = r"""
    \begin{center} 
    \begin{tikzpicture}
    \begin{axis}[scale=1, ytick={0,1,...,10}, xtick={0,1,...,10}, 
    ymin = 0, ymax = 10, xmin = 0, xmax = 10, width = 6cm, height = 6cm, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    xlabel={x}, ylabel={y}, tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]
    """
    for j in range(no_places):
        grid += r"""\draw (axis cs:%s,%s) 
        node[regular polygon, regular polygon sides=4, scale=0.8] (s) {%s};"""\
                % (coord[j][0], coord[j][1], places[j][1])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    my_list = []
    rows = []
    for i in range(no_places):
        my_list.append(r"\resizebox{1.5em}{1.1em}{%s} = %s"
                       % (places[i][1], places[i][0]))
    for i in range(0, len(my_list), 3):
        rows.append(' & '.join(my_list[i:i+3]))
    rows = r' \\ '.join(rows) if len(rows) > 1 else rows[0]
    key = r"""{\tabcolsep=3pt \tiny$ \begin{tabular}[c!]{l||l||l} 
    \multicolumn{1}{l}{\textbf{Key:}} \\[1ex] %s \\ \end{tabular}$}""" % rows

    directions = []
    delta.sort(key=lambda x: abs(x[0]))
    x_end = 0
    y_end = 0
    if delta[0][1] == "x":
        dir_1 = "east" if delta[0][0] > 0 else "west"
        x_end = coord[0][0]
    else:
        dir_1 = "north" if delta[0][0] > 0 else "south"
        y_end = coord[0][1]
    directions.append([abs(delta[0][0]), dir_1])

    while len(directions) < 2:
        end = random.randint(1, 9)
        if end != delta[0][2] and end != delta[0][3]:
            delta_end = end - delta[0][2]
            if delta[0][1] == "x":
                dir_2 = "north" if delta_end > 0 else "south"
                y_end = end
            else:
                dir_2 = "east" if delta_end > 0 else "west"
                x_end = end
            directions.append([abs(delta_end), dir_2])
    values = [[coord[0][0] - x_end, "x"], [coord[0][1] - y_end, "y"]]
    values.sort(key=lambda x: abs(x[0]), reverse=True)
    if values[0][1] == "x":
        result = "East" if values[0][0] > 0 else "West"
    else:
        result = "North" if values[0][0] > 0 else "South"
    choices = ["North", "East", "South", "West"]

    gender = random.choice([['male', 'he'], ['female', 'she']])
    name = names.get_first_name(gender=gender[0])
    random.shuffle(directions)
    question = f"{name} is travelling to the {places[0][0]}. Starting from " \
               f"{start}, {gender[1]} travels {directions[0][0]} blocks " \
               f"{directions[0][1]} and then {directions[1][0]} blocks " \
               f"{directions[1][1]}. Which direction does {name} have to " \
               f"travel to get to the {places[0][0]}? \n\n {key} \n {grid}"
    answer = result
    return mq.multiple_choice(question, choices, answer, reorder=False)


def pd_11(difficulty):
    """Find final coordinates after multiple compass directions are given.
    Conversion of grid lines to distance also need to be computed. Chrys."""
    no_coords = [2, 3, 3][difficulty - 1]
    x_0 = random.randint(3, 7)
    y_0 = x_0 if difficulty == 1 else random.randint(3, 7)
    coord = [(x_0, y_0)]
    symbols = [r"{\Huge \Gentsroom}", r"{\Huge \Ladiesroom}"]
    gender = random.choice([["male", symbols[0], "He", "his"],
                            ["female", symbols[1], "She", "her"]])
    name = names.get_first_name(gender=gender[0])
    grid = r"""
    \begin{center}
    \begin{tikzpicture}
    \begin{axis}[scale=1, ytick={0,1,...,10}, xtick={0,1,...,10}, 
    ymin = 0, ymax = 10, xmin = 0, xmax = 10, width = 6cm, height = 6cm, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    xlabel={x}, ylabel={y}, tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]
    \draw (axis cs:%s,%s) 
    node[regular polygon, regular polygon sides=4, scale=0.8] (s) {%s};
    \end{axis} 
    \end{tikzpicture} 
    \end{center}
    """ % (coord[0][0], coord[0][1], gender[1])

    while len(coord) < no_coords:
        coordinates = []
        x_1 = random.randint(1, 9)
        y_1 = random.randint(1, 9)
        if x_1 != x_0 and y_1 != y_0:
            coordinates.append((x_1, y_1))
        if no_coords > 2:
            n = [random.randint(0, 1), random.randint(0, 1), 2][difficulty - 1]
            x_2 = x_1 if n == 0 else random.randint(1, 9)
            y_2 = y_1 if n == 1 else random.randint(1, 9)
            if difficulty > 2:
                if (x_2, y_2) not in coord and x_2 != x_1 and y_2 != y_1:
                    coordinates.append((x_2, y_2))
            else:
                if (x_2, y_2) not in coord and (x_2, y_2) not in coordinates:
                    coordinates.append((x_2, y_2))
        if len(coordinates) == no_coords - 1:
            coord.extend(coordinates)
    k = random.randint(0, 1)
    unit = random.choice([["miles", "kilometres"], ["metres", "yards"]][k])
    multiplier = [random.randint(2, 3 * difficulty),
                  [100, 50, 25][difficulty - 1]][k]

    deltas = []
    travel = []
    for i in range(1, len(coord)):
        delta_x = coord[i][0] - coord[i - 1][0]
        delta_y = coord[i][1] - coord[i - 1][1]
        deltas.append([delta_x, delta_y])
    for i in deltas:
        x_dir = "east" if i[0] > 0 else ("" if i[0] == 0 else "west")
        y_dir = "north" if i[1] > 0 else ("" if i[1] == 0 else "south")
        directions = [[abs(i[0]), x_dir], [abs(i[1]), y_dir]]
        for j in directions:
            if j[0] == 0:
                directions.remove(j)
        my_list = []
        for m in directions:
            my_list.append(f"{abs(m[0] * multiplier)} {unit} {m[1]}")
        random.shuffle(my_list)
        my_list = " and ".join(my_list) if len(my_list) > 1 else my_list[0]
        travel.append(my_list)

    transport = random.choice([["cycle", "drive"], ["walk", "run"]][k])
    travel = f". {gender[2]} then {transport}s a further ".join(travel) \
        if len(travel) > 1 else travel[0]

    question = f"{name} is at the coordinates {coord[0]}. {gender[2]} " \
               f"decides to {transport} {travel}. If each grid line " \
               f"represents {multiplier} {unit}, what are {name}'s final " \
               f"coordinates? \n\n {grid} \n\n " \
               r"Final Coordinates = (\makebox[1.5em]{\hrulefill}, " \
               r"\makebox[1.5em]{\hrulefill})"
    answer = f"{coord[no_coords - 1]}"
    return [question, answer]


def pd_12(difficulty):
    """Determine how many items are on the same axis line on a grid. Chrys."""
    no_places = 3 * difficulty
    no_on_same = random.randint(1, 2 * difficulty)
    places = mq.random_place_symbols(n=no_places, text_size="large")

    coords = []
    n = random.randint(0, 1)
    coord_1 = random.randint(1, 9)
    coord_2 = random.sample(range(1, 10), k=no_on_same)
    for i in range(no_on_same):
        coords.append((coord_1, coord_2[i]) if n == 0
                      else (coord_2[i], coord_1))
    axis_values = [j for j in range(1, 10)]
    axis_values.remove(coord_1)
    sample_size = no_places - no_on_same
    while len(coords) < no_places:
        coordinates = []
        x = random.choices([axis_values, range(1, 10)][n], k=sample_size)
        y = random.choices([range(1, 10), axis_values][n], k=sample_size)
        for i in range(sample_size):
            if (x[i], y[i]) not in coordinates and (x[i], y[i]) not in coords:
                coordinates.append((x[i], y[i]))
        if len(coordinates) == sample_size:
            coords.extend(coordinates)

    grid = r"""
    \begin{center} 
    \begin{tikzpicture}
    \begin{axis}[scale=1, ytick={0,1,...,10}, xtick={0,1,...,10}, 
    ymin = 0, ymax = 10, xmin = 0, xmax = 10, width = 6cm, height = 6cm, 
    x label style={font=\small, yshift=1ex}, 
    y label style={font=\small, yshift=-3ex},
    xlabel={x}, ylabel={y}, tick label style={font=\footnotesize},
    xmajorgrids=true, ymajorgrids=true]
    """
    for j in range(no_places):
        grid += r"""\draw (axis cs:%s,%s) 
        node[regular polygon, regular polygon sides=4, scale=0.8] (s) {%s};"""\
                % (coords[j][0], coords[j][1], places[j][1])
    grid += r" \end{axis} \end{tikzpicture} \end{center}"

    my_list = []
    rows = []
    for i in range(no_places):
        my_list.append(r"\resizebox{1.5em}{1.1em}{%s} = %s"
                       % (places[i][1], places[i][0]))
    for i in range(0, len(my_list), 3):
        rows.append(' & '.join(my_list[i:i+3]))
    rows = r' \\ '.join(rows) if len(rows) > 1 else rows[0]
    key_2 = r"""{\tabcolsep=3pt \tiny$ \begin{tabular}[c!]{l||l||l} 
    \multicolumn{1}{l}{\textbf{Key:}} \\[1ex] %s \\ \end{tabular}$}""" % rows

    question = r"How many buildings are on the " \
               r"\makebox{%s-coordinate %s?}" % (["x", "y"][n], coord_1) \
               + f" \n\n {grid} \n\n {key_2}"
    answer = f"{no_on_same}"
    return [question, answer]


def st_36(difficulty):
    """Identify number of shapes in a given in set or in the intersection of
    sets using a Venn diagram. Chrys."""
    colours = ["orange", "blue", "green", "yellow"]
    shapes = ["Squares", "Circles", "Triangles"]
    n = random.randint(0, len(colours) - 1)
    k = random.randint(0, len(shapes) - 1)
    label = [colours[n].capitalize(), shapes[k]]

    shape_range = [i for i in range(len(shapes))]
    shape_range.remove(k)
    colour_range = [i for i in range(len(colours))]
    colour_range.remove(n)
    set_a = []
    set_b = []
    a_n_b = []

    amount = random.choices(range(difficulty, 5 + difficulty), k=2)
    amount.append(random.randint(1, 5))
    for i in range(amount[0]):
        rotate = random.choice([0, 90, random.choice(range(300, 330)), 270])
        sh = random.choice(shape_range)
        shape_1 = [mq.draw_square(1, colours[n], colours[n], rotate),
                   mq.draw_circle(1, colours[n], colours[n]),
                   mq.draw_triangle(0.5, colours[n], colours[n], rotate)
                   ][sh]
        set_a.append(shape_1)

    for i in range(amount[1]):
        col = random.choice(colour_range)
        rotate = random.choice([90, 180,  random.choice(range(120, 150)), 270])
        shape_2 = [mq.draw_square(1, colours[col], colours[col], rotate),
                   mq.draw_circle(1, colours[col], colours[col]),
                   mq.draw_triangle(0.5, colours[col], colours[col], rotate)
                   ][k]
        set_b.append(shape_2)
    for i in range(amount[2]):
        rotate = random.choice([90, 50, 270])
        shape_3 = [mq.draw_square(1, colours[n], colours[n], rotate),
                   mq.draw_circle(1, colours[n], colours[n]),
                   mq.draw_triangle(0.5, colours[n], colours[n], rotate)
                   ][k]
        a_n_b.append(shape_3)

    graph = mq.venn_diagram(labels=label, set_a=set_a, set_b=set_b,
                            intersect=a_n_b)

    choice = random.choice([[colours[n], amount[0]],
                            [f"{colours[n]} {shapes[k]}", 0],
                            [shapes[k], amount[1]]])
    question = f"How many of the shapes are {choice[0]}? \n\n" \
               r"\begin{center} %s \end{center}" % graph
    answer = str(choice[1] + amount[2])
    return [question, answer]


def st_37(difficulty):
    """Choose where shape fits in venn diagram. Chrys."""
    colours = ["orange", "blue", "green", "yellow"]
    shapes = ["Square", "Circle", "Triangle"]
    n = random.randint(0, len(colours) - 1)
    k = random.randint(0, len(shapes) - 1)
    label = [colours[n].capitalize(), shapes[k]]

    shape_range = [i for i in range(len(shapes))]
    shape_range.remove(k)
    colour_range = [i for i in range(len(colours))]
    colour_range.remove(n)
    set_a = []
    set_b = []
    a_n_b = []

    amount = random.choices(range(4 - difficulty, 8 - difficulty), k=2)
    amount.append(random.randint(1, 5))
    for i in range(amount[0]):
        rotate = random.choice([0, 90, random.choice(range(300, 330)), 270])
        sh1 = random.choice(shape_range)
        shape_1 = [mq.draw_square(1, colours[n], colours[n], rotate),
                   mq.draw_circle(1, colours[n], colours[n]),
                   mq.draw_triangle(0.5, colours[n], colours[n], rotate)
                   ][sh1]
        set_a.append(shape_1)

    for i in range(amount[1]):
        col = random.choice(colour_range)
        rotate = random.choice([90, 180,  random.choice(range(120, 150)), 270])
        shape_2 = [mq.draw_square(1, colours[col], colours[col], rotate),
                   mq.draw_circle(1, colours[col], colours[col]),
                   mq.draw_triangle(0.5, colours[col], colours[col], rotate)
                   ][k]
        set_b.append(shape_2)
    for i in range(amount[2]):
        rotate = random.choice([90, 50, 270])
        shape_3 = [mq.draw_square(1, colours[n], colours[n], rotate),
                   mq.draw_circle(1, colours[n], colours[n]),
                   mq.draw_triangle(0.5, colours[n], colours[n], rotate)
                   ][k]
        a_n_b.append(shape_3)
    weights = [0, 0, 1][difficulty - 1]
    sets = random.choices(
        [
            [set_a, set_b, a_n_b], [None, None, None],
            [random.choice((None, set_a)),
             random.choice((None, set_b)),
             random.choice((None, a_n_b))]
        ], weights=(2, weights, difficulty - 1), k=1)[0]
    graph = mq.venn_diagram(labels=label, set_a=sets[0], set_b=sets[1],
                            intersect=sets[2])
    upper = [2, 3, 3][difficulty - 1]
    m = random.randint(0, upper)
    choices = [label[0],
               label[1],
               f"Both {label[0].lower()} and {label[1].lower()}"]
    if upper > 2:
        choices .append(f"Neither {label[0].lower()} nor {label[1].lower()}")
    sides = [3, 4, 5, 6, 7, 8]
    sides.remove(3 if k == 2 else (4 if k == 0 else 8))
    sides = random.choice(sides)
    col_choice = random.choice(colour_range)
    m_2 = 1 if k == 1 else (4 if k == 0 else 3)
    m_3 = [colours[n], colours[col_choice], colours[n], colours[col_choice]][m]

    sh__1 = mq.draw_circle(1, m_3, m_3) if m_2 == 1 \
        else mq.draw_regular_polygon(m_2, 1, m_3)
    sh__2 = mq.draw_regular_polygon(sides=sides, size=1, colour=m_3)
    shape_choice = [sh_2, sh__1, sh__1, sh__2][m]

    question = f"Where does this shape go in the venn diagram {shape_choice}?"\
               "\n\n" + r"\begin{center} %s \end{center}" % graph
    answer = choices[m]
    return mq.multiple_choice(question, choices, answer,
                              onepar=False, reorder=False)


def me_45(difficulty):
    """Find Perimeter of square/rectangle. Chrys"""
    unit = random.choice([["", ""], ["cm", "centimetres"], ["m", "metres"]])
    n = random.randint(0, 1)
    lengths = random.sample(range(2 ** difficulty, 10 * difficulty + 1), k=2)
    lengths.sort()
    height = lengths[0]
    width = height if n == 0 else lengths[1]
    square_rectangle = r"""node[rectangle, draw=black, fill=white, rotate=0,
    minimum width=%scm, minimum height=2cm]""" % [2, 4][n]
    if difficulty == 3:
        labels = ""
    else:
        labels = r"""\node[right] (n) at (S.east) {%s}; 
        \node[below] (n) at (S.south) {%s};""" % (str(height) + unit[0],
                                                  str(width) + unit[0])
    model = r"""\begin{tikzpicture}
    \draw (0,0) %s (S) {};
    \node[above] (n) at (S.north) {%s};
    \node[left] (n) at (S.west) {%s};
    %s
    \end{tikzpicture}""" % (square_rectangle, str(width) + unit[0],
                            str(height) + unit[0], labels)
    question = "What is the perimeter of the shape? "
    question += "\n" if unit[0] == "" else f"Give your answer in {unit[1]}. \n"
    question += r"\begin{center} %s \end{center}" % model
    answer = str(2 * (width + height)) + unit[0]
    return [question, answer]


def me_46(difficulty):
    """Match perimeter to shape. Multiple Choice. Chrys."""
    unit = random.choice(["", "cm", "m", " yards", " inches"])
    no_choices = 3
    n = random.choices([0, 1], k=no_choices)

    values = []
    while len(values) < no_choices:
        check = []
        for i in range(no_choices):
            k = n[i]
            lengths = random.sample(range(2 ** difficulty,
                                          10 * difficulty + 1), k=2)
            lengths.sort()
            width = lengths[0] if k == 0 else lengths[1]
            perimeter = 2 * (lengths[0] + width)
            if (lengths[0], width) not in values and perimeter not in check:
                values.append((lengths[0], width))
                check.append(perimeter)
    if difficulty == 3:
        values = [(round(i[0] * 0.1, 1), round(i[1] * 0.1, 1)) for i in values]
    choices = []
    for j in range(no_choices):
        square_rectangle = r"""node[rectangle, draw=black, fill=white, 
        rotate=0, minimum width=%scm, minimum height=1cm]""" % [1, 2][n[j]]
        if difficulty == 3:
            labels = ""
        else:
            labels = r"""\node[right, font=\small] (n) at (S.east) {%s}; 
            \node[below, font=\small] (n) at (S.south) {%s};
            """ % (str(values[j][0]) + unit, str(values[j][1]) + unit)
        model = r"""\begin{tikzpicture}
        \draw (0,0) %s (S) {};
        \node[above, font=\small] (n) at (S.north) {%s};
        \node[left, font=\small] (n) at (S.west) {%s};
        %s
        \end{tikzpicture}""" % (square_rectangle, str(values[j][1]) + unit,
                                str(values[j][0]) + unit, labels)
        choices.append(model)

    result = 2 * (values[0][0] + values[0][1])
    question = f"which of these has a perimeter of " \
               f"\\makebox{{{result}{unit}}}? "

    answer = choices[0]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_47(difficulty):
    """Worded Perimeter question. Chrys."""
    n = random.randint(0, 1)
    rectangle = ["rectangle", "rectangular", "rectangular"][difficulty - 1]
    k = random.randint(0, 2)
    units = ["centimetres", "inches", random.choice(["metres", "feet"])][k]
    lower = [10, 20, 10][k]
    upper = [100, 50, 40][k]
    lengths = random.sample(range(lower, upper), k=2)
    if difficulty == 3:
        lengths = [round(i + random.randint(1, 9) * 0.1, 1) for i in lengths]
    lengths.sort(reverse=True)
    item_1 = [
        ["photograph", "tray", "poster"],
        ["window", "whiteboard", "painting", "table", "blackboard"],
        ["playground", "garden", "sports hall", "car park"],
    ][k]
    item_2 = [
        ["photograph", "tray", "poster"],
        ["window", "television", "whiteboard", "painting", "table"],
        ["swimming pool", "playground", "garden", "football pitch",
         "volleyball court", "car park"]
    ][k]
    item = "" if difficulty == 1 else random.choice([item_1, item_2][n])

    question = [
        f"Each side of a square {item} is {lengths[0]} {units} long. ",
        f"A {rectangle} {item} is {lengths[0]} {units} long "
        f"and {lengths[1]} {units} wide. "
    ][n]
    result = [4 * lengths[0], 2 * (lengths[0] + lengths[1])][n]
    result = round(result, 1)
    result = round(result) if result % 1 == 0 else result
    question += f"What is the perimeter?"
    answer = f"{result} {units}"
    return [question, answer]


def sh_17(difficulty):
    """Guess what type of quadrilateral. Multiple Choice. Chrys"""
    size = 3
    rectangle = r"\tikz \draw (0,0) rectangle (3cm,1.5cm);"
    parallelogram = r"""\tikz \draw (0,0) -- (%f,0) -- (%f, 1) -- 
    (0.75,1) -- (0,0);""" % (size - 0.75, size)
    trapezium = r"""\tikz \node[draw, trapezium, minimum size=%scm]
    at (0,0) {};""" % round(size*0.5, 1)
    rhombus = r"""\tikz \node[diamond, draw, minimum width=3cm, 
    minimum height=1.5cm] (d) at (0,0) {};"""

    quads = {
        'rectangle': rectangle,
        'square':  mq.draw_regular_polygon(4, size-0.5),
        'parallelogram': parallelogram,
        'rhombus': rhombus,
        'trapezium': trapezium
    }

    choices = ['rectangle', 'square', 'parallelogram', 'trapezium']
    if difficulty > 1:
        choices.append('rhombus')
    weights = [(1, 1, 1, 1), (1, 1, 2, 2, 1), (.5, 0, 3, 3, 3)][difficulty - 1]
    choice = random.choices(choices, weights=weights, k=1)[0]

    question = "What type of quadrilateral is this? \n\n " \
               r"\begin{center} %s \end{center} " % quads[choice]
    choices = [i.title() for i in choices]
    answer = choice.title()
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_18(difficulty):
    """Guess what type of triangle. Multiple Choice. Chrys"""
    equilateral = mq.draw_regular_polygon(sides=3, size=4)
    isosceles = mq.draw_triangle(size=3*2.36, draw='black', fill='white')
    scalene = r"\tikz \draw (0,0) -- (5,0) -- (4,2) -- (0,0);"
    triangles = {'equilateral': equilateral,
                 'isosceles': isosceles,
                 'scalene': scalene}

    choices = ['equilateral', 'isosceles', 'scalene']
    weights = (2, difficulty, difficulty)
    choice = random.choices(choices, weights=weights, k=1)[0]

    question = "What type of triangle is this? \n\n " \
               r"\begin{center} %s \end{center} " % triangles[choice]
    choices = [i.title() for i in choices]
    answer = choice.title()
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_19(difficulty):
    """Choose which shape matches the given triangle/quadrilateral type.
    Multiple Choice. Chrys"""
    size = 2
    equilateral = mq.draw_regular_polygon(sides=3, size=4/3 * size)
    isosceles = mq.draw_triangle(size=size * 2.36, draw='black', fill='white')
    scalene = r"\tikz \draw[scale=%s] (0,0) -- (5,0) -- (1,2) -- (0,0);" \
              % (size/3)
    size = 3
    rectangle = r"\tikz \draw[scale=%s/3] (0,0) rectangle (3cm,1.5cm);" % size
    parallelogram = r"""\tikz \draw[scale=%s] (0,0) -- (%f,0) -- (%f, 1) -- 
    (0.75,1) -- (0,0);""" % (size / 3, size - 0.75, size)
    trapezium = r"""\tikz \node[draw, trapezium, minimum size=1.5cm, 
    scale=%s] at (0,0) {};""" % (size / 3 - 0.2)
    rhombus = r"""\tikz \node[diamond, draw, minimum width=3cm, 
    minimum height=1.5cm, scale=%s] (d) at (0,0) {};""" % (size / 3)
    square = mq.draw_regular_polygon(4, size-0.5)

    shapes = {
        rectangle: 'rectangle',
        square: 'square',
        parallelogram: 'parallelogram',
        rhombus: 'rhombus',
        trapezium: 'trapezium',
        equilateral: 'an Equilateral',
        isosceles: 'an Isosceles',
        scalene: 'a Scalene'
    }
    n = random.randint(0, 1)
    quad_weight = [1/difficulty, 1, difficulty, difficulty - 1, difficulty]
    quad_weight = [i/sum(quad_weight) for i in quad_weight]
    quad_choice = numpy.random.choice(
        [rectangle, square, parallelogram, rhombus, trapezium],
        size=3,
        replace=False,
        p=quad_weight
    )
    quad_choice = list(quad_choice)
    choices = [
        [equilateral, isosceles, scalene],
        quad_choice
    ][n]
    weights = [(2, difficulty, difficulty), (1, 1, 1)][n]
    choice = random.choices(choices, weights=weights, k=1)[0]

    question = f"Which of these "
    question += [f"is {shapes[choice]} Triangle? \n\n ",
                 f"equilaterals is a {shapes[choice]}? \n\n"][n]
    answer = choice
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_48(difficulty):
    """Find missing length of shape. Chrys"""
    size = 2
    isosceles = r'''
    node[isosceles triangle, minimum size=%scm, rotate=90, draw,fill=white]
    ''' % size
    trapezium = r"""node[draw, trapezium, minimum size=1.5cm, scale=%s]""" \
                % (size / 2)
    rectangle = r"""node[rectangle, draw=black, fill=white, rotate=0, 
    minimum width=%scm, minimum height=%scm]""" % (size + 1, (size + 1) * 0.5)

    n = random.randint(0, 2)
    values = random.sample(range(2 ** difficulty, 20 * difficulty), k=3)
    values.sort()
    units = random.choice(["", "cm", "m", "mm", " inches", " feet"])
    if n == 0:
        lengths = [values[0], values[1], values[1]]
        labels = [
            r"\node[below, font=\small] (n) at (S.west) {%s%s};"
            % (lengths[0], units),
            r"\node[above left, font=\small] (n) at (S.north east) {%s%s};"
            % (lengths[1], units),
            r"\node[above right, font=\small] (n) at (S.south east) {%s%s};"
            % (lengths[2], units),
        ]
    elif n == 1:
        lengths = [values[2], values[0], values[1], values[1]]
        labels = [
            r"\node[below, font=\small] (n) at (S.south) {%s%s};"
            % (lengths[0], units),
            r"\node[above, font=\small] (n) at (S.north) {%s%s};"
            % (lengths[1], units),
            r"\node[left, font=\small] (n) at (S.west) {%s%s};"
            % (lengths[2], units),
            r"\node[right, font=\small] (n) at (S.east) {%s%s};"
            % (lengths[3], units)
        ]
    else:
        lengths = [values[0], values[0], values[2], values[2]]
        labels = [
            r"\node[below, font=\small] (n) at (S.south) {%s%s};"
            % (lengths[0], units),
            r"\node[above, font=\small] (n) at (S.north) {%s%s};"
            % (lengths[1], units),
            r"\node[left, font=\small] (n) at (S.west) {%s%s};"
            % (lengths[2], units),
            r"\node[right, font=\small] (n) at (S.east) {%s%s};"
            % (lengths[3], units)
        ]
    perimeter = sum(lengths)

    if difficulty == 3:
        m = random.randint(0, 1)
        if m == 0:
            k = random.randint(0, len(labels) - 1)
            labels.remove(labels[k])
            result = lengths[k]
        else:
            k = random.randint(0, [0, 0, 1][n])
            for i in range(2):
                labels.remove(labels[len(labels) - 1]) if k == 0 \
                    else labels.remove(labels[0])
            result = [lengths[len(lengths) - 1], lengths[0]][k]

    else:
        k = random.randint(0, len(labels) - 1)
        result = lengths[k]
        labels.remove(labels[k])
        m = 0

    nodes = ' '.join(labels)
    shape = [isosceles, trapezium, rectangle][n]
    model = r"""
    \begin{center} 
    \begin{tikzpicture}
    \draw (0,0) %s (S) {};
    %s
    \end{tikzpicture}
    \end{center}
    """ % (shape, nodes)
    question = f"The perimeter of the shape is {perimeter}{units}. "
    if m == 1:
        question += "If both of the missing lengths are equal in size, "
    question += f"{['What', 'what'][m]} is the value of {['', 'one of'][m]} " \
                f"the missing length{['', 's'][m]}? \n\n {model}"
    answer = f"{result}{units}"
    return [question, answer]


def me_49(difficulty):
    """Find area of square/ rectangle when given height and width. Chrys"""
    size = 2
    n = random.randint(0, 1)
    lengths = random.sample(range(2 * difficulty, 7 + 2 * difficulty), k=2)
    lengths.sort()
    lengths[0] = lengths[1] if n == 1 else lengths[0]

    k = random.randint(0, 4)
    units = [ "cm", "m", "mm", " inches", " units"][k]
    rectangle_square = r"""node[rectangle, draw=black, fill=white, rotate=0, 
    minimum width=%scm, minimum height=%scm]
    """ % (size + 1, [(size + 1) * 0.5, size + 1][n])
    nodes = [
        r"\node[above, font=\small] (n) at (S.north) {%s%s};"
        % (lengths[1], units),
        r"\node[left, font=\small] (n) at (S.west) {%s%s};"
        % (lengths[0], units)
    ]
    if difficulty == 3 and n == 1:
        nodes.remove(nodes[0])
    model = r"""
    \begin{center} 
    \begin{tikzpicture}
    \draw (0,0) %s (S) {};
    %s
    \end{tikzpicture}
    \end{center}
    """ % (rectangle_square, ' '.join(nodes))
    question = f"Find the area of the {['rectangle', 'square'][n]}. " \
               f"\n\n {model} \n\n"
    question += "$Area=Height \\times Width$" if difficulty == 1 else ""
    area = lengths[0] * lengths[1]
    answer = f"{area}"
    answer += f" ${units}^2$" if k > 2 else f"${units}^2$"
    return [question, answer]


def me_50(difficulty):
    """Choose correct representation of area. Multiple Choice. Chrys"""
    size = 2
    n = random.randint(0, 1)
    lower, upper = 2 * difficulty, 7 + 2 * difficulty
    lengths = random.choices(range(lower, upper), k=2)
    square = mq.draw_square(size=1, draw='black', fill='white')

    rows = []
    r = 'r' * lengths[0]
    for i in range(lengths[1]):
        row = [square * lengths[0]]
        row = ' & '.join(row)
        rows.append(row)
    array = r' \\ '.join(rows)

    shape = r'''
    \begin{center}
    {\arraycolsep=0pt \def\arraystretch{0} \LARGE 
    $\begin{array}{%s} 
    %s 
    \end{array}$} 
    \end{center}
    ''' % (r, array)
    my_list = []
    no_choices = 4
    while len(my_list) < no_choices:
        add = random.sample([-1, 0, 1], k=2)
        check = [lengths, [lengths[0] + add[0], lengths[1] + add[1]]]
        for i in range(no_choices - 2):
            values = random.sample(range(lower, upper), k=2)
            if values not in check and values != [lengths[1], lengths[0]]:
                check.append([values[0], values[1]])
        if len(check) == no_choices:
            my_list = check
    choices = []
    for i in range(len(my_list)):
        txt = '$\\times$'.join([str(my_list[i][0]), str(my_list[i][1])])
        choices.append(txt)

    question = f"The shape is made of unit squares. Which of these " \
               f"multiplications represent the area of the shape? \n\n {shape}"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer)


def me_51(difficulty):
    """Find missing length using area. Chrys."""
    size = 2
    lengths = random.sample(range(2 * difficulty, 7 + 2 * difficulty), k=2)
    lengths.sort()
    area = lengths[0] * lengths[1]

    k = random.randint(0, 4)
    units = [ "cm", "m", "mm", " inches", " units"][k]
    rectangle = r"""node[rectangle, draw=black, fill=white, rotate=0, 
    minimum width=%scm, minimum height=%scm]
    """ % (size + 1, (size + 1) * 0.5)

    n = random.randint(0, 1)
    result = lengths[n]
    lengths[n] = r"\makebox[3ex]{\hrulefill}"
    model = r"""
    \begin{center} \begin{tikzpicture}
    \draw (0,0) %s (S) {};
    \node[left, font=\small] (n) at (S.west) {%s%s};
    \node[above, font=\small] (n) at (S.north) {%s%s};
    \node[font=\small] (a) at (S.center) {$Area = $ %s%s};
    \end{tikzpicture} \end{center}
    """ % (rectangle, lengths[0], units, lengths[1], units, area,
           f" ${units}^2$" if k > 2 else f"${units}^2$")

    question = f"Use the area to find the missing length of the rectangle." \
               f"\n\n {model} \n\n"
    if difficulty == 1:
        question += "Note: $Area = Height \\times Width$"
    answer = f"{result}{units}"
    return [question, answer]


def me_52(difficulty):
    """Worded Find area of square/ rectangle when given height and width.
    Chrys"""
    lengths = random.sample(range(2 * difficulty, 7 + 2 * difficulty), k=2)
    lengths.sort()
    n = random.choices([0, 1], weights=(difficulty, 3), k=1)[0]
    lengths[0] = lengths[1] if n == 1 else lengths[0]
    shape = ["rectangle", "square"][n]
    area = lengths[0] * lengths[1]

    k = random.randint(0, 4)
    units = ["centimetres", "metres", "millimetres", " inches", " units"][k]

    question = f"If the area of a {shape} is {area} square {units} and "
    question += [f"the height of the {shape} is {lengths[0]} {units}, ",
                 "all the sides have the same lengths, "
                 ][n]
    question += [f"what is the width of the {shape}?",
                 "what is the length of one of the sides?"
                 ][n]
    answer = f"{lengths[1]} {units}"
    return [question, answer]


def me_53(difficulty):
    """Find area of rectilinear shape made out of squares. Chrys."""
    colour = random.choice(['red', 'green', 'blue!60', 'teal', 'orange'])
    square = mq.draw_square(size=1, draw='black', fill=colour)

    no_rows = [random.choices([1, 2], (1, 3), k=1)[0], 4, 5][difficulty - 1]
    max_per_row = [6, 4, 4][difficulty - 1]
    lower = [2 if no_rows == 2 else 3, 1, 1][difficulty - 1]
    values = random.choices(range(lower, max_per_row + 1), k=no_rows)
    random.shuffle(values)

    l_r = random.choice(['r', 'l']) * max_per_row
    rows = []
    for i in values:
        row = [square * i]
        if len(row) < max_per_row:
            phantom = [(max_per_row - len(row)) * (r'\phantom{%s}' % square)]
            row = row + phantom
        row = ' & '.join(row)
        rows.append(row)
    array = r' \\ '.join(rows)

    shape = r'''
    \begin{center}
    {\arraycolsep=0pt \def\arraystretch{0} \LARGE 
    $\begin{array}{%s} 
    %s 
    \end{array}$} 
    \end{center}
    ''' % (l_r, array)

    unit = random.choice(["centimetre", "metre", "millimetre", "inch", "unit"])
    question = "If each square in the shape has an area of one square " \
               f"{unit}, what is the area of the shape? \n\n {shape}"
    units = unit + "es" if unit == "inch" else unit + "s"
    answer = f"{sum(values)} square {units}"
    return [question, answer]


def me_54(difficulty):
    """Choose which rectilinear shape has a given area. Chrys."""
    colour = random.sample(['red', 'green', 'blue!60', 'teal', 'orange'], k=3)
    no_rows = difficulty + 2
    max_per_row = 5
    no_shapes = 3

    choices = []
    areas = []

    while len(choices) < no_shapes:
        check_1 = []
        check_2 = []
        for k in range(no_shapes):
            square = mq.draw_square(size=1, draw='black', fill=colour[k])
            values = random.choices(range(1, max_per_row + 1), k=no_rows)
            l_r = random.choice(['r', 'l']) * max_per_row
            rows = []
            for i in values:
                row = [square * i]
                if len(row) < max_per_row:
                    phantom = [
                        (max_per_row - len(row)) * (r'\phantom{%s}' % square)
                    ]
                    row = row + phantom
                row = ' & '.join(row)
                rows.append(row)
            array = r' \\ '.join(rows)

            shape = r'''
            {\arraycolsep=0pt \def\arraystretch{0} \LARGE 
            $\begin{array}{%s} 
             %s 
            \end{array}$}
            ''' % (l_r, array)
            if sum(values) not in check_2:
                check_1.append(shape)
                check_2.append(sum(values))
        if len(check_1) == no_shapes and len(check_2) == no_shapes:
            choices = check_1
            areas = check_2

    n = random.randint(0, len(choices) - 1)
    unit = random.choice(["centimetre", "metre", "millimetre", "inch", "unit"])
    units = unit + "es" if unit == "inch" else unit + "s"
    question = f"If each square has an area of one square {unit}, which of " \
               f"these shapes has an area of {areas[n]} square {units}?"
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_55(difficulty):
    """Match rectilinear shapes that have the same area. Multiple Choice.
     Chrys."""
    colour = random.sample(['red', 'green', 'blue!60', 'teal', 'orange'], k=4)
    no_rows = difficulty + 2
    max_per_row = 5
    no_choices = 3

    choices = []
    values = []
    while len(values) < no_choices + 1:
        check_1 = []
        areas = []
        for i in range(no_choices):
            shape_values = random.choices(range(1, max_per_row + 1), k=no_rows)
            if sum(shape_values) not in areas:
                check_1.append(shape_values)
                areas.append(sum(shape_values))

        shape_1_values = random.choices(range(1, max_per_row + 1), k=no_rows)
        if sum(shape_1_values) == areas[0] and shape_1_values not in check_1:
            check_1.append(shape_1_values)
        if len(check_1) == no_choices + 1 and len(areas) == no_choices:
            values = check_1

    for k in range(len(values)):
        square = mq.draw_square(size=0.5, draw='black', fill=colour[k])
        l_r = random.choice(['r', 'l']) * max_per_row
        rows = []

        for i in values[k]:
            row = [square * i]
            if len(row) < max_per_row:
                phantom = [
                    (max_per_row - len(row)) * (r'\phantom{%s}' % square)
                ]
                row = row + phantom
            row = ' & '.join(row)
            rows.append(row)
        array = r' \\ '.join(rows)
        shape = r'''
        {\arraycolsep=0pt \def\arraystretch{0} \LARGE 
        $\begin{array}{%s} 
         %s 
        \end{array}$}
        ''' % (l_r, array)
        choices.append(shape)

    shape_1 = choices[len(choices) - 1]
    choices.remove(choices[len(choices) - 1])
    question = f"Choose the shape with the same area as the one below. \n\n " \
               r"\begin{center} %s \end{center}" % shape_1 + "\n\n\n"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_56(difficulty):
    """Find perimeter of rectilinear shape made out of squares. Chrys."""
    colour = random.choice(['red', 'green', 'blue!60', 'teal', 'orange'])
    square = mq.draw_square(size=0.5, draw='black', fill=colour)

    no_rows = random.randint(difficulty + 1, difficulty + 2)
    max_per_row = random.randint(3 + difficulty, 7)
    lower = 2 if no_rows == 2 else [3, 1, 1][difficulty - 1]
    values = random.choices(range(lower, max_per_row + 1), k=no_rows)

    random.shuffle(values)

    l_r = random.choice(['r', 'l']) * max_per_row
    rows = []
    for i in values:
        row = [square * i]
        if len(row) < max_per_row:
            phantom = [(max_per_row - len(row)) * (r'\phantom{%s}' % square)]
            row = row + phantom
        row = ' & '.join(row)
        rows.append(row)
    array = r' \\ '.join(rows)

    shape = r'''
    \begin{center}
    {\arraycolsep=0pt \def\arraystretch{0} \LARGE 
    $\begin{array}{%s} 
    %s 
    \end{array}$} 
    \end{center}
    ''' % (l_r, array)

    perimeter = no_rows * 2 + values[0] + values[len(values) - 1]
    for i in range(1, len(values)):
        perimeter = perimeter + abs(values[i] - values[i - 1])

    multiplier = random.randint(1, [1, 2, 2][difficulty - 1])
    result = perimeter * multiplier

    unit = random.choice(["centimetre", "metre", "millimetre", "inch", "unit"])
    units = unit + "es" if unit == "inch" else unit + "s"

    question = f"The shape is made up of squares. Each square is made up " \
               f"of equal sides of length {multiplier} " \
               f"{unit if multiplier == 1 else units}. What is the perimeter" \
               f" of the shape? \n\n {shape}"
    answer = f"{result} {units}"
    return [question, answer]


def me_58(difficulty):
    """Choose the rectilinear shape, made up of squares, that match a given
    perimeter. Multiple Choice. Chrys."""
    no_choices = 3
    colour = random.sample(['red', 'green', 'blue!60', 'teal', 'orange'],
                           k=no_choices)
    shape_values = []
    perimeters = []
    row_boundaries = []
    while len(shape_values) < no_choices:
        check_1 = []
        check_2 = []
        max_row_list = []
        for j in range(no_choices):
            no_rows = random.randint(difficulty, difficulty + 1)
            max_per_row = random.randint(3 + difficulty, 7)
            lower = 2 if no_rows == 2 else [3, 1, 1][difficulty - 1]

            values = random.choices(range(lower, max_per_row + 1), k=no_rows)
            shape_perim = no_rows * 2 + values[0] + values[len(values) - 1]
            for i in range(1, len(values)):
                shape_perim = shape_perim + abs(values[i] - values[i - 1])
            if values not in check_1 and shape_perim not in check_2:
                check_1.append(values)
                check_2.append(shape_perim)
                max_row_list.append(max_per_row)
        if len(check_1) == no_choices and len(check_2) == no_choices:
            shape_values = check_1
            perimeters = check_2
            row_boundaries = max_row_list

    choices = []
    for k in range(len(shape_values)):
        square = mq.draw_square(size=0.5, draw='black', fill=colour[k])
        max_per_row = row_boundaries[k]
        l_r = random.choice(['r', 'l']) * max_per_row
        rows = []
        for i in shape_values[k]:
            row = [square * i]
            if len(row) < max_per_row:
                phantom = [
                    (max_per_row - len(row)) * (r'\phantom{%s}' % square)
                ]
                row = row + phantom
            row = ' & '.join(row)
            rows.append(row)
        array = r' \\ '.join(rows)

        shape = r'''
        {\arraycolsep=0pt \def\arraystretch{0} \LARGE 
        $\begin{array}{%s} 
        %s 
        \end{array}$} 
        ''' % (l_r, array)
        choices.append(shape)

    multiplier = random.randint(1, [1, 2, 3][difficulty - 1])
    perimeters = [i * multiplier for i in perimeters]
    unit = random.choice(["centimetre", "metre", "millimetre", "inch", "unit"])
    units = unit + "es" if unit == "inch" else unit + "s"
    question = f"Each shape is made up of square with equal sides of length " \
               f"{multiplier} {unit if multiplier == 1 else units}. " \
               f"Which shape has a perimeter of {perimeters[0]} {units}."
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_59(difficulty):
    """Match two rectilinear shapes made of squares which have the same
    perimeter. Multiple Choice. Chrys"""
    """Find area of rectilinear shape made out of squares. Chrys."""
    no_choices = 3
    colour = ['red', 'green', 'blue!60', 'orange']
    random.shuffle(colour)
    shape_values = []
    while len(shape_values) < no_choices:
        check_1 = []
        check_2 = []
        max_row_list = []
        for j in range(no_choices):
            no_rows = random.randint(difficulty, difficulty + 1)
            max_per_row = random.randint(3 + difficulty, 7)
            lower = 2 if no_rows == 2 else [3, 1, 1][difficulty - 1]

            values = random.choices(range(lower, max_per_row + 1), k=no_rows)
            shape_perim = no_rows * 2 + values[0] + values[len(values) - 1]
            for i in range(1, len(values)):
                shape_perim = shape_perim + abs(values[i] - values[i - 1])
            if values not in check_1 and shape_perim not in check_2:
                check_1.append(values)
                check_2.append(shape_perim)
                max_row_list.append(max_per_row)

        no_rows = random.randint(difficulty, difficulty + 1)
        max_per_row = random.randint(3 + difficulty, 7)
        lower = 2 if no_rows == 2 else [3, 1, 1][difficulty - 1]
        shape_1_values = random.choices(range(lower, max_per_row + 1),
                                        k=no_rows)
        shape_1_perim = no_rows * 2 + shape_1_values[0] \
                        + shape_1_values[len(shape_1_values) - 1]
        for i in range(1, len(shape_1_values)):
            shape_1_perim = shape_1_perim \
                            + abs(shape_1_values[i] - shape_1_values[i - 1])
        if shape_1_perim == check_2[0] and shape_1_values not in check_1:
            check_1.append(shape_1_values)
        if len(check_1) == no_choices + 1 and len(check_2) == no_choices:
            shape_values = check_1

    choices = []
    for i in range(len(shape_values)):
        shape = mq.draw_rectilinear_shape(shape_values[i], colour[i])
        choices.append(shape)
    shape_1 = choices[len(choices) - 1]
    choices.remove(choices[len(choices) - 1])

    multiplier = [1, 1, random.randint(1, 2)][difficulty - 1]
    shape_1_colour = 'blue' if colour[no_choices] == 'blue!60' \
        else colour[no_choices]
    unit = random.choice(["centimetre", "metre", "millimetre", "inch", "unit"])
    units = unit + "es" if unit == "inch" else unit + "s"
    question = f"The shapes are made up of squares of equal sides of length " \
               f"{multiplier} {unit if multiplier == 1 else units}. " \
               f"Choose the shape with the same perimeter as the " \
               f"{shape_1_colour} shape. \n\n " \
               f"\\begin{{center}} {shape_1} \\end{{center}}"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def md_30(difficulty):
    """Use distributive property to find answer to a multiplication. Chrys."""
    a = random.randint(3, 9)
    b = random.randint(11, 10 + 3 * difficulty)
    ones_multiplier = b - 10
    box = r"\makebox[2em]{\hrulefill}"
    question = f"Using the answers of the multiplications \n\n" \
               f"\\begin{{center}}" \
               f"${a} \\times {ones_multiplier}$ \n\n" \
               f"${a} \\times 10$" \
               f"\\end{{center}}\n\n" \
               f"and use the distributive property of " \
               f"multiplication, find the answer to: \n\n" \
               f"\\begin{{center}} ${a} \\times {b} = {box}$ \\end{{center}}"
    answer = str(a * b)
    return [question, answer]


def pv_17(difficulty):
    """Choose sign that completes the roman numeral inequality. Chrys."""
    nums = random.sample(range(3, difficulty * 50), k=2)
    choices = ["$<$", "$>$"]
    result = choices[0] if nums[0] < nums[1] else choices[1]
    nums = [roman.toRoman(i) for i in nums]
    space = r'\hspace{1ex}'
    question = "Choose the sign that completes the inequality. \n\n" \
               f"\\begin{{center}} {nums[0]} {space} ? {space} {nums[1]}" \
               "\\end{center}"
    answer = result
    return mq.multiple_choice(question, choices, answer, reorder=False)


def pv_18(difficulty):
    """Choose sign that completes inequality. comparing roman numeral to
    digits. Multiple Choice. Chrys."""
    lower = 5 + 50 * (difficulty - 1)
    upper = difficulty * 50
    a = random.randint(lower, upper)
    b = random.choices([a, random.randint(lower, upper)],
                       weights=(1, 4), k=1)[0]
    nums = [a, b]
    choices = ["$<$", "$=$", "$>$"]
    result = choices[0] if nums[0] < nums[1] \
        else (choices[1] if nums[0] == nums[1] else choices[2])
    n = random.randint(0, 1)
    nums[n] = roman.toRoman(nums[n])
    space = r'\hspace{1ex}'
    question = "Choose the sign that completes the inequality. \n\n" \
               f"\\begin{{center}} {nums[0]} {space} ? {space} {nums[1]}" \
               "\\end{center}"
    answer = result
    return mq.multiple_choice(question, choices, answer, reorder=False)


def pv_19(difficulty):
    """Choose which number/roman numeral is smaller or larger or equal to
    a given one. Multiple Choice. Chrys."""
    a =  random.randint(41 + 50 * (difficulty - 1), 80 * (difficulty + 1))
    boundary = 50 - 10 * difficulty
    nums = random.sample(range(a - boundary, a + boundary), k=6)
    nums.sort()

    n = random.choices([0, 1, 2], weights=(6, 6, 1), k=1)[0]
    k = 0 if n == 2 else random.randint(0, 1)
    size = ["smaller", "larger", "the same as"][n]
    is_not = ["is", "is NOT"][k]

    if n == 2:
        a = nums[random.randint(0, len(nums) - 1)]
        result = a
    else:
        a = nums[1] if (n + k) % 2 == 0 else nums[len(nums) - 2]
        nums.remove(a)
        result = nums[0] if (n + k) % 2 == 0 else nums[len(nums) - 1]

    choices = nums
    m = random.randint(0, 1)
    if m == 0:
        choices = [roman.toRoman(i) for i in choices]
    else:
        a = roman.toRoman(a)
    numerals = ["roman numerals", "numbers"][m]
    question = f"Which of these {numerals} {is_not} {size} {a}?"
    answer = roman.toRoman(result) if m == 0 else result
    return mq.multiple_choice(question, choices, answer)


def me_60(difficulty):
    """Choose which rectilinear shape has the nth largest area.
    Multiple choice.Chrys."""
    colour = random.sample(['red', 'green', 'blue!60', 'teal', 'orange'], k=3)
    no_rows = difficulty + 2
    max_per_row = 5
    no_choices = 3

    values = []
    while len(values) < 3:
        shapes = []
        areas = []
        for i in range(no_choices):
            row_values = random.choices(range(1, max_per_row + 1), k=no_rows)
            if sum(row_values) not in areas:
                shapes.append(row_values)
                areas.append(sum(row_values))
        if len(shapes) == no_choices and len(areas) == no_choices:
            for i in range(len(areas)):
                values.append([shapes[i], areas[i]])

    values.sort(key=lambda x: x[1])
    choices = [mq.draw_rectilinear_shape(values[i][0], colour[i])
               for i in range(len(values))]
    n = random.randint(0, 2)
    order = "largest" if n == 2 else "smallest"
    ordinal = mq.ordinal(n + 1) if n == 1 else ""
    question = f"The shapes are made of unit squares. Which of these " \
               f"shapes has the {ordinal} {order} area."
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def me_61(difficulty):
    """Choose rectilinear shape with nth largest perimeter.
     Multiple Choice. Chrys."""
    colour = random.sample(['red', 'green', 'blue!60', 'teal', 'orange'], k=3)
    no_rows = difficulty + 2
    max_per_row = 5
    no_choices = 3

    values = []
    while len(values) < 3:
        shapes = []
        perimeters = []
        for i in range(no_choices):
            row_values = random.choices(range(1, max_per_row + 1), k=no_rows)
            shape_perim = no_rows * 2 \
                          + row_values[0] \
                          + row_values[len(values) - 1]
            for i in range(1, len(values)):
                shape_perim = shape_perim \
                              + abs(row_values[i] - row_values[i - 1])
            if shape_perim not in perimeters:
                shapes.append(row_values)
                perimeters.append(shape_perim)

        if len(shapes) == no_choices and len(perimeters) == no_choices:
            for i in range(len(perimeters)):
                values.append([shapes[i], perimeters[i]])

    values.sort(key=lambda x: x[1])
    choices = [mq.draw_rectilinear_shape(values[i][0], colour[i])
               for i in range(len(values))]
    n = random.randint(0, 2)
    order = "largest" if n == 2 else "smallest"
    ordinal = mq.ordinal(n + 1) if n == 1 else ""
    question = f"The shapes are made of unit squares with equal sides. " \
               f"Which of these shapes has the {ordinal} {order} perimeter."
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_20(difficulty):
    """How many lines of symmetry does the shape have. Chrys."""
    colour = random.choice(['red', 'green', 'blue!60', 'teal', 'orange'])
    values = [
        [[5,1,5,1,5], 1],
        [[4, 1, 1, 4], 1]
    ]
    reg_poly_values = [[3, 3], [4, 4], [5, 5], [6, 6]]

    shapes = [[mq.draw_triangle(4, "black", colour), 1]]
    weights = [1]
    for i in range(len(values)):
        rectilinear = mq.draw_rectilinear_shape(values[i][0], colour=colour)
        shapes.append([rectilinear, values[i][1]])
        weights.append(1)
    for i in range(difficulty + 1):
        reg_poly = r'''
        \begin{tikzpicture} 
        \node[regular polygon, regular polygon sides=%s, minimum size=%scm, 
        draw=black, fill=%s] at (0, 0) {}; 
        \end{tikzpicture}''' % (reg_poly_values[i][0], 3, colour)
        shapes.append([reg_poly, reg_poly_values[i][1]])
        weights.append(1 + 0.5 * (difficulty - 1))

    random.shuffle(shapes)
    choice = random.choices(shapes, weights=weights, k=1)[0]
    question = f"How many lines of symmetry does the shape have? \n\n" \
               f"\\begin{{center}} {choice[0]} \\end{{center}}"
    answer = str(choice[1])
    return [question, answer]


def sh_21(difficulty):
    """Choose which shape has a given number of lines of symmetry.
    Multiple Choice. Chrys."""
    colour = ['red', 'green', 'blue!60', 'teal',
              'orange', 'magenta', 'yellow!70']
    random.shuffle(colour)
    values = [
        [[5, 1, 5, 1, 5], 1],
        [[4, 1, 1, 4], 1]
    ]
    shapes = [[mq.draw_triangle(5, "black", colour[0]), 1]]
    for i in range(len(values)):
        rectilinear = mq.draw_rectilinear_shape(values[i][0],
                                                colour=colour[i + 1])
        shapes.append([rectilinear, values[i][1]])
    for i in range(3, difficulty + 4):
        reg_poly = r'''
        \begin{tikzpicture} 
        \node[regular polygon, regular polygon sides=%s, minimum size=%scm, 
        draw=black, fill=%s] at (0, 0) {}; 
        \end{tikzpicture}''' % (i, 3, colour[i])
        shapes.append([reg_poly, i])

    choices = []
    lines_of_sym = 0
    while len(choices) < 3:
        sample = random.sample(shapes, k=3)
        if sample[0][1] != sample[1][1] and sample[0][1] != sample[2][1]:
            choices = [sample[i][0] for i in range(len(sample))]
            lines_of_sym = sample[0][1]

    question = f"Which of these shapes have {lines_of_sym} lines of " \
               f"symmetry? \n\n"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_22(difficulty):
    """Which shape has the nth most/least amount of lines of symmetry.
    Multiple Choice. Chrys."""
    colour = ['red', 'green', 'blue!60', 'teal',
              'orange', 'magenta', 'yellow!70']
    random.shuffle(colour)
    values = [
        [[5, 1, 5, 1, 5], 1],
        [[4, 1, 1, 4], 1]
    ]
    shapes = [[mq.draw_triangle(5, "black", colour[0]), 1]]
    for i in range(len(values)):
        rectilinear = mq.draw_rectilinear_shape(values[i][0],
                                                colour=colour[i + 1])
        shapes.append([rectilinear, values[i][1]])
    for i in range(3, difficulty + 4):
        reg_poly = r'''
        \begin{tikzpicture} 
        \node[regular polygon, regular polygon sides=%s, minimum size=%scm, 
        draw=black, fill=%s] at (0, 0) {}; 
        \end{tikzpicture}''' % (i, 3, colour[i])
        shapes.append([reg_poly, i])

    choices = []
    while len(choices) < 3:
        sample = random.sample(shapes, k=3)
        if sample[0][1] != sample[1][1] and sample[0][1] != sample[2][1] \
                and sample[1][1] != sample[2][1]:
            choices = sample
    choices.sort(key=lambda x: x[1])
    choices = [choices[i][0] for i in range(len(choices))]

    n = random.randint(0, len(choices) - 1)
    ordinal = "" if n == 0 or n == len(choices) - 1 else mq.ordinal(n + 1)
    order = ["fewest", random.choice(["highest", "fewest"]), "highest"][n]

    question = f"Which of these shapes has the {ordinal} {order} number of" \
               f" lines of symmetry? \n\n"
    answer = choices[n]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_23(difficulty):
    """Choose which shape is symmetrical. Multiple Choice. Chrys."""
    not_symm = []
    for i in range(2):
        shape_1 = mq.draw_random_shape(polygon=False,
                                       curves=random.choice([difficulty, 1]),
                                       sides=4)
        not_symm.append(shape_1)
    colour = "white"
    values = [
        [[5, 1, 5, 1, 5], 1],
        [[4, 1, 1, 4], 1]
    ]
    symmetrical = [mq.draw_triangle(5, "black", colour)]
    for i in range(len(values)):
        rectilinear = mq.draw_rectilinear_shape(values[i][0],
                                                colour=colour)
        symmetrical.append(rectilinear)
    for i in range(3, difficulty + 4):
        reg_poly = r'''
        \begin{tikzpicture} 
        \node[regular polygon, regular polygon sides=%s, minimum size=%scm, 
        draw=black, fill=%s] at (0, 0) {}; 
        \end{tikzpicture}''' % (i, 3, colour)
        symmetrical.append(reg_poly)

    n = random.randint(0, 1)
    is_not = ["", "NOT"][n]
    choices = [random.choice([symmetrical, not_symm][n])] \
              + random.sample([not_symm, symmetrical][n], k=2)
    question = f"Which of these shapes is {is_not} symmetrical"
    answer = choices[0]
    return mq.multiple_choice(question, choices, answer, onepar=False)


def sh_24(difficulty):
    """Identify 3d shape. Multiple Choice. Chrys."""
    colour = random.choice(["blue", "red", "magenta",
                            "orange", "yellow", "green"])
    shapes = [
        ["Cube", mq.draw_cuboid(colour=colour)],
        ["Sphere", mq.draw_sphere(colour=colour, scale=1.3)],
        ["Cylinder", mq.draw_cylinder(colour)],
        ["Pyramid", mq.draw_square_based_pyramid(colour)],
    ]
    if difficulty > 1:
        cone = ["Cone", mq.draw_cone(colour)]
        shapes.append(cone)
    if difficulty > 2:
        additional_sh = [["Prism", mq.draw_prism(colour, scale=0.8)],
                         ["Cuboid", mq.draw_cuboid(colour, 0.9, 4)]]
        shapes.extend(additional_sh)

    choices = random.sample(shapes, k=2 + difficulty)
    sh_1 = choices[0][1]
    answer = choices[0][0]
    choices = [i[0] for i in choices]

    question = f"What shape is this? \n\n" \
               r"\begin{center} %s \end{center}" % sh_1
    return mq.multiple_choice(question, choices, answer)
