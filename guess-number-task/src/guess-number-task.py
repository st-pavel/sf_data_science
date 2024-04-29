import numpy as np
import game_v2
import game_v3

'''
Основной модуль проекта
'''

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(10001)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    #score_game(random_predict)

    # Оценка рабооты алгоритмов
    # Run benchmarking to score effectiveness of all algorithms
    print('Run benchmarking for random_predict: ', end='')
    score_game(game_v2.random_predict)

    print('Run benchmarking for game_core_v2: ', end='')
    score_game(game_v2.game_core_v2)

    print('Run benchmarking for game_core_v3: ', end='')
    score_game(game_v3.game_core_v3)

    print('Run benchmarking for game_core_v4: ', end='')
    score_game(game_v3.game_core_v4)
    
    
    