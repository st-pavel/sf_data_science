import numpy as np

def game_core_v3(number: int = 1) -> int:
    """ Используем алгоритм бинарного поиска для приближения к загаданному числу
        Binary search algorithm 
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток для получения загаданного числа
    """
    # Ваш код начинается здесь

    count = 0
    predict = np.random.randint(1, 101)
    
    # начальные границы бинарного поиска
    min_predict = 0
    max_predict = 101

    while number != predict:
        count += 1
        if number > predict:
            min_predict = predict
        elif number < predict:
            max_predict = predict
        predict = (max_predict+min_predict)//2

    # Ваш код заканчивается здесь

    return count

def game_core_v4(number: int = 1) -> int:
    """ Используем модифицированные алгоритм бинарного поиска для приближения к загаданному числу,
        в каждой итерации новое угадываемой значение выбирается случайным образом в рамках 
        минимальной и максимальной границ 
        Binary search algorithm with set random predict within min and max limits 
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток для получения загаданного числа
    """
    # Ваш код начинается здесь

    count = 0
    predict = np.random.randint(1, 101)
    
    # начальные границы бинарного поиска
    min_predict = 0
    max_predict = 101

    while number != predict:
        count += 1
        if number > predict:
            min_predict = predict
        elif number < predict:
            max_predict = predict
        predict = np.random.randint(min_predict, max_predict)

    # Ваш код заканчивается здесь

    return count