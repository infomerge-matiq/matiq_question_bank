import os
from inspect import getmembers, isfunction

import sample_problems    # replace this with your own file

module = sample_problems


def display_problems(difficulty):
    all_questions = [fn for fn in getmembers(module, isfunction) if
                     fn[1].__module__ == module.__name__]
    q_list = []
    a_list = []
    for question in all_questions:
        q_text, a_text = question[1](difficulty)
        q_list.append(f'\\question {q_text}\n\\vspace{{\\fill}}')
        a_list.append(f'\\question {a_text}')
    questions = f'\n'.join(q_list)
    answers = f'\n'.join(a_list)
    with open('../latex_files/validator_template.tex', 'r') as file:
        tex = file.read()
    questions_tex = tex.replace('$questions$', questions)
    answers_tex = tex.replace('$questions$', answers)
    with open('../latex_files/all_test.tex', 'w') as output:
        output.write(questions_tex)
    with open('../latex_files/all_answers.tex', 'w') as output:
        output.write(answers_tex)
    print("Running pdflatex...")
    os.system('pdflatex  -quiet -output-directory ../output '
              '../latex_files/all_test.tex')
    os.system('pdflatex  -quiet -output-directory ../output '
              '../latex_files/all_answers.tex')
    print("Done.")
    os.startfile('..\\output\\all_test.pdf')
    os.startfile('..\\output\\all_answers.pdf')


if __name__ == '__main__':
    display_problems(difficulty=2)
