import sys
class BSTNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None


    def search(rootNode, data):
        if rootNode is None:
            print("{} not found".format(data))
            return False

        elif rootNode.data == data:
            print("{} found".format(data))
            return True

        elif rootNode.data < data:
            return search(rootNode.right, data)

        else: # self.data > data
            return search(rootNode.left, data)



    def deleteNode(parent, curr, data):

        if curr is None: # not found, return
            return

        elif data < curr.data:
            self.deleteNode(curr, curr.left, data)

        elif data > curr.data:
            self.deleteNode(curr, curr.right, data)

        else: # found node to delete

            # case 1: curr has no children
            if curr.right is None and curr.left is None:
                if parent.right is curr:
                    parent.right = None
                else:
                    parent.left = None

                # curr = None

            # case 2: curr has only one child
            elif curr.right is None: # has a left child
                if parent.right is curr:
                    parent.right = curr.left
                else:
                    parent.left = curr.left

            elif curr.left is None: #has a right child
                if parent.right is curr:
                    parent.right = curr.right
                else:
                    parent.left = curr.right

                # curr = None

            #case 3: curr has two children
            else:
                prev = curr
                ptr = curr.right

                # find first in order successor
                while(ptr.left != None):
                    prev = ptr
                    ptr = ptr.left

                curr.data = ptr.data
                prev.left = None

            #print("{} deleted".format(data))




    def delete(self, data):
        if self.root is None:
            return

        self.deleteNode(None, self.root, data)


    # insert functions
    def insertNode(self, curr, data):

        if curr is None:
            curr = BSTNode(data, None, None)
            print("{} inserted".format(data))


        elif curr.data == data: # node already in tree
            return

        elif data < curr.data:
            if curr.left is None:
                curr.left = BSTNode(data, None, None)
            else:
                self.insertNode(curr.left, data)

        else: # data > curr.data
            if curr.right is None:
                curr.right = BSTNode(data, None, None)
            else:
                self.insertNode(curr.right, data)

    def insert(self, data):

        if self.root is None:
            self.root = BSTNode(data, None, None)
            # print("{} inserted".format(data))
            return

        self.insertNode(self.root, data)

    # inorder Traversal functions
    def inorderPrint(self, curr):
        if curr is None:
            return

        self.inorderPrint(curr.left)
        print("{} ".format(curr.data), end=" ");
        self.inorderPrint(curr.right)

    def inorder(self):
        self.inorderPrint(self.root)








# testing

newBST = BST()

newBST.insert(25)
newBST.insert(30)
newBST.insert(15)
newBST.insert(5)
newBST.insert(20)
newBST.insert(17)
newBST.insert(20)

newBST.inorder()
