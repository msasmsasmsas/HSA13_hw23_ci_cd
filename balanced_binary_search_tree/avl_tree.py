class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, key):
        # Звичайна вставка BST
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Дублікати не вставляються

        # Оновлення висоти
        self.update_height(root)

        # Перевірка балансу
        balance = self.balance_factor(root)

        # Left-Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right-Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def search_key(self, key):
        return self.search(self.root, key)

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Вузол знайдено
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            # Вузол з двома дітьми
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        # Оновлення висоти
        self.update_height(root)

        # Перевірка балансу
        balance = self.balance_factor(root)

        # Left-Left Case
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        # Left-Right Case
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Right Case
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        # Right-Left Case
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete_key(self, key):
        self.root = self.delete(self.root, key)


# Приклад використання
avl = AVLTree()
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    avl.insert_key(key)
print(avl.search_key(30))  # <AVLNode object>
avl.delete_key(30)
print(avl.search_key(30))  # None