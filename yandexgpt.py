import requests
from config import *


prompt = {
    "modelUri": f"gpt://{id}/yandexgpt/latest",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxtokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты генератор условий математических задач для вариативного тестирования предназначенного для студентов 1 курса университета (шаблонов для метода-рандомайзера написанного на Python). Тебя просят сгенерировать задачу, в ответ ты отправляешь ТОЛЬКО словарь типа str: str из элементов кода питона. Только словарь. Ни слова больше."
        },
        {
            "role": "user",
            "text": '''Сгенерируй питоновский словарь, состоящий из task_description (Условие задачи), variables_dict (словарь переменных NumPy и SymPy, которые будут потом рандомиться), solution_formula (формула для получения ответа, представленной в виде питон-кода с использованием библеотек SymPY(sp), NumPy(np)), answer_format (формат ответа. Всегда в виде функции SymPy),для последующей его передачи в метод-генератор. Например, {'task_description': 'Произведение матриц {A}*{B} равно: ...', 'variables_dict': """{'A': np.array([[1, 2], [3, 4]]), 'B': np.array([[5, 6], [7, 8]])}""", 'solution_formula': 'np.dot(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))', 'answer_format': 'sp.Matrix(answer).applyfunc(sp.Rational)'} или {'task_description': 'Решить матричное уравнение [[1, 2], [3, 4]]*X = [[5, 6], [7, 8]]. Чему равен X?','variablesdict': """{'A': np.array([[1, 2], [3, 4]]), 'B': np.array([[5, 6], [7, 8]])}""",'solutionformula': 'np.linalg.solve(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))','answer_format': 'sp.Matrix(answer).applyfunc(lambda x: sp.nsimplify(str(x), rational=True))'}, или {'task_description': 'Вычислить интеграл: {A}.', 'variables_dict': """{'A': 'sp.sympify("2*x**2")'}""", 'solution_formula': 'sp.integrate({A}, sp.Symbol("x"))', 'answer_format': 'answer'}, или 

{'task_description': 'Найти расстояние от точки {A} до отрезка, образованного точками {B} и {C}.', 'variables_dict': """{'A': 'sp.Point(1,1)', 'B': 'sp.Point(2,1)', 'C': 'sp.Point(1,2)'}""", 'solution_formula': '{A}.distance(sp.Line({B},{C}))', 'answer_format': 'answer'}, или {'task_description': 'Найти корни квадратного трёхчлена: {A}x^2 + {B}x + {C}.', 'variables_dict': """{'A': '1', 'B': '2', 'C': '1'}""", 'solution_formula': 'sp.solve(sp.sympify("{A}*x**2+{B}*x+{C}"),sp.Symbol("x"))', 'answer_format': 'answer'}. Нужен только словарь, без лишних слов. Без воды. Только словарь.'''
        }
    ]
}

url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Api-Key {api_key}'
}


def get_random_mathtask() -> dict:
    #Отправка запроса YandexGPT.
    response = requests.post(url, headers=headers, json=prompt)
    st = str(response.text)
    #Достаем из ответа словарь.
    st = st.replace("""```""",'Ь', 1).replace("""```""",'Ъ', 1).replace('python','')
    result = st[st.find("Ь")+1:st.find("Ъ")].replace('\\n', '').replace('\\','')
    return eval(result)