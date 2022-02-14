#!/usr/bin/env python



#Node class
class Node:
   def __init__(self, new):
      self.left = None
      self.right = None
      self.new = new

   def insert(self, new):
           # what to do if new is less than root
           if new < self.new:
                    if self.left is None:     # if there is no node here
                        self.left = Node(new) # make a node with this value
                    else:                     # if there is a node here
                        self.left.insert(new) # add one to the left
                        
           # what to do if new is greater than root    
           elif new > self.new:
               if self.right is None:
                   self.right = Node(new)
               else:
                    self.right.insert(new)


   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.new),
      if self.right:
         self.right.PrintTree()
               



