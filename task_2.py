def find_minimum(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

# Приклад використання
root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.right = Node(20)

print(find_minimum(root))  # Виведе: 2
# Найменше значення в двійковому дереві пошуку знаходиться в крайньому лівому вузлі.
# Для цього достатньо переміщатися лівими піддеревами, поки не досягнете вузла без лівого нащадка.
