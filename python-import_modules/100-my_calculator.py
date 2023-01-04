#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    length = len(sys.argv)
    if length < 4:
        print('usage:./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
        elif sys.argv[2] == '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        elif sys.argv[2] == '/':
            print('{} / {} = {}'.formate(a, b, div(a, b)))
        else:
            print('unknown operator.available operators: +, -, *, /')
            sys.exit(1)
