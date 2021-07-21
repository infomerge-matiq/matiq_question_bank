import random


def multiple_choice(question: str, choices: list[str], onepar=False):
    layout = ""
    if onepar:
        layout = "onepar"
    choices_list = []
    random.shuffle(choices)
    for choice in choices:
        choices_list.append(f"\\choice {choice}\n")
    full_question = "".join([question, f"\n\n\\begin{{{layout}choices}}\n"] +
                            choices_list + [f"\\end{{{layout}choices}}"])
    return full_question


def dollar(x):
    return "$" + str(x) + "$"


def ordinal(n):
    return "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1)
                                   * (n % 10 < 4) * n % 10::4])


def is_prime(n):
    if isinstance(n, int) and n > 0:
        if n == 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    else:
        raise ValueError


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


def gcd(m, n, *args):
    for arg in (m, n) + args:
        if not isinstance(arg, int):
            return ValueError
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


def fraction_simplify(a, b):
    return a // gcd(a, b), b // gcd(a, b)


def fraction_addition(a, b, c, d):
    numerator = a * d + b * c
    denominator = b * d
    return fraction_simplify(numerator, denominator)


def fraction_subtraction(a, b, c, d):
    numerator = a * d - b * c
    denominator = b * d
    return fraction_simplify(numerator, denominator)


def convert_measurement(number, unit_in, unit_out):
    prefixes = {"m": 0.001, "c": 0.01, "d": 0.1, "": 1, "da": 10,
                "h": 100, "k": 1000}
    base_units = ["m", "g", "l"]
    for unit in [unit_in, unit_out]:
        if not unit[-1] in base_units or not unit[0:-1] in prefixes:
            raise NameError(f"{unit} is not a valid unit.")
    if unit_in[-1] != unit_out[-1]:
        raise TypeError("Units are not of the same type.")
    else:
        return number * prefixes[unit_in[0:-1]] / prefixes[unit_out[0:-1]]
