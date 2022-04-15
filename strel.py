import lexer
import parser

# solve the equation for the given variable and return its value
def solve(equation, variable):
    print('Equation:', equation)
    print()

    # get rid of all the whitespace
    equation = equation.replace(' ', '')
    
    # split the equation into lhs and rhs expressions
    lhs, _, rhs = equation.partition('=')

    # tokenize both the expressions
    lhs_tokens = lexer.tokenize(lhs)
    rhs_tokens = lexer.tokenize(rhs)

    # parse the tokens into abstract syntax trees
    lhs_tree = parser.parse(lhs_tokens)
    rhs_tree = parser.parse(rhs_tokens)

    print('LHS Tree:')
    parser.print_tree(lhs_tree.root)
    print()

    print('RHS Tree:')
    parser.print_tree(rhs_tree.root)
    print()

    # TODO: solve the equation
