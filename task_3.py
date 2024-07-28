def sum_of_values(node):
    if node is None:
        return 0
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)

# Приклад використання
root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.right = Node(20)

print(sum_of_values(root))  # Виведе: 37
# Щоб знайти суму всіх значень у дереві, можна використовувати рекурсивний обхід
# (наприклад, in-order traversal) і накопичувати суму всіх значень вузлів.
