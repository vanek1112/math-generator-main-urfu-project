import sqlite3
import mathtask as mt
import yandexgpt
from config import database_name


def get_tasklist_from_database() -> list:
    result = []
    try:
        # Установим соединение с базой данных.
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TasksDataForGenerator')
        rows = cursor.fetchall()
        for row in rows:
            result.append(mt.MathTask(*row))
    except sqlite3.Error as error:
        print("Ошибка при работе с базой данных:", error)
    finally:
        if conn:
            conn.close()
    return result


def insert_data_to_database(task_description, variables_dict, solution_formula, answer_format):
    try:
        # Установим соединение с базой данных.
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS TasksDataForGenerator (TaskCondition TEXT,VariablesDict TEXT,AnswerFormula TEXT,AnswerFormat TEXT);")
        sql_query = "INSERT INTO TasksDataForGenerator (TaskCondition, VariablesDict, AnswerFormula, AnswerFormat) VALUES (?, ?, ?, ?)"

        # Добавляем данные в базу.
        cursor.execute(sql_query, (task_description, variables_dict, solution_formula, answer_format))
        conn.commit()

        print("[>] Данные успешно добавлены в таблицу TaskAnswers.")

    except sqlite3.Error as error:
        print("[!] Ошибка при работе с базой данных:", error)

    finally:
        if conn:
            conn.close()


def push_task_to_db_by_user():
    n = int(input("Кол-во задач, которое пойдет в таблицу: "))
    for i in range(n):
        task_condition = input("Условие задачи: ")
        variables_dict = input("Словарь переменных: ")
        answer_formula = input("Формула ответа: ")
        answer_format = input("Формат ответа: ")
        insert_data_to_database(task_condition, variables_dict, answer_formula, answer_format)
        print('\n')


def push_task_to_db_by_yandexgpt():
    n = int(input("Кол-во задач, которое пойдет в таблицу: "))
    for i in range(n):
        task = yandexgpt.get_random_mathtask()
        insert_data_to_database(**task)
    print('Успешно. Проверьте базу данных.')