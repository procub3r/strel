import strel

equation = '(((2 * x) + 4) * 4) + ((9 + 2) * 4) = 10 * (x + 32) * 2'
x = strel.solve(equation, 'x')

print('The value of x is:', x)
