import csv
import re


def get_data():
    list_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    main_data  = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы',
    ]
    list_names = [
        'vendor_sys_list',
        'name_sys_list',
        'code_sys_list',
        'type_sys_list',
    ]
    pattern = re.compile('\S+$')
    for file in list_files:
        with open(file) as f:
            f_reader = csv.reader(f)
            for _ in f:
                list_csv = next(f_reader)
                print(list_csv)
                # print(re.findall(pattern, list_csv[0]))
    return main_data

def get_list(main_data):
    return [[] for ind in range(len(main_data))]

if __name__ == '__main__':
    get_data()
    # print(get_list(get_data()))