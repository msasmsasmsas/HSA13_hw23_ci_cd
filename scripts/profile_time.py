import matplotlib.pyplot as plt
import time
import random
import math
import cProfile
import pstats
from balanced_binary_search_tree.avl_tree import AVLTree

def search_wrapper(avl, key):
    """Обгортка для профілювання пошуку."""
    avl.search_key(key)

def profile_time():
    times = []
    n_values = [1000, 10000, 100000, 200000, 400000, 600000, 800000, 1000000]

    for n in n_values:
        avl = AVLTree()
        # Заповнення дерева
        for i in range(n):
            avl.insert_key(random.randint(0, n))

        # Профілювання часу пошуку
        profiler = cProfile.Profile()
        total_time = 0
        runs = 100  # Кількість спроб для усереднення
        for _ in range(runs):
            key = random.randint(0, n)
            profiler.enable()
            search_wrapper(avl, key)
            profiler.disable()
            # Отримуємо статистику
            stats = pstats.Stats(profiler)
            total_time += stats.total_tt  # Загальний час у секундах

        avg_time = total_time / runs
        times.append(avg_time)
        print(f"n={n}, Середній час пошуку={avg_time:.10f} сек")

    # Побудова графіку
    plt.plot(n_values, times, label='Час пошуку (сек)', marker='o')
    # Теоретична крива O(log n), нормалізована до першої точки
    plt.plot(n_values, [math.log(n) * times[0] / math.log(n_values[0]) for n in n_values],
             label='O(log n) теоретична', linestyle='--')
    plt.xscale('log')  # Логарифмічна шкала для n
    plt.xlabel('Кількість вузлів (n, логарифмічна шкала)')
    plt.ylabel('Середній час пошуку (сек)')
    plt.title('Профілювання часу пошуку в AVL-дереві')
    plt.legend()
    plt.grid(True)
    plt.savefig("profile_time.png")
    plt.show()

if __name__ == "__main__":
    profile_time()