# with just one class

class BSTNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def search(rootNode, data):
        if rootNode is None:
            # print("{} not found".format(data))
            return False

        elif rootNode.data == data:
            # print("{} found".format(data))
            return True

        elif rootNode.data < data:
            return BSTNode.search(rootNode.right, data)

        else: # self.data > data
            return BSTNode.search(rootNode.left, data)

    def delete(parent, curr, data):

        if curr is None: # not found, return
            return

        elif data < curr.data:
            BSTNode.delete(curr, curr.left, data)

        elif data > curr.data:
            BSTNode.delete(curr, curr.right, data)

        else: # found node to delete

            # case 1: curr has no children
            if curr.right is None and curr.left is None:

                if parent is None:
                    print("Delete Root: {}".format(curr.data))
                    curr = None


                elif parent.right is curr:
                    parent.right = None
                else:
                    parent.left = None




            # case 2: curr has only one child
            elif curr.right is None: # has a left child
                if parent is None: # match at root
                    curr = curr.left


                elif parent.right is curr:
                    parent.right = curr.left

                else:
                    parent.left = curr.left

            elif curr.left is None: #has a right child
                if parent is None: # match at root
                    curr = curr.right


                elif parent.right is curr:
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
                if ptr is prev.right:
                    prev.right = None
                else:
                    prev.left = None



    def insert(curr, data):

        if curr is None:
            curr = BSTNode(data, None, None)
            return curr

        elif curr.data == data: # node already in tree
            return curr

        elif data < curr.data:
            if curr.left is None:
                curr.left = BSTNode(data, None, None)
            else:
                return BSTNode.insert(curr.left, data)

        else: # data > curr.data
            if curr.right is None:
                curr.right = BSTNode(data, None, None)
            else:
                return BSTNode.insert(curr.right, data)


    def inorder(curr):
        if curr is None:
            return

        BSTNode.inorder(curr.left)
        print("{} ".format(curr.data), end=" ");
        BSTNode.inorder(curr.right)

root = None

root = BSTNode.insert(root, 25)
BSTNode.insert(root, 30)
BSTNode.insert(root, 15)
BSTNode.insert(root, 5)
BSTNode.insert(root, 20)
BSTNode.insert(root, 17)
BSTNode.insert(root, 20)

BSTNode.inorder(root)
print("\n")

# print(BSTNode.search(root, 17))
# print(BSTNode.search(root, 25))
# print(BSTNode.search(root, 5))
# print(BSTNode.search(root, 30))
# print(BSTNode.search(root, 15))
# print(BSTNode.search(root, 20))
#
# print(BSTNode.search(root, 28))
# print(BSTNode.search(root, 16))
# print(BSTNode.search(root, 2))
# print(BSTNode.search(root, 6))
# print(BSTNode.search(root, 29))
# print(BSTNode.search(root, 55))
# print(BSTNode.search(root, 18))
# print("\n")


BSTNode.delete(None, root, 25)
BSTNode.inorder(root)
print("\n")

BSTNode.delete(None, root, 60)
BSTNode.inorder(root)
print("\n")

BSTNode.delete(None, root, 20)
BSTNode.inorder(root)
print("\n")

BSTNode.delete(None, root, 15)
BSTNode.inorder(root)
print("\n")

BSTNode.delete(None, root, 20)
BSTNode.inorder(root)
print("\n")

BSTNode.delete(None, root, 5)
BSTNode.inorder(root)
print("\n")

BSTNode.delete(None, root, 17)
BSTNode.inorder(root)
print("\n")

BSTNode.delete(None, root, 30)
BSTNode.inorder(root)
print("\n")
