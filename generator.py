import sqlite3
import mathtask as mt
import sympy as sp
import numpy as np


#Генератор математических задач.
def solve_task(task: mt.MathTask) -> tuple:
    while True:
        try:
            # Формулируем задачу подставляя переменные.
            randomized_variables_dict = task.randomize_variables()
            formatted_description = task.task_description.format(**task.randomized_description)

            # Вычисляем ответ, используя eval и библиотеки numpy,sympy.
            answer = eval(task.solution_formula.format(**randomized_variables_dict))
            break
        except (np.linalg.LinAlgError):
            continue
    # Форматируем ответ.
    formatted_answer = 'Ответ: {result}.'.format(result=eval(task.answer_format))
    return formatted_description, formatted_answer


