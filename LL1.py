#Linked List

## Sinleli linked list
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
head = Node(1)
A = Node(9)
B = Node(3)
c = Node(5)

head.next = A
A.next = B
B.next = c

print(head)

## Traversing the List : O(n)
curr = head
while curr:
    print(curr)
    curr = curr.next
print( )

## Display Linked list
def displayList(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))

displayList(head)

## Searching for element in linked list
def search(head, x):
    curr = head
    while curr:
        if curr.val == x:
            return True
        curr = curr.next
    return False

print(search(head, 3))
print(search(head, 52))

##Doubali linked list
class doubliNode:
    def __init__(self, val,next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)

head2 = tail2 = doubliNode(3)

#To display
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

display(head2)
#Insert at the begening
def insert_at_begening(head, tail, x):
    new_node = doubliNode(x, next = head, prev = None)
    head.prev = new_node
    return new_node, tail

head2, tail2 = insert_at_begening(head2, tail2, 3)
display(head2)

#Insert at the end
def insert_at_end(head, tail, x):
    new_node = doubliNode(x, prev = tail)
    tail.next = new_node
    return new_node, new_node
head2, tail2 = insert_at_end(head2, tail2, 1)
display(head2)
