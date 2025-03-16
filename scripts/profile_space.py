import matplotlib.pyplot as plt
from pympler import asizeof
from balanced_binary_search_tree.avl_tree import AVLTree

def profile_space():
    sizes = []
    n_values = range(0, 10000, 1000)  # Тестуємо для різної кількості вузлів

    for n in n_values:
        avl = AVLTree()
        for i in range(n):
            avl.insert_key(i)
        size = asizeof.asizeof(avl)
        sizes.append(size)
        print(f"n={n}, Розмір={size} байт")

    # Побудова графіку
    plt.plot(n_values, sizes, label='Розмір пам’яті (байти)', marker='o')
    plt.plot(n_values, [n * sizes[1] / 1000 for n in n_values], label='O(n) теоретична', linestyle='--')
    plt.xlabel('Кількість вузлів (n)')
    plt.ylabel('Розмір (байти)')
    plt.title('Профілювання використання простору AVL-дерева')
    plt.legend()
    plt.grid(True)
    plt.savefig("profile_space.png")
    plt.show()

if __name__ == "__main__":
    profile_space()