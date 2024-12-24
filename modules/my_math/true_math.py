from math import inf, nan

def drive(first, second):
    """
    Функция drive() модуля true_math принимает на вход два числа first,
    second и возвращает результат деления, где first - делимое, second - делитель.
    В случае, если делитель = 0, то функция возвращает значение math.inf.
    В случае если делимое и делить = 0, то функция возвращает значение math.nan (not a number)

    :param first: делимое
    :param second: делитель
    :return: результат деления
    """
    title = '\nОтвет модуля true_math: '
    while second != 0:
        result = first / second
        return title, result
    else:
        if first != 0:
            return title, inf
        else:
            return  title, nan

