#  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
#  величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести
#  фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников
with open('../example5/text_3.txt', 'r', encoding='utf-8') as f:
    surnames = []
    all_salary = 0
    people = 0
    for line in f:
        people += 1
        surname, salary = (i for i in line.split())
        salary = float(salary)
        if salary < 20000:
            surnames.append(surname)
        all_salary += salary
    all_salary /= people
print(*surnames)
print(all_salary)
