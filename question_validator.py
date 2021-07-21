import os
import random
import re

from num2words import num2words
import roman

from functions import *


# Insert your question here.
def my_question(year, difficulty):
    units = random.choice([["m", "km"], ["cm", "m"], ["cm", "mm"],
                           ["g", "kg"], ["ml", "l"]])
    unit1, unit2 = random.sample(units, 2)
    number = random.randint(1, 1000) / 10
    question = f"What is ${number:g}\\,${unit1} in {unit2}?"
    result = convert_measurement(number, unit1, unit2)
    rounded = float(f"{result:f}")
    if rounded.is_integer():
        answer = dollar(f"{int(rounded)}\\,") + unit2
    else:
        answer = f'${float(f"{rounded:g}")}\\,$' + unit2
    return [question, answer]


year = 5  # Edit as needed
difficulty = 2  # Edit as needed


# Do not edit the code after this line.
questions_text = ""
answers_text = ""
my_dir = os.path.join(os.getcwd(), "question_validator.tex")

for _ in range(20):
    sample_question = my_question(year, difficulty)
    questions_text += "\n\\question " + sample_question[0]
    answers_text += "\n\\question " + sample_question[1]

text = questions_text + answers_text

with open(my_dir, "r") as file:
    tex = file.read()
replace_text = "%%%" + text + "\n%%%"
tex = re.sub(r"%%%(.*)%%%", replace_text.replace("\\", "\\\\"), tex,
             flags = re.DOTALL)
with open(my_dir, "w") as file:
    file.write(tex)
os.system("pdflatex " + my_dir)
os.startfile("question_validator.pdf")
