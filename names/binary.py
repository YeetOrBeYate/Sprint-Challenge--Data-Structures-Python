class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value:
            if self.left == None:
                node = BinarySearchTree(value)
                self.left = node
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right == None:
                node = BinarySearchTree(value)
                self.right = node
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # if right is there
        elif self.right:
            return self.right.contains(target)
        # if left is there
        elif self.left:
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):

        node = self.right
        if node:
            return node.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        cb(self.value)
        
        # if right is present
        if self.left:
             self.left.for_each(cb)
            
        # if left is present
        if self.right:
             self.right.for_each(cb)
