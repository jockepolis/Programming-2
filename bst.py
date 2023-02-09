""" bst.py

Student: Joakim Svensson
Mail: joakim.svensson7535@gmail.com
Reviewed by: Nandini M S
Date reviewed: 4th October 2022
"""

import random
from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)
    
    def _height(self,r):
        if r is None:
            return 0
        else:
            Lheight = self._height(r.left)
            Rheight = self._height(r.right)
            maxHeight = Lheight
            if Rheight > maxHeight:
                maxHeight = Rheight
            return maxHeight + 1

    def remove(self, key):
        if not self.contains(key):
            return False
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if k < r.key:
            r.left = self._remove(r.left, k)
        elif k > r.key:
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                self.root = r.right
                mini = self.smallestkey()
                r.key = mini
                r.right = self._remove(r.right, mini)
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above


    def smallestkey(self):
        r = self.root
        while r.left:
            r = r.left
        return r.key


    def __str__(self):                            # Compulsory
        if self.root is None:
            return '<>'
        lst = self.to_list()
        result = '<' + str(lst[0])
        for i in range(len(lst[1:])):
            result += ', ' + str(lst[i+1])
        return result + '>'

    def to_list(self):                            # Compulsory
        lst = list()
        self._to_list(self.root, lst)
        return lst

    def _to_list(self, r, lst):
        if r is not None:
            self._to_list(r.left, lst)
            lst.append(r.key)
            self._to_list(r.right, lst)


    def to_LinkedList(self):                      # Compulsory
        lst = LinkedList()
        lst2 = self.to_list()
        for i in lst2:
            lst.insert(i)
        return lst

    "Komplexiteten för denna är O(n * log(n)), då det är log(n) för att gå igenom bst och sedan n för att gå igenom vanliga listan."

    def ipl(self):                                # Compulsory
        return self._ipl(self.root, 1)
        
    def _ipl(self, r, level):
        if r is None:
            return 0
        else:
            return self._ipl(r.left, level+1) + self._ipl(r.right, level+1) + level
            

def random_tree(n):                               # Useful
    bst = BST()
    for i in range(n):
        randomkey = random.random()
        bst.insert(randomkey)
    return bst


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")


    n = 500
    randomtree = random_tree(n)
    ipl = randomtree.ipl()
    print(ipl/n)
    height = randomtree.height()
    print(height)


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size?
2. computing height?
3. contains?
4. insert?
5. remove?

Svar:
Man skulle kunna använda generatorn till samtliga funktioner men endast för size är den "bra" att använda. 
Generatorn går igenom hela trädet och returnerar varenda key. Blir onödig komplexitet för många av funktionerna
men för funktionen 1. computing size är den bra, för där behöver man ändå gå igenom varenda nod i trädet.



Results for ipl of random trees
===============================
Svar:
När n = 20 är det ungefär 4-5 nodbesök oftast för det experimentella (men ibland 6-7 nodbesök) och teoretiskt är det 6 nodbesök.
När n = 20 är höjden mellan 6-8 för trädet men när n = 40 är höjden i alla fall 10. Man kan gör exemplen med ännu större
skillnad och det är tydligt att höjden beror på antalet noder n. Vad är det egentligen för samband?
n = 100 -> ipl/n = 7.06 -> Height = 13.
n = 300 -> ipl/n = 8.75 -> Height = 17.
n = 500 -> ipl/n = 10.83 -> Height = 20.

Om man skulle beskriva sambandet de två emellan är det att ipl/n = (height/2) + 1. Det är åtminstone ungefär vad jag får fram
för mina experimentella värden.

"""
