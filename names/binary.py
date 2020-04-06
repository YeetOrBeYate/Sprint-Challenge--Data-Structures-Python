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
    # def contains(self, target):
    #     if self.value == target:
    #         return True
    #     # if right is there
    #     elif self.left:
    #         return self.left.contains(target)
    #     # if left is there
    #     elif self.right:
    #         return self.right.contains(target)
    #     else:
    #         return False

    ## not sure why the above code doesnt work, but this was my first pass solution the other day and it works for some reason. Dont care I got mvp

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value: 
            if not self.right:
                return False 
            else:
                return self.right.contains(target)




