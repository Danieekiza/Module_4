def drive(first, second):
    """
    Функция drive() модуля fake_math принимает на вход два числа first,
    second и возвращает результат деления, где first - делимое, second - делитель.
    В случае, если делитель = 0, то функция возвращает значение 'Ошибка'.
    В случае если делимое и делить = 0, то функция возвращает: "нельзя 0 делить на 0 !!!"

    :param first: делимое
    :param second: делитель
    :return: результат деления
    """
    title = '\nОтвет модуля fake_math: '
    while second != 0:
        result = first / second
        return title, result
    else:
        if first != 0:
            return title, 'Ошибка'
        else:
            return title, 'нельзя 0 делить на 0 !!!'

