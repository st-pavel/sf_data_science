import numpy as np

def game_core_v3(number: int = 1) -> int:
    """ Используем алгоритм бинарного поиска для приближения к загаданному числу
        Binary search algorithm 
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0
    predict = np.random.randint(1, 101)

    min = 0
    max = 100

    while number != predict:
        count += 1
        if number > predict:
            min = predict
            #predict = np.random.randint(min, max)
            predict = (max+min)//2
        elif number < predict:
            max = predict
            #predict = np.random.randint(min, max)
            predict = (max+min)//2


    # Ваш код заканчивается здесь

    return count