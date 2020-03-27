from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):

        # self.current = 0
        # if self.storage.length == self.capacity:
            
        #     if self.current == 0:
        #         self.current = self.capacity
        #     node = self.storage.head

        #     for x in range(1,self.current):
        #         node = node.next

        #     node.value = item
        #     self.current -=1
        # else:

            if self.storage.length == self.capacity:
                #current oldest is the first one
                node_to_change = self.storage.head

                #reset the current once eveythings been changed
                if self.current ==5:
                    self.current = 0

                for x in range(0,self.current):
                    node_to_change = node_to_change.next
                
                node_to_change.value = item
                self.current += 1

            else:
                self.storage.add_to_tail(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        first = self.storage.head

        while first:
            list_buffer_contents.append(first.value)
            first = first.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
