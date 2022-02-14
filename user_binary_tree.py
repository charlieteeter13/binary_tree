#!/usr/bin/env python

from binary_tree import Node


# number of elements
n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
 
print("\nList is - ", a)

root = Node(a[0])

num = n
for x in a:
    root.insert(x)

root.PrintTree()



