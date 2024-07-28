class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def find_maximum(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.value

# Приклад використання
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.right = Node(30)

print(find_maximum(root))  # Виведе: 30
# Найбільше значення в двійковому дереві пошуку знаходиться в крайньому правому вузлі.
#Для цього достатньо переміщатися правими піддеревами, поки не досягнете вузла без правого нащадка.
