import re
import unittest

"""
В системе авторизации есть ограничение: логин должен начинаться с латинской буквы,
состоять из латинских букв, цифр, точки и минуса,
но заканчиваться только латинской буквой или цифрой;
минимальная длина логина — один символ, максимальная — 20.
Напишите код, проверяющий соответствие входной строки этому правилу.
Придумайте несколько способов решения задачи и сравните их.
Подробнее: http://company.yandex.ru/job/vacancies/dev_python_mysql.xml
"""

def check_login(login):
    z = re.match('^([a-zA-Z0-9])$', login)
    z1 = re.match('^([a-zA-Z])([a-zA-Z0-9.-]){0,18}([a-zA-Z0-9])$', login)
    if z or z1:
        print(z)
        print(z1)
        return True
    return False

class TestLogin(unittest.TestCase):

    def test_one_symbol_login(self):
        self.assertEqual(check_login("q"), True)

    def test_ordinary_login(self):
        self.assertEqual(check_login("laosdfa8"), True)

    def test_login_with_allow_symbols(self):
        self.assertEqual(check_login("lSGs-d7.8"), True)

    def test_too_long_login(self):
        self.assertEqual(check_login("toolongloginheretoolongloginhere"), False)



if __name__ == "__main__":
    unittest.main()