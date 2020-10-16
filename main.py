consp_name = input('Введите имя нового конспекта:')
file = open(consp_name+'.txt', 'w+')
defs_list = []
dates_list = []


def save(defs, dates):
    final = ""
    for d in dates:
        final += f"{d['date']} - {d['event']}\n"
    if defs:
        final += "Определения: \n"
        for d in defs:
            final += f"{d['termin']} - {d['definition']}\n"
    return final


while True:
    new_line_act = int(input('Добавить дату (1) или определение? (2) '))
    if new_line_act == 1:
        dates_list.append({"date": input('Введите дату: '), "event": input('Введите событие: ')})
    elif new_line_act == 2:
        defs_list.append({"termin": input('Введите термин: '), "definition": input('Введите определение: ')})
    elif not new_line_act:
        file.write(save(defs_list, dates_list))
        file.close()
        print(f"Конспект завершён и сохранён в файл {consp_name}.txt!")
        if input('Показать конспект (y/n): ') == 'y':
            print('===========================')
            print(save(defs_list, dates_list))
        exit()
