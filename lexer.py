import re

class Node:
    def __init__(self, type, value=None):
        # type value of the node
        self.type = type
        self.value = value

        # left and right children of the node
        self.left = None
        self.right = None

    def __repr__(self):
        return f'node type: {self.type}, value: {self.value}'

# different types of tokens and regexes to match them
token_classes = [
    ('oparen', re.compile('\(')),
    ('cparen', re.compile('\)')),
    ('number', re.compile('-*[0-9]+\.*[0-9]*')),
    ('operator', re.compile('[/*+-]')),
    ('variable', re.compile('[a-zA-Z]')),
]

def tokenize(expression):
    tokens = []
    while expression != '':
        for type, pattern in token_classes:
            match = pattern.match(expression)
            if match is not None:
                token = Node(type, match.group())
                tokens.append(token)
                expression = expression[match.end():]
                break
    return tokens
