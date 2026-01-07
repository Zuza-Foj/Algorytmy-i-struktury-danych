from binary_tree import BinaryTree


def derivative(tree, index=0, var='x'):
    if index >= len(tree.tree) or tree.tree[index] is None:
        return "0", ""

    val = str(tree.tree[index])
    left_idx = 2 * index + 1
    right_idx = 2 * index + 2

    if tree.get_left(index) is None and tree.get_right(index) is None:
        if val == var:
            d_val = "1"
        else:
            d_val = "0"
        return d_val, val

    d_left, e_left = derivative(tree, left_idx, var)
    d_right, e_right = derivative(tree, right_idx, var)

    if val == '+':
        d_res = f'{d_left} + {d_right}'
        e_res = f'{e_left} + {d_right}'
        return d_res, e_res
    elif val == '-':
        d_res = f'{d_left} - {d_right}'
        e_res = f'{d_left} - {d_right}'
        return d_res, e_res
    elif val == '*':
        d_res = f'{d_left} * {e_right} + {e_left} * {d_right}'
        e_res = f'{e_left} * {e_right}'
        return d_res, e_res
    elif val == '/':
        d_res = f'({d_left} * {e_right} - {e_left} * {d_right}) / ({e_right}) ** 2'
        e_res = f'{e_left} / {e_right}'
        return d_res, e_res

    return "0", val


if __name__ == "__main__":
    my_tree = BinaryTree()

    my_tree.set_root("*")
    my_tree.set_right(0, "x")
    my_tree.set_left(0, "/")
    my_tree.set_left(1, "*")
    my_tree.set_right(1, "+")
    my_tree.set_left(3, "+")
    my_tree.set_right(3, "-")
    my_tree.set_left(7, "5")
    my_tree.set_right(7, "x")
    my_tree.set_left(8, "2")

    print(derivative(my_tree, 0, 'x'))




