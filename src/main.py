"""Прогноз выполнения учебного проекта за пять дней.
Выполнил: Тасмагамбетова Дильназ. Вариант 15.
"""

project_size = 20
all_days = 5

def task(minimal, maximum):
    """Запрашивает число пунктов в заданном диапазоне.
    Принимает нижнюю и верхнюю границы диапазона.
    Возвращает целое количество пунктов за день.
    """
    tasks_count = int(input("Количество пунктов задания за день: "))

    while tasks_count < minimal or tasks_count > maximum:
        print(f"Введите число в диапазоне от {minimal} до {maximum}")
        tasks_count = int(input("Количество пунктов задания за день: "))
    return tasks_count

def status(tasks_comp):
    """Определяет статус проекта по числу выполненных пунктов.
    Принимает выполненный объем и возвращает строку статуса.
    """
    if tasks_comp < project_size / 2:
        return "Начальный этап"
    elif tasks_comp < project_size:
        return "В работе"
    else:
        return "Завершен"

def table(project_name, tasks_count):
    """Выводит пятидневный прогноз и спрашивает о новом расчете.
    Принимает название проекта и число пунктов за день.
    Возвращает True при ответе «да», иначе False.
    """
    tasks_comp = 0

    print()
    print(f"{'Отчет':^60}")
    print("-" * 60)
    print(f"Название проекта: {project_name}")
    print(f"{'Объем проекта, пунктов:':<40}{project_size:>20}")
    print(f"{'Количество дней:':<40}{all_days:>20}")
    print("-" * 60)
    print(f"{'День':<6}{'Выполнено':>9}{'Осталось':>10}{'Готовность':>12}  {'Статус':<21}")
    print("-" * 60)

    for day in range(1, all_days + 1):
        tasks_comp = tasks_comp + tasks_count
        if tasks_comp > project_size:
            tasks_comp = project_size
        tasks_left = project_size - tasks_comp
        progress = tasks_comp / project_size
        project_status = status(tasks_comp)
        print(f"{day:02d}    {tasks_comp:>9}{tasks_left:>10}{progress:>12.1%}  {project_status:<21}")

    tasks_left = project_size - tasks_comp
    project_status = status(tasks_comp)

    print("-" * 60)
    print(f"{'Итог после пяти дней':^60}")
    print(f"{'Выполнено, пунктов:':<40}{tasks_comp:>20}")
    print(f"{'Осталось, пунктов:':<40}{tasks_left:>20}")
    print(f"{'Окончательный статус:':<30}{project_status:>30}")
    print("-" * 60)

    answer = input("Рассчитать другой проект? (да/нет) ").strip().lower()

    while answer != "да" and answer != "нет":
        print("Введите «да» или «нет».")
        answer = input("Рассчитать другой проект? (да/нет) ").strip().lower()
    return answer == "да"

repeat = True

while repeat:
    project_name = input("Название проекта: ")
    tasks_count = task(1, 10)
    repeat = table(project_name, tasks_count)

print("Работа программы завершена")
