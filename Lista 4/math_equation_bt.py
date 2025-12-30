class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print_tree(node.right, level + 1, " -->")

        indent = "    " * level
        print(f"{indent}{prefix}{node.value}")

        print_tree(node.left, level + 1, " -->")

#(((5 + 2) * (2 − 1))/((2 + 9) + ((7 − 2) − 1)) * 8)

n5 = Node(5)
n2_a = Node(2)
n2_b = Node(2)
n1_a = Node(1)

plus_a = Node("+", left=n5, right=n2_a)
minus_a = Node("-", left=n2_b, right=n1_a)
mult_a = Node("*", left=plus_a, right=minus_a)

n2_c = Node(2)
n9 = Node(9)
n7 = Node(7)
n2_d = Node(2)
n1_b = Node(1)

plus_b = Node("+", left=n2_c, right=n9)
minus_b = Node("-", left=n7, right=n2_d)
minus_c = Node("-", left=minus_b, right=n1_b)
plus_c = Node("+", left=plus_b, right=minus_c)

div = Node("/", left=mult_a, right=plus_c)
n8 = Node(8)

root = Node("*", left=div, right=n8)

print_tree(root)
