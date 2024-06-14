import expression_generator
import generator
import mathtask as mt
import task_table
import yandexgpt


def solve_all_task():
    print('\n')
    print('---------------------------------------------------------------------------------------')
    task_list = task_table.get_tasklist_from_database()
    for math_task in task_list:
        print('\n'.join(generator.solve_task(math_task)))
        print('\n')
        print('---------------------------------------------------------------------------------------')


def main():
    choice = input('Хотите решить все задачи из базы данных? [y/n]: ')
    if choice.lower() == 'y':
        solve_all_task()
        print('\n')
        print('Tasks solved successfully!')
        print('\n')
        input('Press Enter to continue...')
        print('\n')
        main()
    if choice.lower() == 'n':
        choice = input('Хотите закинуть задачу(и) от YandexGPT  базу данных? [y/n]: ')
        if choice.lower() == 'y':
            task_table.push_task_to_db_by_yandexgpt()
            print('\n')
            input('Press Enter to continue...')
            print('\n')
            main()
        if choice.lower() == 'n':
            choice = input('Хотите закинуть задачу(и) от руки в базу данных? [y/n]: ')
            if choice.lower() == 'y':
                task_table.push_task_to_db_by_user()
                print('\n')
                input('Press Enter to continue...')
                print('\n')
                main()
            if choice.lower() == 'n':
                main()
    else:
        return


if __name__ == '__main__':
    main()