from multiprocessing import Pool

def f(x):
    return x * x


with Pool(processes=4) as pool:  # запуск 4 worker процесса

    # вычисление "f(10)" асинхронно в одномпроцессе
    result = pool.apply_async(f, (10,))
    print(result.get(timeout=1))
    # печатает "100"

    print(pool.map(f, range(10)))
    # печатает "[0, 1, 4,..., 81]"