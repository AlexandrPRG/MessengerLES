"""
Для проверки решения, в качестве аргументов этих функций
следует использовать указаные в задачах значения. При решении задач
необходимо также избегать дублирования кода и помнить о правилах PEP 8
"""
from subprocess import Popen, PIPE
import chardet


# 1
"""
Каждое из слов «разработка», «сокет», «декоратор» представить
в строковом формате и проверить тип и содержание соответствующих
переменных. Затем с помощью онлайн-конвертера преобразовать строковые
представление в формат Unicode и также проверить тип и содержимое
переменных.
"""


def task_1(check_list: list):
    for el in check_list:
        print(type(el), el)
    print('**************')
    online_coder = [
        '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
        '\u0441\u043e\u043a\u0435\u0442',
        '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
        ]
    for ind in range(len(check_list)):
        print(type(online_coder[ind]), online_coder[ind])

# 2
"""2. Каждое из слов «class», «function», «method» записать в 
байтовом типе. Сделать это необходимо в автоматическом, а не ручном 
режиме, с помощью добавления литеры b к текстовому значению, 
(т.е. ни в коем случае не используя методы encode, decode или функцию 
bytes) и определить тип, содержимое и длину соответствующих переменных.
"""


def task_2(check_list: list):
    for el in check_list:
        el = eval('"b"+"\'"+el+"\'"')
        print(type(el), el)


# 3
"""3. Определить, какие из слов «attribute», «класс», «функция», 
«type» невозможно записать в байтовом типе. Важно: решение должно быть
универсальным, т.е. не зависеть от того, какие конкретно слова мы 
исследуем.
"""


def task_3(check_list: list):
    out_str = 'невозможно записать в байтовом типе: '
    for el in check_list:
        for symb in el:
            try:
                bytes(symb, encoding='ascii')
            except UnicodeEncodeError:
                print(out_str + el)
                break


# 4
"""4. Преобразовать слова «разработка», «администрирование», 
«protocol», «standard» из строкового представления в байтовое и 
выполнить обратное преобразование (используя методы encode и decode).
"""


def task_4(check_list: list):
    for el in check_list:
        el_encode = el.encode('utf-8')
        print(el_encode)
        print(el_encode.decode('utf-8'))


# 5
"""Написать код, который выполняет пинг веб-ресурсов yandex.ru, 
youtube.com и преобразовывает результат из байтовового типа данных в 
строковый без ошибок для любой кодировки операционной системы.
"""


def task_5():
    def ping_resurs(address: str):
        args = ['ping', address]
        pinging = Popen(args, stdout=PIPE)
        for line in pinging.stdout:
            code_page = chardet.detect(line)['encoding']
            print(address)
            print(line)
            print(code_page)
            print(line.decode(code_page))
    ping_resurs('yandex.ru')
    ping_resurs('youtube.com')


# 6
"""Создать текстовый файл test_file.txt, заполнить его тремя строками: 
«сетевое программирование», «сокет», «декоратор». 
Далее забыть о том, что мы сами только что создали этот файл и 
исходить из того, что перед нами файл в неизвестной кодировке. 
Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой 
кодировке он был создан.
"""


def task_6(line_list: list):
    with open('test_file.txt', 'w') as f:
        for el in line_list:
            f.writelines(el+'\n')
    with open('test_file.txt', 'rb') as f:
        for line in f.readlines():
            code_page = chardet.detect(line)['encoding']
            print(line)
            print(code_page)
            print(line.decode(code_page))


if __name__ == '__main__':
    task_1(['разработка', 'сокет', 'декоратор'])
    # task_2(['class', 'function', 'method'])
    # task_3(['attribute', 'класс', 'функция', 'type'])
    # task_4(['разработка', 'администрирование', 'protocol', 'standard'])
    # task_5()
    # task_6(['сетевое программирование', 'сокет', 'декоратор'])
