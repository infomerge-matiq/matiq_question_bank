from functions import *


def addition(year, difficulty):
    lower = 10 ** (year + difficulty - 2)
    upper = 10 ** (year + difficulty - 1) - 1
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    n = random.randint(0, 2)
    x = [a, b, a + b]
    answer = x[n]
    x[n] = "\\square"
    return [str(x[0]) + " + " + str(x[1]) + " = " + str(x[2]), str(answer)]


def subtraction(year, difficulty):
    lower = 10 ** (year + difficulty - 2)
    upper = 10 ** (year + difficulty - 1) - 1
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    n = random.randint(0, 2)
    x = [a + b, a, b]
    answer = x[n]
    x[n] = "\\square"
    return [str(x[0]) + " - " + str(x[1]) + " = " + str(x[2]), str(answer)]


def multiplication(year, difficulty):
    n = random.randint(0, 2)
    lower = 2 ** (year + difficulty - 2 + n)
    upper = 2 ** (year + difficulty - 1 + n) - 1
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    x = [a, b, a * b]
    answer = x[n]
    x[n] = "\\square"
    return [str(x[0]) + " \\times " + str(x[1]) + " = " + str(x[2]),
            str(answer)]


def division(year, difficulty):
    n = random.randint(0, 2)
    lower = 2 ** (year + difficulty - 1 - n)
    upper = 2 ** (year + difficulty - n) - 1
    a = random.randint(lower, upper)
    b = random.randint(lower, upper)
    x = [a * b, a, b]
    answer = x[n]
    x[n] = "\\square"
    return [str(x[0]) + " \\div " + str(x[1]) + " = " + str(x[2]), str(answer)]


def factorisation(year, difficulty):
    lower = 2 ** (year + difficulty - 1)
    upper = 2 ** (year + difficulty + 1)
    num = random.randint(lower, upper)
    return ["$Find the prime factors of $" + str(num) + ".",
            str(prime_factors(num))]