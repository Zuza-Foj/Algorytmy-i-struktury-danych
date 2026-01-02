import graphviz

class BinaryTree:
    def __init__(self):
        self.tree = []

    def resize(self, index):
        if index >= len(self.tree):
            self.tree.extend([None] * (index - len(self.tree) + 1))

    def set_root(self, value):
        self.resize(0)
        self.tree[0] = value

    def set_left(self, parent_index, value):
        left_index = 2 * parent_index + 1
        self.resize(left_index)
        self.tree[left_index] = value

    def set_right(self, parent_index, value):
        right_index = 2 * parent_index + 2
        self.resize(right_index)
        self.tree[right_index] = value

    def get_root(self):
        return self.tree[0] if self.tree else None

    def get_left(self, parent_index):
        left_index = 2 * parent_index + 1
        return self.tree[left_index] if left_index < len(self.tree) else None

    def get_right(self, parent_index):
        right_index = 2 * parent_index + 2
        return self.tree[right_index] if right_index < len(self.tree) else None

    def get_parent(self, child_index):
        if child_index == 0: return None
        parent_index = (child_index - 1) // 2
        return self.tree[parent_index] if parent_index < len(self.tree) else None

    def get_sibling(self, index):
        if index == 0: return None
        parent_index = (index - 1) // 2
        left_child = 2 * parent_index + 1
        right_child = 2 * parent_index + 2

        if index == left_child:
            sibling_index = right_child
        else:
            sibling_index = left_child

        return self.tree[sibling_index] if sibling_index < len(self.tree) else None

    def get_children(self, parent_index):
        return [self.get_left(parent_index), self.get_right(parent_index)]

    def draw(self):
        if not self.tree or self.tree[0] is None:
            print("Drzewo jest puste.")
            return

        dot = graphviz.Digraph(comment='Binary Tree')
        for i in range(len(self.tree)):
            if self.tree[i] is not None:
                dot.node(str(i), label=str(self.tree[i]))

                left_index = 2 * i + 1
                if left_index < len(self.tree) and self.tree[left_index] is not None:
                    dot.edge(str(i), str(left_index))

                right_index = 2 * i + 2
                if right_index < len(self.tree) and self.tree[right_index] is not None:
                    dot.edge(str(i), str(right_index))

        dot.render('tree_output', view=True, format='png')
        return dot

if __name__ == "__main__":
    tree = BinaryTree()
    tree.set_root("*")
    tree.set_right(0, "8")
    tree.set_left(0, "/")
    tree.set_left(1, "*")
    tree.set_right(1, "+")
    tree.set_left(3, "+")
    tree.set_right(3, "-")
    tree.set_left(7, "5")
    tree.set_right(7, "2")
    tree.set_left(8, "2")
    tree.set_right(8, "1")
    tree.set_left(4,"+")
    tree.set_right(4, "-")
    tree.set_left(9, "2")
    tree.set_right(9, "9")
    tree.set_left(10,"-")
    tree.set_right(10, "1")
    tree.set_left(21, "7")
    tree.set_right(21, "2")

    tree.draw()


