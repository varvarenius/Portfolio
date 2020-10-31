import numpy as np

def game_core_v2(number):
    # Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       # Функция принимает загаданное число и возвращает число попыток
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if predict > number:
            predict = ((predict - number) // 2) + number # используем бинарное деление для поиска
        else:
            predict = ((number - predict) //2) + number # увеличиваем число predict, чтобы использовать бинарное деление
        
       
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2)