# Aurthor: Jin Huang
# Description: Implement the AVL class.


import random


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self):
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)


class AVL:
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL tree
        """
        self.root = None

        # populate AVL with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form using pre-order traversal
        """
        values = []
        self._str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        """
        if cur:
            values.append(str(cur.value))
            self._str_helper(cur.left, values)
            self._str_helper(cur.right, values)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.
        """
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            if node:
                # check for correct height (relative to children)
                l = node.left.height if node.left else -1
                r = node.right.height if node.right else -1
                if node.height != 1 + max(l, r):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                s.push(node.right)
                s.push(node.left)
        return True

    # -----------------------------------------------------------------------

    def contains(self, node, value):
        """
        Takes an AVL tree, node, and value,
        Recursively checks if the value is in the tree.
        Returns True if the tree contains the value;
        Otherwise, returns False
        """

        if node is None:
            return False

        if value < node.value:
            return self.contains(node.left, value)

        if value > node.value:
            return self.contains(node.right, value)

        return True

    def getHeight(self, node):
        """
        Takes a root node and recursively gets its height
        """
        if node is None:
            return 0
        else:
            if node.left:
                leftHeight = self.getHeight(node.left)
            else:
                leftHeight = 0
            if node.right:
                rightHeight = self.getHeight(node.right)
            else:
                rightHeight = 0

            if leftHeight >= rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1


    def balance(self, balanceFactor, node):
        """
        Takes an AVL, balanceFactor and node,
        balances the tree achored at the node
        """

        def rightRotation(node):
            """
            Right rotate anchored at the given node
            """
            newParent = node.left
            temp = newParent.right
            if node.parent is None:
                newParent.parent = None
                self.root = newParent
            elif node.parent is not None:
                newParent.parent = node.parent

            node.parent = newParent
            newParent.right = node
            node.left = temp
            if temp is not None:
                temp.parent = node

            node.height = self.updateHeights(node) - 1
            newParent.height = self.updateHeights(newParent) - 1

            return newParent


        def leftRotation(node):
            """
            Left rotate anchored at the given node
            """
            newParent = node.right
            temp = newParent.left
            if node.parent is None:
                newParent.parent = None
                self.root = newParent
            elif node.parent is not None:
                newParent.parent = node.parent

            node.parent = newParent
            newParent.left = node
            node.right = temp
            if temp is not None:
                temp.parent = node

            # update heights
            node.height = self.updateHeights(node) - 1
            newParent.height = self.updateHeights(newParent) - 1

            return newParent


            # left heavy tree
        if balanceFactor == 2:

            leftChildBF = self.balanceFactor(node.left)

            # left left: right rotate
            if leftChildBF >= 0:
                return rightRotation(node)

            # left right: first left rotate, then right rotate
            elif leftChildBF < 0:
                node.left = leftRotation(node.left)
                return rightRotation(node)


        # right heavy tree
        elif balanceFactor == -2:

            rightChildBF = self.balanceFactor(node.right)

            # right right: left rotate
            if rightChildBF <= 0:
                return leftRotation(node)

            # right left: first right rotate, then left rotate
            elif rightChildBF >= 0:
                node.right = rightRotation(node.right)
                return leftRotation(node)



        # no need to balance
        return node



    def balanceFactor(self, node):
        """
        Takes an AVL and node,
        returns the balanceFactor of the node
        """
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        balanceFactor = leftHeight - rightHeight
        return balanceFactor

    def updateHeights(self, node):
        """
        Takes an AVL and node,
        updates the new height of the node
        """

        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        nodeHeight = 0

        if leftHeight >= rightHeight:
            nodeHeight = 1 + leftHeight

        elif leftHeight < rightHeight:
            nodeHeight = 1 + rightHeight

        return nodeHeight

    def insert(self, root, value):
        """
        Takes an AVL, node, and value, inserts the value to the tree
        """
        # BST recursive insertion
        if root is None:                    # Base case
            newNode = TreeNode(value)
            root = newNode
            return newNode


        elif value < root.value:
            root.left = self.insert(root.left, value)

        elif value >= root.value:
            root.right = self.insert(root.right, value)

        #calls getHeight function and calculates balance factor of root
        root.height = self.updateHeights(root) - 1

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        balanceFactor = leftHeight - rightHeight

        if value < root.value:
            root.left.parent = root
        elif value > root.value:
            root.right.parent = root


        return self.balance(balanceFactor, root)



    def add(self, value: object) -> None:
        """
        Takes an AVL and a value, adds the value to the tree, maintaining AVL property.
        Duplicates are not allowed.
        Do nothing if the value is in the tree.
        """
        # call contains method to check if the value is in the tree
        if self.contains(self.root, value) is True:
            return
        else:
            if self.root is None:
                newNode = TreeNode(value)
                self.root = newNode
            else:
                return self.insert(self.root, value)

    def deletion(self, root, value):
        """
        Takes an AVL, node, and value, deletes the value from the tree.
        Returns True if the deletion is successful,
        returns False otherwise.
        """
        def findMin(root):
            """
            Takes a root and find the smallest (leftmost) value
            anchored at the root
            """
            while root.left is not None:
                root = root.left
            return root.value

        # BST recursive deletion
        if root is None:
            return root

        elif value < root.value:
            root.left = self.deletion(root.left, value)

        elif value > root.value:
            root.right = self.deletion(root.right, value)

        elif value == root.value:
            # only a right subtree or no subtree
            if root.left is None:
                if root.parent is None:
                    self.root = root.right
                else:
                    return root.right
            # only a left subtree or no subtree
            elif root.right is None:
                if root.parent is None:
                    self.root = root.left
                else:
                    return root.left
            # both subtrees exist
            else:
                successorValue = findMin(root.right)
                root.value = successorValue
                root.right = self.deletion(root.right, successorValue)

        # calls getHeight function and calculates balance factor of root
        root.height = self.updateHeights(root) - 1

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        balanceFactor = leftHeight - rightHeight

        return self.balance(balanceFactor, root)



    def remove(self, value: object) -> bool:
        """
        Takes an AVL and a value,
        removes the first instance of the value in the tree.
        Replace with in-order successor. If the deleted node only has one subtree,
        replace with the root node of that subtree.
        Returns True if the removal is sucessful,
        Returns False otherwise.
        """
        if value is None:
            return False

        # if the value is not in the tree
        if self.contains(self.root, value) is False:
            return False
        else:
            if value == self.root.value:
                if self.root.left is None and self.root.right is None:
                    self.root = None
                    return True
            self.deletion(self.root, value)
            return True