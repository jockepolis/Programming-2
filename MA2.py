"""
Solutions to module 2 - A calculator
Student: Joakim Svensson
Mail: joakim.svensson7535@gmail.com
Reviewed by: Oliver Groth
Reviewed date: 19 september 2022
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math 
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    if wtok.is_at_end():
        wtok.next()
    else:
        result = assignment(wtok, variables)
        wtok.next()
        if  not wtok.is_at_end():
            raise SyntaxError("Not end of line")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("No variable following '='")
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ['+', '-']:
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else:
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in ['*', '/']: 
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        else: 
            wtok.next()
            try:
                result = result / factor(wtok, variables)
            except:
                raise EvaluationError('No 0 division')
    return result

def arglist(wtok,variables):
    arglst = []
    if wtok.get_current() == '(':
        wtok.next()
        arglst = [assignment(wtok,variables)]
        while wtok.get_current() == ',':
            wtok.next()
            arglst.append(assignment(wtok,variables))
        if wtok.get_current() == ')':
            wtok.next()
        else:
            raise SyntaxError("Expected ')'")
    else:
        raise SyntaxError("Expected '('")
    return arglst

def factor(wtok, variables):
    """ See syntax chart for factor"""
    function_1 = {'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 'log': math.log, 'fib': fib_memoization, 'fac': fac}
    function_n = {'sum': sum, 'max': max, 'min': min, 'mean': mean}
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in function_1:
        func1 = function_1.get(wtok.get_current())
        wtok.next()
        if wtok.get_current() == '(':
            wtok.next()
            arg = assignment(wtok,variables)
            try:
                result = func1(arg)
            except:
                raise EvaluationError(f'Illegal argument {arg} with')
            if wtok.get_current() == ')':
                wtok.next()
            else:
                raise SyntaxError("Expected ')'")
        else:
            raise SyntaxError("Expected '('")

    elif wtok.get_current() in function_n:
        funcn = function_n.get(wtok.get_current())
        wtok.next()
        result = funcn(arglist(wtok,variables))

    elif wtok.get_current() in variables:
        result = variables.get(wtok.get_current())
        wtok.next()

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.get_current() == '-':
        wtok.next()
        result = - factor(wtok,variables)
    
    elif wtok.is_name() and wtok.get_current() not in variables:
        raise EvaluationError("Does not work")

    else:
        raise SyntaxError("Expected number or '('")

    return result

def fac(n):
    """ Computes and returns n!""" 
    if n==0:
        return 1
    else:
        return n*fac(n-1)

def fib_memoization(n):
    memory = {0:0, 1:1}

    def _fib(n):
        if n not in memory:
             memory[n] = _fib(n-1) + _fib(n-2)
        return memory[n]
    return _fib(n) 

def mean(n):
    return sum(n)/len(n)

def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi,}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print(variables)
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvaluationError as pe:
                print("*** Evaluation: ", pe.arg)
                print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()