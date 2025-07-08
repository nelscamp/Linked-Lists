class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None
            self.prev = None
            

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        new_node = self.__Node(val)
        if self.__size == 0:
            new_node.next = self.__trailer
            new_node.prev = self.__header
            self.__header.next = new_node
            self.__trailer.prev = new_node
        else:
            new_node.next = self.__trailer
            new_node.prev = self.__trailer.prev
            self.__trailer.prev.next = new_node
            self.__trailer.prev = new_node
        self.__size = self.__size+1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        new_node = self.__Node(val)
        if index < 0 or index >= self.__size:
            raise IndexError
        elif index == 0:
            new_node.next = self.__header.next
            new_node.prev = self.__header
            self.__header.next.prev = new_node
            self.__header.next = new_node
        else:
            current = self.__header.next
            for i in range (1, index):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
        self.__size = self.__size+1


    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index < 0 or index >= self.__size:
            raise IndexError
        elif self.__size == 0:
            raise IndexError
        elif self.__size == 1:
            removed_value = self.__header.next
            self.__header.next = self.__trailer
            self.__trailer.prev = self.__header
            self.__size = self.__size-1
            return removed_value.val
        elif index == 0:
            removed_value = self.__header.next
            self.__header.next = self.__header.next.next
            self.__header.next.prev = self.__header
            self.__size = self.__size-1
            return removed_value.val
        else:
            current = self.__header.next
            for i in range (1, index):
                current = current.next
            removed_value = current.next
            current.next = current.next.next
            current.next.prev = current
            self.__size = self.__size-1
            return removed_value.val
        
            

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index < 0 or index >= self.__size:
            raise IndexError
        elif self.__size == 0:
            raise IndexError
        else:
            current = self.__header.next
            for i in range(0, index):
                current = current.next
            return current.val
        

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__size == 0:
            return
        else:
            head_ref = self.get_element_at(0)
            self.append_element(head_ref)
            self.remove_element_at(0)
            return


    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        #if self.__header is None:
        #    return '[ ]'
        #else:
        if self.__size == 0:
            return '[ ]'
        else:
            list = []
            current = self.__header.next
            while current.next:
                list.append(str(current.val))
                current = current.next
            return '[ ' + (', '.join(list)) + ' ]'
        

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__iter_index = self.__header.next
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__iter_index.next is None:
            raise StopIteration
        to_return = self.__iter_index.val
        self.__iter_index = self.__iter_index.next
        return to_return

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        reversed = Linked_List()
        current = self.__trailer.prev
        for item in self:
            reversed.append_element(current.val)
            current = current.prev
        return reversed


if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    LL = Linked_List()
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    #Testing append_element
    print('!! Testing append_element !!')
    LL.append_element(-2)
    LL.append_element(-1)
    LL.append_element(0)
    LL.append_element(1)
    LL.append_element(2)
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    #Testing insert_element_at
    print('!! Testing insert_element_at !!')
    try:
        LL.insert_element_at(30, len(LL)) #last index, should fail because cannot insert at tail
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        LL.insert_element_at(10, -1) #not in bounds, should fail
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        LL.insert_element_at(10, 0) #at first index, should pass
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        LL.insert_element_at(20, 1) #insert at index 1, should pass
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    #Testing remove_element_at
    print('!! Testing remove_element_at !!')
    try:
        LL.remove_element_at(7) #out of bounds, should fail
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        LL.remove_element_at(len(LL)-1) #last index, should pass
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        LL.remove_element_at(0) #first index, should pass
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        LL.remove_element_at(-1) #invalid index, should fail
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        LL.remove_element_at(2) #valid index, should pass
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    #Testing get_element_at
    print('!! Testing get_element_at !!')
    try:
        element = LL.get_element_at(-1) #out of bounds, should fail
        print(element)
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        element = LL.get_element_at(0) #first index, should pass
        print(element)
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        element = LL.get_element_at(1) #within range, should pass
        print(element)
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        element = LL.get_element_at(len(LL)-1) #last index, should pass
        print(element)
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    try:
        element = LL.get_element_at(5) #out of bounds, should fail
        print(element)
        print('passed test')
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()

    #Testing reverse
    print('!! Testing Reversed !!')
    print(reversed(LL))
    print()

    #Testing iterator
    print('!! Testing Iterator !!')
    for val in LL:
        print(val)
    print()


    print('!! Testing Iterator Reversed !!')
    for rev_val in reversed(LL):
        print(rev_val)
    print()

    #Testing remove again lol
    print('!! Testing Remove_element !!')
    try:
        print(LL)
        LL.remove_element_at(3) #Remove all remaining elements
        print(LL)
        LL.remove_element_at(2)
        print(LL)
        LL.remove_element_at(1)
        print(LL)
        LL.remove_element_at(0)
        print(LL)
        LL.remove_element_at(0)  #this one should fail bc its already empty
    except IndexError:
        print('Invalid Index')
    print(LL)
    print('linked list has ' + str(len(LL)) + ' nodes')
    print()