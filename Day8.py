'''A unival tree (which stands for "universal value") is a tree where all
nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None

def unival(root,count):
    if root is None:
        return  True
    left  = unival(root.left,count)
    right  = unival(root.right,count)
    if left == False or right==False:
        return False
    if root.left and root.data!=root.left.data:
        return False
    if root.right and root.data!=root.right.data:
        return False
    count[0]+=1
    return True

def countTree(root):
    count=[0]
    unival(root,count)
    return count[0]

root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)
countTree(root)
print ("Count of Single Valued Subtress is" , countTree(root) )
