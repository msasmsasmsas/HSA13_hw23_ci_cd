import matplotlib.pyplot as plt
from pympler import asizeof
from balanced_binary_search_tree.avl_tree import AVLTree

def profile_space():
    sizes = []
    n_values = range(0, 10000, 1000)

    for n in n_values:
        avl = AVLTree()
        for i in range(n):
            avl.insert_key(i)
        size = asizeof.asizeof(avl)
        sizes.append(size)
        print(f"n={n}, Розмір={size} байт")

    # Теоретична O(n) крива, нормалізована до розміру одного вузла
    size_per_node = (sizes[1] - sizes[0]) / 1000  # Розмір на вузол (184 байт)
    theoretical = [sizes[0] + n * size_per_node for n in n_values]

    # Побудова графіку
    plt.plot(n_values, sizes, label='Розмір пам’яті (байти)', marker='o')
    plt.plot(n_values, theoretical, label='O(n) теоретична', linestyle='--')
    plt.xlabel('Кількість вузлів (n)')
    plt.ylabel('Розмір (байти)')
    plt.title('Профілювання використання простору AVL-дерева')
    plt.legend()
    plt.grid(True)
    plt.savefig("profile_space.png")
    plt.show()

if __name__ == "__main__":
    profile_space()