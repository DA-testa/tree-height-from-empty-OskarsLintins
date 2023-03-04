# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    children = {i: [] for i in range(n)}

    for i in range(n):
        if parents[i] != -1:
            children[parents[i]].append(i)

    def max_height(node):
        if not children[node]:
            return 1
        else:
            return 1 + max(max_height(child) for child in children[node])
        
    root = parents.index(-1)
    return max_height(root)

def main(): 
    word = input()

    if word == "I": 
        n = int(input())
        parents = list(map(int, input().split()))

    elif word == "F":
        filename = input()
        with open(filename) as fn:
            n = int(fn.readline())
            parents = list(map(int, fn.readline().split()))

    height = compute_height(n, parents)
    print (height)

    # /workspaces/tree-height-from-empty-OskarsLintins/test/

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()