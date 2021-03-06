import os
import random

import matiq as mq


# Insert your question here.
def my_question(difficulty):
    question = ""
    answer = ""
    return [question, answer]


# Do not edit the code after this line.
questions_text = ""
answers_text = ""

# Test if function runs without errors.
for _ in range(10000):
    difficulty = random.randint(1, 3)
    my_question(difficulty)

for _ in range(20):
    difficulty = random.randint(1, 3)
    sample_question = my_question(difficulty)
    questions_text += "\n\\question " + sample_question[0]
    answers_text += "\n\\question " + sample_question[1]

text = questions_text + answers_text

with open('../latex_files/validator_template.tex', 'r') as file:
    tex = file.read()
tex = tex.replace('$questions$', text)
with open('../latex_files/validator.tex', 'w') as file:
    file.write(tex)

print("Running pdflatex...")
os.system(f'pdflatex -quiet -output-directory ../output '
          f'../latex_files/validator.tex')
print("Done.")
os.startfile('..\\output\\validator.pdf')
