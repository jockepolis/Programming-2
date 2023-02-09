""" linked_list.py

Student: Joakim Svensson
Mail: joakim.svensson7535@gmail.com
Reviewed by: Nandini M S
Date reviewed: 4th October 2022
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

        def length(self):
            if self.succ is None:
                return 1
            else:
                return 1 + self.succ.length()
        


    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        f = self.first
        while f:
            yield f.data
            f = f.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        f = self.first            # Method 1
        if f is None:
            return 0
        else:
            return f.length()


    def mean(self):               # Optional
        pass

    def remove_last(self):        # Optional
        pass

    def remove(self, x):
        if self.first is None:
            return False
        if self.first.data == x:
            self.first = self.first.succ
            return True
        else:
            f = self.first
            while f.succ and f.succ.data != x:
                f = f.succ
            if f.succ is None:
                return False
            else:
                f.succ = f.succ.succ
                return True
    


    def count(self, x):          # Optional
        pass



    def to_list(self):            # Compulsory
        return self._to_list(self.first)

    def _to_list(self, f):
        if f is None:
            return []
        else:
            return [f.data] + self._to_list(f.succ)



    def remove_all(self, x):      # Compulsory
        self.first = self._remove_all(x, self.first)

    def _remove_all(self, x, f):
        if f is None:
            return None
        elif f.data == x:
            return self._remove_all(x, f.succ)
        else:
            f.succ = self._remove_all(x,f.succ)
            return f



    def __str__(self):            # Compulsary
        result = '('
        f = self.first
        if f != None:
            result += str(f.data)
            f = f.succ
            while f:
                result += ', ' + str(f.data)
                f = f.succ
        result += ')'
        return result

    def _copy(self):               # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 

        Eftersom vi alltid plockar det elementet sist i listan måste vi gå igenom hela den en massa gånger, 
        komplexiteten blir då O(n^2). Bör kunna gå att göra den effektivare.

    '''

    def copy(self):               # Compulsary
        cpy = self.to_list()      # Should be more efficient
        res = LinkedList()
        res.first = res.Node(cpy[-1], res.first)
        for i in range(len(cpy)-2, -1, -1):
            res.first = res.Node(cpy[i], res.first)
        return res
    ''' Complexity for this implementation:

        Här skapar jag en kopia av listan som en standardlista och plockar det sista elementet och sen itererar åt andra hållet, 
        således blir komplexiteten för detta endast O(n).

    '''

    def __getitem__(self, ind):   # Compulsory
        f = self.first
        if (self.length()-1) < ind:
            return None
        j = 0
        while j < ind:
            f = f.succ
            j += 1
        return f.data



class Person:                     # Compulsory to complete

    "Klassen Person borde egentligen vara inuti linkedlist, dvs där Node-klassen är. Nu ska den inte vara det av hanteringsskäl."

    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}: {self.pnr}"

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:


if __name__ == '__main__':
    main()
