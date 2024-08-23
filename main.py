def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()
# inner_function()
# File "/Users/dmitry/PycharmProjects/module_4_2.py/main.py", line 8, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# попытка вызова функции inner_function приводит к ошибке выше, так как функция не существует в глобальном
# пространстве имен.