# Author: Jin Huang
# Description: Implement a BST class


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

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
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

    def dequeue(self) -> object:
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
    Binary Search Tree Node class
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Takes a BST and value.
        Adds the value to the tree. Duplicates are placed in the right subtree.
        """
        newNode = TreeNode(value)

        # empty BST
        if self.root is None:
            self.root = newNode
            return

        traversePointer = self.root

        pointerPosition = None              # the position to insert node

        # traverse until leaf
        while traversePointer is not None:
            pointerPosition = traversePointer
            if value < traversePointer.value:               # go down left
                traversePointer = traversePointer.left
            else:                                           # go down right
                traversePointer = traversePointer.right

        # if empty subtree
        if pointerPosition is None:
            pointerPosition = newNode
            self.root = pointerPosition

        # nonempty subtree, compare to leaf
        elif value < pointerPosition.value:
            pointerPosition.left = newNode

        else:
            pointerPosition.right = newNode


        return



    def contains(self, value: object) -> bool:
        """
        Takes a BST and value.
        If the value is in the BST:
            returns True
        Otherwise (including empty BST):
            returns False
        """
        if self.root is None:
            return False

        traversePointer = self.root

        while traversePointer is not None:
            if value == traversePointer.value:
                return True
            elif value < traversePointer.value:
                traversePointer = traversePointer.left
            else:
                traversePointer = traversePointer.right
        return False


    def get_first(self) -> object:
        """
        Takes a BST and returns the value stored at the root node.
        If empty BST:
            Returns None
        """
        if self.root is None:
            return None
        else:
            return self.root.value


    def remove_first(self) -> bool:
        """
        Takes a BST and removes the root node in the BST.
        If empty BST, returns False.
        If successful removal, returns True.
        """
        root = self.root

        if root is None:
            return False

        if root.left is not None and root.right is not None:
            rightSubRoot = root.right
            leftSubRoot = root.left

            # find the leftmost child of right subtree
            leftMost = rightSubRoot
            if leftMost.left is None:
                self.root = leftMost
                leftMost.left = leftSubRoot
                return True

            while leftMost.left.left is not None:
                leftMost = leftMost.left
            leftMostParent = leftMost
            leftMost = leftMostParent.left

            if leftMost.right is None:
                self.root = leftMost
                self.root.left = leftSubRoot
                self.root.right = rightSubRoot
                leftMostParent.left = None
                return True

            elif leftMost.right is not None:
                temp = leftMost.right
                self.root = leftMost
                self.root.left = leftSubRoot
                self.root.right = rightSubRoot
                leftMostParent.left = temp
                return True

        #
        elif root.left is not None:
            subRoot = root.left
            self.root = subRoot
            return True
        #
        elif root.right is not None:
            subRoot = root.right
            self.root = subRoot
            return True

        else:
            self.root = None
            return True


        return

    def remove(self, value) -> bool:
        """
        Takes a BST and a value. Removes the first instance of the value
        in the BST.
        Returns True if successful removal. Returns False, otherwise.
        """
        if self.root is None:
            return False

        if value == self.root.value:
            return self.remove_first()


        traversePointer = self.root
        parentNode = None

        while traversePointer is not None:

            if value == traversePointer.value:
                break

            elif value < traversePointer.value:
                parentNode = traversePointer            # before go down a level, save parentNode
                traversePointer = traversePointer.left
            elif value > traversePointer.value:
                parentNode = traversePointer
                traversePointer = traversePointer.right

        # no such node
        if traversePointer is None:
            return False

        else:
            # leaf
            if traversePointer.left is None and traversePointer.right is None:
                if traversePointer.value >= parentNode.value:
                    parentNode.right = None
                else:
                    parentNode.left = None
                return True

            # only one subtree
            elif traversePointer.left is None or traversePointer.right is None:
                if traversePointer.right is None:
                    subRoot = traversePointer.left

                if traversePointer.left is None:
                    subRoot = traversePointer.right

                if traversePointer.value >= parentNode.value:
                    parentNode.right = subRoot

                else:
                    parentNode.left = subRoot

                return True

            # two subtrees, replace with the leftmost child of the right subtree
            traverseLeft = traversePointer.left
            traverseRight = traversePointer.right


            # find the leftmost child of the right subtree
            leftMost = traverseRight

            if traverseRight.left is None:
                if traversePointer.value >= parentNode.value:
                    parentNode.right = leftMost
                    leftMost.left = traverseLeft
                    return True
                else:
                    parentNode.left = leftMost
                    leftMost.left = traverseLeft
                    return True

            else:
                while leftMost.left.left is not None:
                    leftMost = leftMost.left
                leftMostParent = leftMost
                leftMost = leftMostParent.left

                if traversePointer.value >= parentNode.value:
                    if leftMost == traverseRight:
                        parentNode.right = leftMost
                        leftMost.left = traverseLeft
                        return True
                    else:
                        temp = leftMost.right
                        parentNode.right = leftMost
                        leftMost.left = traverseLeft
                        leftMost.right = traverseRight

                        leftMostParent.left = temp
                        return True

                if traversePointer.value < parentNode.value:
                    if leftMost == traverseRight:
                        parentNode.left = leftMost
                        leftMost.left = traverseLeft
                        return True
                    else:
                        temp = leftMost.right
                        parentNode.left = leftMost
                        leftMost.left = traverseLeft
                        leftMost.right = traverseRight

                        leftMostParent.left = temp
                        return True



        return




    def pre_order_traversal(self) -> Queue:
        """
        Takes a BST and performs  pre-order traversal of the tree.
        Returns a Queue that contains values of visited nodes, in the order they were visited.
        Returns an empty Queue if empty tree.
        """
        result = Queue()
        root = self.root

        # empty tree
        if root is None:
            return result

        # visit node>left>right
        def rec_pre_traverse(node):
            if node is not None:
                result.enqueue(node.value)
                rec_pre_traverse(node.left)
                rec_pre_traverse(node.right)

        rec_pre_traverse(root)
        return result


    def in_order_traversal(self) -> Queue:
        """
        Takes a BST and performs  in-order traversal of the tree.
        Returns a Queue that contains values of visited nodes, in the order they were visited.
        Returns an empty Queue if empty tree.
        """
        result = Queue()
        root = self.root

        # empty tree
        if root is None:
            return result

        # visit left > node > right
        def rec_in_traverse(node):
            if node is not None:
                rec_in_traverse(node.left)
                result.enqueue(node.value)
                rec_in_traverse(node.right)

        rec_in_traverse(root)
        return result


    def post_order_traversal(self) -> Queue:
        """
        Takes a BST and performs  post-order traversal of the tree.
        Returns a Queue that contains values of visited nodes, in the order they were visited.
        Returns an empty Queue if empty tree.
        """
        result = Queue()
        root = self.root

        # empty tree
        if root is None:
            return result

        # visit left > right > node
        def rec_post_traverse(node):
            if node:
                rec_post_traverse(node.left)
                rec_post_traverse(node.right)
                result.enqueue(node.value)

        rec_post_traverse(root)
        return result


    def by_level_traversal(self) -> Queue:
        """
        Takes a BST and performs  level-order traversal of the tree.
        Returns a Queue that contains values of visited nodes, in the order they were visited.
        Returns an empty Queue if empty tree.
        """
        layer = Queue()
        layerNodesCount = 0

        result = Queue()
        root = self.root

        if root is None:
            return result

        # first layer contains root
        layer.enqueue(root)
        layerNodesCount += 1

        # for each layer,
        # dequeue root node from this layer >
        # enqueue root node to result >
        # enqueue this root node's left child to this layer >
        # enqueue this root node's right child to this layer
        while layerNodesCount > 0:

            # traverse the nodes in each layer
            for i in range(layerNodesCount):

                # pop the first-in node
                node = layer.dequeue()
                layerNodesCount -= 1

                # add this root node to result
                result.enqueue(node.value)

                # next: search nodes in the next layer
                # first: search left
                if node.left is not None:

                    # if left child exists, add to this level
                    layer.enqueue(node.left)
                    layerNodesCount += 1

                # next: search right
                if node.right is not None:

                    # if right child exists, add to this level
                    layer.enqueue(node.right)
                    layerNodesCount += 1

        return result



    def is_full(self) -> bool:
        """
        Takes a BST and returns True if the tree is a full binary tree.
        Empty tree and single-root tree is full.
        """
        root = self.root

        # Empty tree is full
        if root is None:
            return True


        def rec_is_full(node):
            """
            Helper function that recursively checks if subtrees are full.
            Visit left child > right child.
            Full if: both None or both exist.
            """
            # Base: root node is None: True
            if node is None:
                return True

            # Base: leaf node > True
            if node.left is None and node.right is None:
                return True

            # Base: one child > False
            if node.left is None and node.right is not None or node.left is not None and node.right is None:
                return False

            # Both left and right nodes exist > recursively check the rest
            if node.left is not None and node.right is not None:
                return rec_is_full(node.left) and rec_is_full(node.right)


        return rec_is_full(root)


    def is_complete(self) -> bool:
        """
        Takes a BST and returns True if the tree is a complete binary tree.
        Empty tree and single-root tree are complete.
        """
        root = self.root

        # empty tree and single-root tree
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        layer = Queue()
        layer.enqueue(root)
        layerNodesCount = 1

        prevNode = root

        # Do a level-order traversal
        # Not a complete tree: a non-empty node follows an empty tree
        while layerNodesCount > 0:

            # traverse the nodes in each layer
            for i in range(layerNodesCount):

                node = layer.dequeue()
                layerNodesCount -= 1

                # non-empty current node
                if node is not None:

                    # if a non-empty node follows an empty node
                    # not a complete BST
                    if prevNode is None:
                        return False

                    # Only append children if non-empty node
                    # Enqueue each node's left and right child
                    # If a child is missing, then the child node should be None
                    else:
                        layer.enqueue(node.left)
                        layerNodesCount += 1

                        layer.enqueue(node.right)
                        layerNodesCount += 1

                # Whether empty or non-empty,
                # update prevNode
                prevNode = node

        return True



    def is_perfect(self) -> bool:
        """
        Takes a BST and returns True if the tree is a perfect binary tree.
        Empty tree and single-root tree are perfect.
        """
        root = self.root
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        # Finds the depth of leftmost leaf
        def findDepth(node):
            """
            Takes a node and returns the depth of that node
            """
            depth = 0

            while node is not None:
                node = node.left
                if node is not None:
                    depth += 1
            return depth

        def rec_is_perfect(node, level):
            """
            Takes a node, depth and level.
            Recursively checks if a tree is perfect.
            """

            if node is None:
                return True

            # if reaches leaf node,
            # for a perfect binary tree
            # this leaf node's level + 1 must be the same as
            # the global variable depth
            if node.left is None and node.right is None:
                if depth == level:
                    return True
                else:
                    return False

            # if reaches here, then this node is not a leaf node,
            # i.e. this is an internal node
            # False if this internal node has only one child
            if node.left is None or node.right is None:
                return False

            # recursively checks left and right subtrees, go down a level
            return rec_is_perfect(node.left, level+1) and rec_is_perfect(node.right, level + 1)

        depth = findDepth(root)
        return rec_is_perfect(root, 0)



    def size(self) -> int:
        """
        Takes a BST and returns the total number of nodes in the tree.
        """
        root = self.root

        def rec_size(node):
            if node is None:
                return 0


            return 1 + rec_size(node.left) + rec_size(node.right)

        return rec_size(root)


    def height(self) -> int:
        """
        Takes a BST and returns the height of the tree.
        Returns -1 if empty tree. Returns 0 if single root node.
        """
        root = self.root

        if root is None:
            return -1

        if root.left is None and root.right is None:
            return 0

        # Recursion: process for each node
        # visit left, calcualte height of left subtree >
        # visit right, calculate height of right subtree>
        # compare left height to right height
        def rec_height(node):
            """
            Takes a node and recursively finds the max depth
            """
            if node is None:
                return 0

            # finds height of left subtree
            leftHeight = rec_height(node.left)

            # finds height of right subtree
            rightHeight = rec_height(node.right)

            # max height + the node itself
            if leftHeight >= rightHeight:
                if node == root:
                    return leftHeight
                else:
                    return leftHeight + 1
            else:
                if node == root:
                    return rightHeight
                else:
                    return rightHeight + 1


        return rec_height(root)



    def count_leaves(self) -> int:
        """
        Takes a Binary Search Tree and returns the number of leaf nodes.
        Return 0 if empty tree.
        """
        root = self.root

        # empty tree
        if root is None:
            return 0

        def rec_leaves(node):
            """
            Recursively counts the leaf nodes of left and right subtrees.
            """
            if node is None:
                return 0

            # encounters a leaf
            if node.left is None and node.right is None:
                return 1

            # recursively traverses left and right subtree
            return rec_leaves(node.left) + rec_leaves(node.right)

        return rec_leaves(root)


    def count_unique(self) -> int:
        """
        Takes a binary search tree and counts the number of unique values stored in the tree.
        """
        root = self.root

        if root is None:
            return 0

        stack = Stack()

        def inorderTraverse(node, stack):
            """
            Takes a node and stack,
            recursively in-order traverses the tree,
            pushes unique nodes to stack.
            """
            if node is not None:
                # visit left
                inorderTraverse(node.left, stack)

                # visit central
                if stack.is_empty():
                    stack.push(node)
                else:
                    stackTop = stack.top()
                    if stackTop.value != node.value:
                        stack.push(node)

                # visit right
                inorderTraverse(node.right, stack)


        inorderTraverse(root, stack)

        # count the nodes in stack
        count = 0
        while stack.is_empty() is False:
            stack.pop()
            count += 1
        return count
