# зададим исх. списки строк
first = 'Мама мыла раму'
second = 'Рамена мало было'

# создаем lambda-функцию
# ф-я map для применения lambda-функции к каждой паре символов из списков
result = list(map(lambda x, y: x == y, first, second))

# вывод рез-та
print(result)

# ф-я get_advanced_writer, которая принимает название файла для записи
def get_advanced_writer(file_name):
    # внутри get_advanced_writer определяем write_everything
    def write_everything(*data_set):
        # откр. файл в режиме добавления
        with open(file_name, 'a', encoding='utf-8') as file:
            # запис. все данные из data_set в файл
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

# пример get_advanced_writer
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# импорт choice из модуля random для случ. выбора
from random import choice

# зададим класс MysticBall
class MysticBall:
    def __init__(self, *words):
        # атрибут words хранящий коллекцию строк
        self.words = words

    def __call__(self):
        # метод __call__, который случайным образом выбирает слово из words
        return choice(self.words)

# пример:
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())