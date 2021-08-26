import os
import random
import re

from num2words import num2words
import roman

from functions import *


# Insert your question here.
def my_question(difficulty):
    num_type = random.choice(["decimal", "fraction"])
    b = 10 ** random.randint(difficulty, difficulty + 1)
    a = random.choice([x for x in range(1, b) if gcd(x, 10) == 1])
    fraction = dollar(latex_frac(a, b))
    decimal = a / b
    if num_type == "decimal":
        num = fraction
        answer = dollar(decimal)
    else:
        num = dollar(decimal)
        answer = fraction
    question = f"What is {num} as a {num_type}?"
    return [question, answer]


# Do not edit the code after this line.
questions_text = ""
answers_text = ""
my_dir = os.path.join(os.getcwd(), "question_validator.tex")

for _ in range(20):
    difficulty = random.randint(1, 3)
    sample_question = my_question(difficulty)
    questions_text += "\n\\question " + sample_question[0]
    answers_text += "\n\\question " + sample_question[1]

text = questions_text + answers_text

with open(my_dir, "r") as file:
    tex = file.read()
replace_text = "%%%" + text + "\n%%%"
tex = re.sub(r"%%%(.*)%%%", replace_text.replace("\\", "\\\\"), tex,
             flags=re.DOTALL)
with open(my_dir, "w") as file:
    file.write(tex)
print("Running pdflatex...")
os.system(f"pdflatex -quiet {my_dir}")
os.startfile("question_validator.pdf")
