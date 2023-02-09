"""
Solutions to module 2 - A calculator
Student: Astor Gulz
Mail: astorgulz@hotmail.com
Reviewed by: Kellen
Reviewed date: 20 sept 2021
"""
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper
import math

class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg

var = {'PI': math.pi, 'e': math.e}

def assignment(wtok):
    result = expression(wtok)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            var[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError(f'No variable following "=" ')
    return result

def expression(wtok):
    result = term(wtok)
    # print('expression')
    while wtok.get_current() in ('+', '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok)
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok)
    return result

def term(wtok):
    result = factor(wtok)
    # print('term')
    while wtok.get_current() in ('*', '/'):
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok)
        elif wtok.get_current() == '/':
            wtok.next()
            if wtok.get_current() == '0':
                raise EvaluationError("No 0 division!!")
            result = result / factor(wtok)
    return result

def factor(wtok):
    # print('factor')
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok)
        if wtok.get_current() == ')':
            wtok.next()
            return result
        else:
            raise SyntaxError("Expected ')'")

    elif wtok.is_name():
        if wtok.get_current() in var:
            result = var[wtok.get_current()]
            wtok.next()
            return result

        elif wtok.get_current() in fun:
            func = fun[wtok.get_current()]
            func_name = wtok.get_current()
            wtok.next()
            if wtok.get_current() == '(':
                wtok.next()
                arg = assignment(wtok)
                try:
                    result = func(arg)
                except:
                    raise EvaluationError(f'Illegal argument {arg} with')
                if wtok.get_current() == ')':
                    wtok.next()
                else:
                    raise SyntaxError("Expected '('")
                return result
        elif wtok.get_current() in fun_n:
            func_n = fun_n[wtok.get_current()]
            wtok.next()
            lst = []
            if wtok.get_current() == '(':
                wtok.next()
                while True:
                    lst.append(wtok.get_current())
                    wtok.next()
                    if wtok.get_current() == ',':
                        wtok.next()
                    else:
                        break
                if wtok.get_current() == ')':
                    wtok.next()
                else:
                    raise SyntaxError("Expected ')'")
            lst = [int(i) for i in lst]
            result = func_n(lst)
            wtok.next()
            return result
        else:
            raise SyntaxError(f'There is not such a variable/function:{wtok.get_current()}')
    elif wtok.get_current() == '-':
        wtok.next()
        result = - factor(wtok)
        return result
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
        return result
    else:
        raise SyntaxError('Expected number or (')
    return

memory = {0: 0, 1: 1}
def fib(wtok):
    if wtok not in memory:
        memory[wtok] = fib(wtok - 1) + fib(wtok - 2)
    return memory[wtok]
def sin(wtok):
    return math.sin(wtok)
def cos(wtok):
    return math.cos(wtok)
def exp(wtok):
    return math.e ** wtok
def log(wtok):
    return math.log(wtok)
def mean(wtok):
    return sum(wtok) / len(wtok)
def fac(wtok):
    return math.factorial(wtok)

fun = {'fib': fib, 'sin': sin, 'cos': cos, 'log': log, 'exp': exp, 'fac': fac}
fun_n = {'sum': sum, 'max': max, 'min': min, 'mean': mean}

def file(name):
    lst = []
    with open(name, 'r') as file2:
        lines = file2.readlines()
        for row in lines:
            lst.append(row)
    return lst
pass

def main():
    print("Calculator version 0.2")
    lines = []
    while True:
        if lines == []:
            line = input("Input : ")
        else:
            line = lines.pop(0)
        wtok = TokenizeWrapper(line)
        try:
            if wtok.get_current() == 'quit':
                break
            #### TEST-file
            if wtok.get_current() == 'file':
                test_lst = file('MA2test.txt')
                lines += test_lst
            else:
                result = assignment(wtok)
                if wtok.is_at_end():
                    print('Result: ', result)
                    var["ans"] = result
                    var["vars"] = result
                else:
                    raise SyntaxError('Unexpected token')
        except SyntaxError as se:
            print("*** Syntax: ", se.arg)
            print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")
        except EvaluationError as pe:
            print("*** Evaluation: ", pe.arg)
            print(f"Error ocurred at '{wtok.get_current()}'" +
                  f" just after '{wtok.get_previous()}'")
        except TokenError:
            print('*** Syntax: Unbalanced parentheses')
    print('Bye!')
if __name__ == "__main__":
    main()
