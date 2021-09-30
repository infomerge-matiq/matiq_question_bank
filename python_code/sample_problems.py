import random

import functions as mq


def addition(difficulty):
    lower = 10 ** (difficulty + 3)
    upper = 10 ** (difficulty + 4) - 1
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    n = random.randint(0, 2)
    x = [a, b, a + b]
    answer = x[n]
    x[n] = "\\square"
    return [f"${x[0]} + {x[1]} = {x[2]}$", str(answer)]


def subtraction(difficulty):
    lower = 10 ** (difficulty + 3)
    upper = 10 ** (difficulty + 4) - 1
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    n = random.randint(0, 2)
    x = [a + b, a, b]
    answer = x[n]
    x[n] = "\\square"
    return [f"${x[0]} - {x[1]} = {x[2]}$", str(answer)]


def multiplication(difficulty):
    n = random.randint(0, 2)
    lower = 2 ** (difficulty + 3 + n)
    upper = 2 ** (difficulty + 4 + n) - 1
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    x = [a, b, a * b]
    answer = x[n]
    x[n] = "\\square"
    return [f"${x[0]} \\times {x[1]} = {x[2]}$", str(answer)]


def division(difficulty):
    n = random.randint(0, 2)
    lower = 2 ** (difficulty + 4 - n)
    upper = 2 ** (difficulty + 5 - n) - 1
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    x = [a * b, a, b]
    answer = x[n]
    x[n] = "\\square"
    return [f"${x[0]} \\div {x[1]} = {x[2]}$", str(answer)]


def factorisation(difficulty):
    lower = 2 ** (difficulty + 4)
    upper = 2 ** (difficulty + 6)
    num = random.randint(lower, upper)
    return ["Find the prime factors of " + str(num) + ".",
            ', '.join([str(a) for a in mq.prime_factors(num)])]
