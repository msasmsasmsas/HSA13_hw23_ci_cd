import matplotlib.pyplot as plt
import time
import random
import math
from balanced_binary_search_tree.avl_tree import AVLTree


def profile_time():
    times = []
    n_values = [1000, 10000, 100000, 1000000]  # Різні розміри дерева

    for n in n_values:
        avl = AVLTree()
        for i in range(n):
            avl.insert_key(random.randint(0, n))

        # Вимірювання часу пошуку (усереднене за 100 спроб)
        total_time = 0
        for _ in range(100):
            key = random.randint(0, n)
            start = time.time()
            avl.search_key(key)
            total_time += time.time() - start
        avg_time = total_time / 100
        times.append(avg_time)
        print(f"n={n}, Середній час пошуку={avg_time} сек")

    # Побудова графіку
    plt.plot(n_values, times, label='Час пошуку (сек)', marker='o')
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