"""
File m3.py for exam 2022-10-28

Name: Joakim Svensson

"""

# No other imports are allowed
import math
import random
import time


class LinkedList:
    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '<' + ', '.join((str(x) for x in self)) + '>'

    def insert(self, data):
        if self.first == None or data < self.first.data:
            self.first = self.Node(data, self.first)
        else:
            prev = self.first
            while prev.succ and (data > prev.succ.data):
                prev = prev.succ
            prev.succ = self.Node(data, prev.succ)


def build_list(n):  # A6: Should be analysed
    llist = LinkedList()
    for x in range(3*n):
        llist.insert(x)
    return llist


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        if self.root:
            yield from self.root

    def insert(self, key):
        def _insert(key, r):
            if r is None:
                return self.Node(key)
            elif key < r.key:
                r.left = _insert(key, r.left)
            elif key > r.key:
                r.right = _insert(key, r.right)
            else:
                pass  # Already there
            return r
        self.root = _insert(key, self.root)

    def __str__(self):
        return '<' + ', '.join([str(x) for x in self]) + '>'

    def copy(self):

        def _copy(r):  # A5
            if r is None:
                return None
            root_copy = self.Node(r.key)
            root_copy.left = _copy(r.left)
            root_copy.right = _copy(r.right)
            return r

        return BST(_copy(self.root))


class LevelOrderIterator:  # Task B3
    pass


def main():
    # Code for timing the build_list function
    # Har tagit hjälp av kod från en tidigare tenta där "timing" också används!
    print('\nA5: Time complexity for build_list:')
    measured = []
    for n in [1000, 2000, 4000, 8000]:
        tstart = time.perf_counter()
        print(n, end ='\t')
        build_list(n)
        dt= time.perf_counter()-tstart
        measured.append(dt)
        print(f" {dt:5.1f}")
    print('\nTime growth when doubling the input:' )  
    for i in range(1,len(measured)):
        print(f'{measured[i]/measured[i-1]:5.1f}')  

    print('\nEstimation of time for build_list(1000000)')
    n = 10000
    tstart = time.perf_counter()
    build_list(n)
    dt= time.perf_counter()-tstart
    print(f"Time for {n}: {dt:5.1f}")
    # Code for trying the copy method in class BST
    bst = BST()
    for x in (5, 3, 2, 4, 8, 10, 6, 1, 7, 9):
        bst.insert(x)
    print('\nA6: copy')
    copy = bst.copy()
    print('original:', bst)
    print('copy    :', copy)

    # Code for demonstrating the level order iterator
    print('\nB3: LevelOrderIterator')
    bst = BST()
    print('Insertion order: ', end=' ')
    for x in [5, 3, 2, 4, 8, 10, 6, 1, 7, 9]:
        print(x, end=' ')
        bst.insert(x)
    print('\nSymmetric order: ', end=' ')
    for x in bst:
        print(x, end=' ')
    print('\nLevel order    : ', end=' ')
    exit()  # Remove this line for testing the iterator
    loi = LevelOrderIterator(bst)
    for x in loi:
        print(x, end=' ')
    print()

    print('\n\nDone')


if __name__ == '__main__':
    main()

''' Answer to A6
Output from the timing of the build_list function
=================================================
A5(ska vara A6 egentligen men ni har skrivit fel i main): 
Time complexity for build_list:
1000       0.4
2000       1.7
4000       6.7
8000      27.1

Time growth when doubling the input:
  4.0
  4.0
  4.0

Estimation of time for build_list(1000000)
Time for 10000:  42.6

Reasoning and motivation
========================
Det framgår väldigt tydligt att komplexiteten beror av parametern n genom O(n^2). Det framgår genom att när vi dubblerar
inputen från n -> 2n blir "the time growth" 4. Den blir alltså n^2.

Vad blir det när n = 1 miljon?
Jo, när n = 10 000 tar det 42.6 sekunder på min dator. Så 46,2 sekunder multiplicerat med 100^2 motsvarar
tiden det tar för n = 1 000 000. Detta ger:
46,2 sekunder * 100^2 = 46 200 sekunder = 7700 minuter = 128,33 timmar = 5,35 dagar ungefär.



'''
