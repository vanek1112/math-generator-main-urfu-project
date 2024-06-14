import random
import sympy as sp


transformations = (sp.parsing.sympy_parser.standard_transformations +
                       (sp.parsing.sympy_parser.implicit_multiplication,
                        sp.parsing.sympy_parser.implicit_application,
                        sp.parsing.sympy_parser.function_exponentiation,
                        ))


def generate_term(n: int) -> str:
    coef = random.randint(-25, 25)
    while coef == 0:
        coef = random.randint(-25, 25)
    power = random.randint(0, n)
    if power == 0:
        return f"{coef}"
    if power == 1:
        return f"{coef}x"
    return f"{str(coef)*bool(not(int(coef)))}x**{power}"

#Метод, генерирующий математическое выражение.
def generate_random_expression() -> str:
    n = random.randint(2, 5)
    num_terms = random.randint(1, 5)

    expression = f"f="
    while True:
        for i in range(num_terms):

            term = generate_term(n)
            expression += '+' if expression[-1] != '=' else ''

            if random.random() > 0.45:
                function = random.choice(['sin', 'cos', 'sqrt', 'tan', 'cot'])
                rd = random.random()
                if 'x' in term or '**' in term:
                    if rd > 0.90:
                        expression += term
                        expression = f"{function}({expression})"
                        continue
                    elif rd > 0.5:
                        if random.random() > 0.5:
                            term += f"+{generate_term(random.randint(0, 1))}"
                        expression += f"{function}({term})"
                        continue

                if random.random() > 0.75:
                    expression += f"+{random.choice([-1,1])}exp(x)"
            expression += term
        expression = expression.replace('f=', '')
        if 'x' in str(sp.parse_expr(expression, transformations=transformations)):
            break
    expression = expression.replace('+-', '-').replace('( -', '(-').replace(' ) ', '(').replace('(+', '(').replace('( +','')

    expression = sp.parse_expr(expression, transformations=transformations)
    return expression