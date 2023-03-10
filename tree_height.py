# python3

import sys
import threading
import numpy
import os

def compute_height(n, parents):
    children = {i: [] for i in range(n)}

    for i in range(n):
        if parents[i] != -1:
            children[parents[i]].append(i)

    def max_height(i):
        if not children[i]:
            return 1
        else:
            return 1 + max(max_height(child) for child in children[i])
        
    root = parents.index(-1)
    return max_height(root)

def main(): 
    word = input()

    if 'I' in word: 
        n = int(input())
        parents = list(map(int, input().split()))

    elif word[0] == "F":
        filename = input().strip()
        filepath = os.path.join(os.getcwd(),'test/' + filename)
        if filename.endswith("a"):
            return
        else:
            with open(filepath, 'r') as fn:
                n = int(fn.readline())
                parents = list(map(int, fn.readline().split()))

    height = compute_height(n, parents)
    print (height)

# /workspaces/tree-height-from-empty-OskarsLintins/test/    
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()