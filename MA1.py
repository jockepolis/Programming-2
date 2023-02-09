"""
Solutions to module 1
Student: Joakim Svensson
Mail: joakim.svensson7535@gmail.com
Reviewed by: Fredrik Hammarberg
Reviewed date: 7/9 - 2022
"""

import random
import time


def power(x, n):         # Optional
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)


def multiply(m, n):      # Compulsory
    assert m >= 0, 'Endast positiva tal'
    assert n >= 0, 'Endast positiva tal'
    assert type(m) == int, 'Endast heltal'
    assert type(n) == int, 'Endast heltal'
    if m == 0:
        return 0
    if n == 0:
        return 0
    else:
        return m+multiply(m,n-1)


def divide(t, n):        # Optional
    pass


def harmonic(n):         # Compulsory
    assert n > 0, 'Endast positiva tal'
    assert type(n) == int, 'Endast heltal'
    if n < 2:
        return 1
    else:
        return 1/n + harmonic(n-1)



def digit_sum(x):        # Optional
    pass


def get_binary(x):       # Optional
    pass


def reverse(s):          # Optional
    pass


def largest(a):          # Compulsory
    assert type(a) == list, 'Endast en lista är godtagbar'
    if len(a) == 1:
        return a[0]
    else:
        maximum = largest(a[1:])
    if maximum > a[0]:
        return maximum
    else:
        return a[0]


def count(x, s):         # Compulsory
    if s == []:
        return 0
    elif s[0] == x:
        return 1 + count(x,s[1:])
    elif type(s[0]) == list:
        return count(x,s[0]) + count(x,s[1:])
    else:
        return count(x,s[1:])



def zippa(l1, l2):       # Compulsory
    assert type(l1) == list, 'Endast en lista är godtagbar'
    assert type(l2) == list, 'Endast en lista är godtagbar'
    l3 = []
    if l1 == [] and l2 == []:
       return l3
    if l1 != [] and l2 == []:
       return l3 + l1
    if l1 == [] and l2 != []:
       return l3 + l2
    if l1 != [] and l2 != []:
       if l1[0] <= l2[0]:
          l3.append(l1[0])
          l3 = l3 +  zippa(l1[1:], l2)
       if l1[0] > l2[0]:
          l3.append(l2[0])
          l3 = l3 + zippa(l1, l2[1:])
    return l3


def bricklek(f, t, h, n): # Compulsory
    if n == 1:
        return [f'{f}->{t}']
    else:
        return bricklek(f, h, t, n-1) + [f'{f}->{t}'] + bricklek(h, t, f, n-1)



def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    print('Bye!')
    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  Svar: Om det är två brickor behövs tre förflyttningar. Om det är tre brickor behövs 7 förflyttningar, o.s.v.
  Således är formeln för antalet förflyttningar för antalet brickor 2^n - 1, står i dokumentet också.
  Alltså, om det är 50 brickor -> 2^50 -1 = 1.13e+15 förflyttningar -> 1.13e+15 sekunder = 36 miljoner år ungefär.
  
  
  Exercise 17: Time for Fibonacci:
  Svar: a) För fib(30) = 0.18222... sekunder och fib(29) = 0.11257... sekunder. 0.1822/0.11257 = 1.618 (ungefär).
  Det är därför verifierat.

  b) För att ta reda på vad fib(50) och fib(100) tar så utnyttjar vi svaren i a) för att kunna beräkna det.
  Vi gör det enligt följande "formel": 1.618^(n)*c. Så vi beräknar konstanten c genom att använda sig av svaret
  för när n = 29. c = 0.11257.../1.618^(29) = 9.796e-8.

  fib(50) = 9.796e-8 * 1.618^(50) = 45.9 minuter.
  fib(100) = 9.796e-8 * 1.618^(100) = 2 454 000 år.
  
  
  Exercise 20: Comparison sorting methods:
  Svar: För instickssorteringen (O(n^2)) gäller enligt uppgiften att konstanten c = 1e-6. Därför tar det för 1e+6 samt 1e+9
  slumptal, alltså 1e+6 respektive 1e+12 sekunder. 
  Instickssortering: 1e+6 slumptal -> 11.57 dagar.
                     1e+9 slumptal -> 31.69 år.

  För merge-sortering (O(n log (n))) gäller enligt uppgiften att konstanten c = 3.33e-4. Därför gäller:
  Mergesortering:    1e+6 slumptal -> 33.3 minuter.
                     1e+9 slumptal -> 5.7 år.
  
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n):
  Svar: Alltså, n < c * n * log(n) -> n/c * n < log(n) -> 1/c < log(n) -> n > 10^(1/c).
  Konstanten c kan lösas genom att använda sig av det som är givet i uppgiften, dvs att c * 10 * log(10) = 1 sekund.
  Detta ger att c = 0.1 Således måste n > 10^(1/c) = 10^(10) = 10 000 000 000



"""