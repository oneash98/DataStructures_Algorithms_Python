class BSTNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, value):
    if rootNode.value == None:
        rootNode.value = value
    elif value <= rootNode.value:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTNode(value)
        else:
            insertNode(rootNode.leftChild, value)
    else:
        if rootNode.rightChild == None:
            rootNode.rightChild = BSTNode(value)
        else: 
            insertNode(rootNode.rightChild, value) 

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.value)
    inOrderTraversal(rootNode.rightChild)

def search(rootNode, value):
    if value == rootNode.value:
        print(value)
    elif value <= rootNode.value:
        if value == rootNode.leftChild.value:
            print(value)
        else:
            search(rootNode.leftChild, value)
    else:
        if value == rootNode.rightChild.value:
            print(value)
        else:
            search(rootNode.rightChild, value)

newBST = BSTNode(None)
insertNode(newBST, 20)
insertNode(newBST, 13)
insertNode(newBST, 23)
insertNode(newBST, 10)
insertNode(newBST, 5)
insertNode(newBST, 30)
insertNode(newBST, 1)

print(search(newBST, 20))