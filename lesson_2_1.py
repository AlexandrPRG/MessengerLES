"""
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv()
"""
import csv
import re


def get_data():
    def check_index(temp_list: list, id:int):
        try:
            out = temp_list[id]
        except IndexError:
            out = ''
        return out

    list_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    main_data  = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы',
    ]
    list_main = [[] for _ in range(len(main_data))]
    pattern = re.compile('\s{2}[\S ]*$')
    for file in list_files:
        with open(file) as f:
            f_reader = csv.reader(f)
            for _ in f:
                list_csv = next(f_reader)
                for ind, data in enumerate(main_data):
                    main_in_csv = re.search(data, list_csv[0])
                    if main_in_csv:
                        data_append = re.findall(pattern, list_csv[0])
                        if data_append:
                            list_main[ind].append(data_append[0].strip())
    vendor_sys_list, name_sys_list, code_sys_list, type_sys_list = list_main
    # print(vendor_sys_list, name_sys_list, code_sys_list, type_sys_list)
    list_main = []
    lists_len = [len(vendor_sys_list),
                 len(name_sys_list),
                 len(code_sys_list),
                 len(type_sys_list),]
    for ind in range(max(lists_len)):
        for _ in range(max(lists_len)):
            lst = []
            lst.append(check_index(vendor_sys_list, ind))
            lst.append(check_index(name_sys_list, ind))
            lst.append(check_index(code_sys_list, ind))
            lst.append(check_index(type_sys_list, ind))
        list_main.append(lst)


    # print(*list_main)
    with open('main_data.csv', 'w', encoding='utf-8') as m:
        WRITER = csv.writer(m)
        WRITER.writerow(main_data)
    return list_main


def write_to_csv(file_name: str):
    data_prepare = get_data()
    with open(file_name, 'a', encoding='utf-8', newline='') as m:
        WRITER = csv.writer(m)
        WRITER.writerows(data_prepare)


if __name__ == '__main__':
    write_to_csv('main_data.csv')
