import lexer

# This function has been copied off of stackoverflow
# and very little changes have been made.
# I may or may not implement this myself. I only need
# it for debugging purposes now.
# https://stackoverflow.com/a/65865825
def print_tree(root, value="value", left="left", right="right"):
    def display(root, value=value, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, value)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, value)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, value)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, value)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, value, left, right)
    for line in lines:
        print(line)

class Tree:
    def __init__(self, root):
        self.root = root

    def add_operation(self, tree):
        tree.root.left = self.root
        self.root = tree.root

def parse(tokens):
    # TODO: preprocessing
    tree = make_tree(tokens)
    return tree

def parse_parens(tokens):
    extra_oparens = 0
    extra_cparens = 0
    for index, token in enumerate(tokens):
        if token.type == 'oparen':
            extra_oparens += 1
        elif token.type == 'cparen':
            if extra_cparens == extra_oparens:
                break
            extra_cparens += 1
    paren_tokens = tokens[:index]
    tokens1 = tokens[index + 1:]
    tree = make_tree(paren_tokens)
    return tree, tokens1

def make_tree(tokens):
    node = tokens.pop(0)

    if len(tokens) == 0:
        tree = Tree(node)
        return tree

    if node.type == 'oparen':
        tree, tokens = parse_parens(tokens)
        if len(tokens) != 0:
            tree1 = make_tree(tokens)
            tree.add_operation(tree1)
        return tree

    if node.type == 'operator':
        tree = Tree(node)
        tree.root.right = make_tree(tokens).root
        return tree

    tree = Tree(node)
    tree1 = make_tree(tokens)
    tree.add_operation(tree1)
    return tree
