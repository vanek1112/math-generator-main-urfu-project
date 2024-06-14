import random
import numpy as np
import sympy as sp
from expression_generator import generate_random_expression


class MathTask():
    def __init__(self, task_description: str, variables_dict: str, solution_formula: str, answer_format: str):
        self.task_description = task_description  #Условие задачи.
        self.variables_dict = variables_dict  #Словарь переменных, значение которых нужно зарандомить.
        self.solution_formula = solution_formula  #Выражение для получения ответа на задачу.
        self.answer_format = answer_format  #Формат вывода ответа.
        self.randomized_description = dict()

    def randomize_value(x):
        if isinstance(x, int):
            x += random.randint(-10, 10)
            return repr(x)
        if isinstance(x, float):
            x += random.randint(-10, 10)
        if isinstance(x, np.ndarray):
            for i in range(x.shape[0]):
                for j in range(x.shape[1]):
                    x[i, j] += random.randint(-10, 10)
            return 'np.' + repr(x).replace('\n      ', '')
        if isinstance(x, sp.Expr):
            x = str(generate_random_expression())
            return f'sp.sympify(\'{x}\')'
        if isinstance(x, sp.Point2D):
            x = f'sp.Point({random.randint(-10, 10)}, {random.randint(-10, 10)})'
        return x

    def randomize_variables(self) -> dict:
        variables_values = list(eval(self.variables_dict).values())
        randomized_variables = [MathTask.randomize_value(eval(x)) for x in variables_values]
        self.randomized_description = dict()
        result = dict()
        for key, value in zip(eval(self.variables_dict).keys(), randomized_variables):
            result[key] = value
            self.randomized_description[key] = eval(self.format_value_for_description(value))
        return result

    @staticmethod
    def format_value_for_description(x: str) -> str:
        if 'np.array' in x:
            return x.replace('np.array', 'sp.Matrix')
        return x
