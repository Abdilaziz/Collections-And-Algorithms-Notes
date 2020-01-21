
# if self.red is false, node is black
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.red = False
        self.size = None
    
    def getGrandParent(self):
        if self.parent:
            return self.parent.parent
        else:
            return None
    
    def getSibling(self):
        if self.parent:
            if self.parent.left == self:
                return self.parent.right
            else:
                return self.parent.left
        else:
            return None
    
    def getUncle(self):
        if self.parent:
            return self.parent.getSibling()
        else:
            return None


# Self Balancing Order Statistic Tree
class RBTree(object):
    def __init__(self):
        self.root = None
    
    # Tree Search
    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, currentNode, data):
        if currentNode:
            if currentNode.data == data:
                return True
            elif currentNode.data < data:
                return self.search_helper(currentNode.right, data)
            else:
                return self.search_helper(currentNode.left, data)
        return False
    
    def insert(self, data):
        new_node = Node(data)
        # Tree is empty
        if self.root == None:
            self.root = new_node
            return
        currentNode = self.root
        while currentNode != None:
            parent = currentNode
            if data < currentNode.data:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        new_node.parent = parent
        if new_node.data < new_node.parent.data:
            new_node.parent.left = new_node
        else:
            new_node.parent.right = new_node
        self.rebalance_tree(new_node)

    # ensure red-black tree properties are satisfied
    def rebalance_tree(self, new_node):
        print("rebalancing tree")
        while new_node.parent.red and new_node != self.root:
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.red:
                    new_node.parent.red = False
                    uncle.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle.red:
                    new_node.parent.red = False
                    uncle.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.left_rotate(new_node.parent.parent)                   
        self.root.red = False

    def left_rotate(self, new_node):
        print("rotating left")
        sibling = new_node.right
        new_node.right = sibling.left
        if sibling.left != None:
            sibling.left.parent = new_node
        sibling.parent = new_node.parent
        if new_node.parent == None:
            self.root = sibling
        else:
            if new_node == new_node.parent.left:
                new_node.parent.left = sibling
            else:
                new_node.parent.right = sibling
        sibling.left = new_node
        new_node.parent = sibling

    def right_rotate(self, new_node):
        print("rotating right")
        sibling = new_node.left
        new_node.lefright = sibling.right
        if sibling.right != None:
            sibling.right.parent = new_node
        sibling.parent = new_node.parent
        if new_node.parent == None:
            self.root = sibling
        else:
            if new_node == new_node.parent.right:
                new_node.parent.right = sibling
            else:
                new_node.parent.left = sibling
        sibling.right = new_node
        new_node.parent = sibling



    def rebalance_tree2


    # in order traversal
    def print_tree(self):
        self.print_tree_helper(self.root)
    
    def print_tree_helper(self, current):
        if current.left:
            self.print_tree_helper(current.left)
        print(current.data, current.parent, current.red)
        if current.right:
            self.print_tree_helper(current.right)


# Set up tree
tree = RBTree()

# Insert elements
# tree.insert(10)
# tree.insert(4)
# tree.insert(2)
# tree.insert(-1)
# tree.insert(1)
# tree.insert(3)
# tree.insert(5)

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

# Check search
# Should be True
# print(tree.search(4))
# Should be False
# print(tree.search(6))

tree.print_tree()