import random
import time
import math

class point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def norm2(self):
        return math.sqrt(self.x*self.x + self.y*self.y)


def fib(n):
    if n < 2:
        return 1
    else:
        x = fib(n-1)
        y = fib(n-2)
        return x + y

def sum(a,b):
    sum = 0
    for i in range(a,b):
        sum += i
    return sum

def sumlist(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum

def myrange(a,b):
    c = []
    i = a
    while i < b:
        c.append(i)
        i += 1
    return c

def med3(a,b,c):
    if a <= b:
        if b <= c: 
            return b
        elif c <= a:
            return a
        else:
            return c
    else:
        if c <= b:
            return b
        elif a <= c:
            return a
        else:
            return c
    
def qs_sub(l,left,right):
    if left < right:
        i = left
        j = right
        p = med3(l[i],l[j],l[(j-i)/2])
        while 1:
            while l[i] < p:
                i += 1
            while l[j] > p:
                j -= 1
            if i >= j:
                break
            t = l[i]
            l[i] = l[j]
            l[j] = t
            i += 1
            j -= 1
        qs_sub(l,left,i-1)
        qs_sub(l,j+1,right)

def qs(l):
    qs_sub(l,0,len(l)-1)

def random_ints(a,n):
    l = []
    for i in range(0,n):
        l.append(random.randint(0,a))
    return l

def check_sorted(l):
    f = True
    for i in range(0,len(l)-1):
        if l[i] > l[i+1]:
            f = False
            break
    return f

def measure_qs(n):
    start = time.time()
    a = random_ints(10000,n)
    qs(a)
    end = time.time()

    if check_sorted(a):
        print "OK"
    else:
        print "NG"

    print n, "elems in", end-start, "sec"


    
class bs_tree:

    class bs_tree_node:
        def __init__(self,x):
            self.right = None
            self.left = None
            self.data = x

    def __init__(self):
        self.root = None

    def insert(self,x):
        self.root = self.insert_sub(self.root,x)

    def insert_sub(self,node,x):
        if node == None:
            return self.bs_tree_node(x)
        elif node.data == x:
            return node
        elif node.data < x:
            node.right = self.insert_sub(node.right,x)
        elif node.data > x:
            node.left = self.insert_sub(node.left,x)
        return node

    def all_vals_list(self):
        list = []
        self.all_vals_list_sub(self.root,list)
        return list
        
    def all_vals_list_sub(self,node,list):
        if node:
            print node.data
            if node.left:
                self.all_vals_list_sub(node.left,list)

            list.append(node.data)

            if node.right:
                self.all_vals_list_sub(node.right,list)
        
        
