import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):

    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
    
class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        elif self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
            
        elif self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
            
        elif self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
            
        elif self.val == "/":
            return self.left.evaluate() // self.right.evaluate()
            
    

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        curr = None
        for i in postfix:
            curr = TreeNode(i)
            if not i.isdigit():
                curr = TreeNode(i)
                curr.right, curr.left = stack.pop(), stack.pop()
            stack.append(curr)
        return curr
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        
