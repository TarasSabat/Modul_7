''' № 1
Для ініціалізації свого проекту створіть допоміжну функцію do_setup(args_dict), яка буде викликати функцію setup з параметрами зі словника args_dict.
Структура словника для параметра args_dicts має бути наступною
{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
'''
# from setuptools import setup


# def do_setup(args_dict):
#     setup(
#         name=args_dict['name'],
#         version=args_dict['version'],
#         description=args_dict['description'],
#         url=args_dict['url'],
#         author=args_dict['author'],
#         author_email=args_dict['author_email'],
#         license=args_dict['license'],
#         packages=args_dict['packages'],
#     )
   
# print(do_setup({
#     "name": "useful",
#     "version": "1",
#     "description": "Very useful code",
#     "url": "http://github.com/dummy_user/useful",
#     "author": "Flying Circus",
#     "author_email": "flyingcircus@example.com",
#     "license": "MIT",
#     "packages": ["useful"],
# }))

''' № 2
Функція do_setup(args_dict, requires) повинна викликати функцію setup з параметрами зі словника args_dict та параметром install_requires, який набуває значення requires.
Структура словника для параметра args_dicts має бути наступною
{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
'''
# from setuptools import setup


# def do_setup(args_dict, requires):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires = requires)
    
''' № 3
Продовжуємо модифікувати приклад. Для функції do_setup необхідно передбачити третій параметр, який буде словником, де ми можемо вказати список "точок входу" для ключа console_scripts.
Функція do_setup(args_dict, requires, entry_points) повинна викликати функцію setup з параметрами словника args_dict та параметром install_requires, який набуває значення requires. Третій параметр entry_points приймає словник, де ми можемо вказати список "точок входу" для ключа console_scripts.
Структура словника для параметра args_dicts має бути наступною
{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
'''
# from setuptools import setup


# def do_setup(args_dict, requires, entry_points):
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=requires,
#           entry_points={'console_scripts':entry_points['console_scripts']}
#           )
''' № 4
Далі підуть завдання на повторення та закріплення матеріалу. Можна використовувати будь-які техніки, з якими ви зіткнулися у процесі навчання. І почнемо ми з функцій.
У Python існує рядкова функція isdigit(). Ця функція повертає True, якщо всі символи в рядку є цифрами, і є принаймні один символ, інакше — False. Напишіть функцію з ім'ям is_integer, яка розширюватиме функціональність isdigit(). При перевірці рядка необхідно ігнорувати початкові та кінцеві прогалини в рядку. Після виключення зайвих прогалин рядок вважається таким, що представляє ціле число, якщо:
її довжина більша або дорівнює одному символу
вона повністю складається з цифр
передбачити виняток, що, можливо, є початковий знак "+" або "-", після якого мають йти цифри
'''
# import re

# def is_integer(s):
#     s = s.strip().removeprefix('-').removeprefix('+')
#     r = re.search('\D+', s) is None     
#     if len(s) <= 0:
#         return False
#     else:
#         return r

    
# print(is_integer('      '))

''' № 5 
Дуже часто люди у своїх повідомленнях не ставлять великі літери, особливо це стало масовим явищем в еру мобільних. пристроїв. Розробіть функцію capital_text, яка прийматиме на вхід рядок з текстом і повертатиме рядок з відновленими великими літерами.
Функція повинна:
зробити великою першу літеру в рядку, попри прогалини
зробити великою першу літеру після точки, попри прогалини
зробити великою першу літеру після знака оклику, попри прогалини
зробити великою першу літеру після знака питання, попри прогалини
'''
# def capital_text(s):  
#     result = ""
#     capitalize_next = True
#     for char in s:
#         if capitalize_next and char.isalpha():
#             result += char.upper()
#             capitalize_next = False
#         else:
#             result += char
#         if char in [".", "!", "?"]:
#             capitalize_next = True
#     return result
    

# print(capital_text('  зробити великою. першу літеру! в рядку? попри прогалини  '))

''' № 6 
Параметри функції:
riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.
'''
# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     if reverse:
#         riddle = riddle[::-1]
#         word_start = riddle.find(start_letter)
#         word = riddle[word_start: word_start+word_length] 
        
#     else:        
#         word_start = riddle.find(start_letter)
#         word = riddle[word_start: word_start+word_length] 
        
#     return word

# print(solve_riddle('terpower1im', 5, 'p', reverse=False))

''' № 7
У четвертому модулі розв'язували завдання нормалізації даних. Розширимо її.
При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати працювати з даними далі. Напишіть функцію data_preparation, яка приймає набір даних, список списків (Приклад: [[1,2,3],[3,4], [5,6]]).
Функція повинна видаляти з переданих списків найбільше і найменше значення, але якщо розмір списку понад два елементи. Після видалення даних з кожного списку необхідно злити їх разом в один список, відсортувати його за зменшенням та повернути отриманий список як результат (Для прикладу вище результат буде наступним: [6, 5, 4, 3, 2]).
'''
# Варіант 1
# def data_preparation(list_data):
#     list_end = []
#     for el in list_data:
#         if len(el) > 2:
#             el.sort()
#             el.pop(0)
#             if len(el) > 2:
#                 el.pop(-1)
#                 list_end.extend(el)
#                 continue
#             list_end.extend(el)
#             continue
#         else:
#             list_end.extend(el)
#             continue
#     list_end.sort()
#     list_end.reverse()
#     return list_end

# print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))

## Варіант 2
# def data_preparation(list_data):
#     list_end = []
#     for el in list_data:
#         if len(el) > 2:
#             el.remove(min(el))
#             if len(el) > 2:
#                 el.remove(max(el))
#                 list_end.extend(el)
#                 continue
#             list_end.extend(el)
#             continue
#         else:
#             list_end.extend(el)
#             continue
#     list_end.sort()
#     list_end.reverse()
#     return list_end

# print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))
