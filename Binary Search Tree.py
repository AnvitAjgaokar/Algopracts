# binary search tree

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def preorder(root):
    if root is not None:
        print(root.key, end =" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key , end=" ")


def insert(node,key):
    if node is None:
        return Node(key)
    else:
        if node.key == key:
            return node
        elif node.key < key:
            node.right = insert(node.right, key)
        else:
            node.left = insert(node.left, key)
    return node


def minvalueNode(node):
    current = node

    while(cuurent.left is not None):
        current =  current.left

    return current

def deleteNode(root,key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left,key)

    elif key > root.key:
        root.right = deleteNode(root.right,key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minvalueNode(root.right)
        root.key = temp.key

        root.right = deleteNode(root.right,temp.key)

    return root


num = int(input("How many Elements you have : "))
list1 = []
for i in range(1, num + 1):
    a = int(input(f'Enter Element No. {i} : '))
    list1.append(a)

tr = Node(list1[0])
for i in range(1, len(list1)):
    tr = insert(tr, list1[i])




preorder(tr)
print("\n")
inorder(tr)
print("\n")
postorder(tr)
print("\n")



print(f"After deletion: ")
num1 = int(input("delete : "))
tr = deleteNode(tr,num1)

preorder(tr)
print("\n")
inorder(tr)
print("\n")
postorder(tr)
print("\n")
