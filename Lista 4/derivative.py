from binary_tree import BinaryTree

def simplify(val, left, right):
    if val == '+':
        if left == "0": return right
        if right == "0": return left

    elif val == '-':
        if right == "0": return left
        if left == "0": return f"-({right})"
        if left == right: return "0"

    elif val == '*':
        if left == "0" or right == "0": return "0"
        if left == "1": return right
        if right == "1": return left

    elif val == '/':
        if left == "0": return "0"
        if right == "1": return left
        if left == right: return "1"

    return f'({left} {val} {right})'

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

    if val in ['+', '-', '*', '/']:
        e_res = f'({e_left} {val} {e_right})'

        if val == '+':
            d_res = simplify('+', d_left, d_right)
        elif val == '-':
            d_res = simplify('-', d_left, d_right)
        elif val == '*': # (f*g)' = f'g + fg'
            f = simplify('*', d_left, e_right)
            g = simplify('*', e_left, d_right)
            d_res = simplify('+', f, g)
        elif val == '/': # (f/g)' = (f'g - fg') / g^2
            f = simplify('*', d_left, e_right)
            g = simplify('*', e_left, d_right)
            num = simplify('-', f, g)
            d_res = f'({num} / ({e_right})**2)'

        return d_res, e_res


    elif val == 'sin':
        d_res = simplify('*', f'cos({e_left})', d_left)
        return d_res, f'sin({e_left})'

    elif val == 'cos':
        d_res = simplify('*', f'(-sin({e_left}))', d_left)
        return d_res, f'cos({e_left})'

    return "0", val


if __name__ == "__main__":
    my_tree = BinaryTree()

    my_tree.set_root("/")
    my_tree.set_right(0, "+")
    my_tree.set_left(0, "*")
    my_tree.set_left(1, "sin")
    my_tree.set_right(1, "x")
    my_tree.set_left(3, "x")
    my_tree.set_left(2, "x")
    my_tree.set_right(2, "6")


    print(derivative(my_tree, 0, 'x'))




