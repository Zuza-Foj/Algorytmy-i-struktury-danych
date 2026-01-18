import graphviz

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_rec(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_rec(node.right, key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_rec(self.root, key)

    def search_rec(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self.search_rec(node.left, key)
        return self.search_rec(node.right, key)

    def search(self, key):
        return self.search_rec(self.root, key)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_rec(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete_rec(node.left, key)
        elif key > node.key:
            node.right = self.delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self.min_value_node(node.right)
            node.key = successor.key
            node.right = self.delete_rec(node.right, successor.key)

        return node

    def delete(self, key):
        self.root = self.delete_rec(self.root, key)

    def display(self):
        if self.root is None:
            print("Drzewo jest puste.")
            return

        dot = graphviz.Digraph(comment='BinarySearchTree')
        queue = [self.root]
        dot.node(str(id(self.root)), label=str(self.root.key)) # tworzę nowy węzeł adres + tekst na obrazku węzła

        while queue:
            current = queue.pop(0)

            if current.left:
                dot.node(str(id(current.left)), label=str(current.left.key)) # kółko
                dot.edge(str(id(current)), str(id(current.left)), label="L") # krawędź
                queue.append(current.left) # nowy root (żeby sprawdzić czy ma dzieci)

            if current.right:
                dot.node(str(id(current.right)), label=str(current.right.key))
                dot.edge(str(id(current)), str(id(current.right)), label="P")
                queue.append(current.right)

        dot.render('bst_output', view=True, format='png')
        return dot

if __name__ == "__main__":
    bst_1 = BinarySearchTree()
    for val in [30, 40, 24, 58, 48, 26, 11, 13]:
        bst_1.insert(val)

    bst_1.display()

    print(f"Czy 40 istnieje? {bst_1.search(40)}") # True
    print(f"Czy 100 istnieje? {bst_1.search(100)}") # False
