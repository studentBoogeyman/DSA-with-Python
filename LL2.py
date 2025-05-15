##Deep Dive in linked list
class Node:
    def __init__(self, value, next):
        self.vlaue = value #Refrences the users input
        self.next = next #refrence to next node


'''Major problem with the singly linked list is that it only links forward and not backkward so you cannot excatly come back so we are taking curr and curr.
next both conditions true.'''


# Function to remove duplicates from unsorted linked list.
def removeDuplicates(self, head):
    s = set()    # To keep track of elements we have already seen
    curr = head  # Initializing the pointer to start from the head
    s.add(curr.data)  # Adding the first element, as it can't be a duplicate yet
    
    # Using curr and curr.next to ensure we don't get AttributeError at the end 
    ## Atributer error is caused because we trying to access thing that is not defined
    while curr and curr.next:
        if curr.next.data not in s: 
            s.add(curr.next.data)  # If the value is new, add it to the set
            curr = curr.next       # Move the pointer forward
        else:
            curr.next = curr.next.next  # Skip the duplicate node by updating the link
    
    return head #we return head as it isnt changed and it points to the changed linked list and it is not the whole list

#To delete an node
def deleteNode(head, x):
    # Code here
    if x == 1:                #Special condition where we can just change the head to the next element 
        return head.next
        
    count = 1
    curr = head #initialising
    
    while curr and curr.next:
        if count == x-1:       #if we just put count == x we will be on the element that we want to delet and as the list is singly linked list it is not possible
            curr.next = curr.next.next # creating new link 
            break # because only one element is to be deleted
        count += 1 #genral count increment 
        curr = curr.next #shifting the pointer ahed 
    return head

# Function to delete a node in the middle of a singly linked list.
def deleteNode(self, node):
    #code here
    node.data = node.next.data #it will delet the exitsing node and replace its data with the nextnodes data
    node.next = node.next.next #this will basically delet the next node whose data is coppied without it data appers twice

#Function to find weter a linked list is circular or not
def isCircular(self, head):
        # Code here
        if head is None: #just in case there is an empty list we can directly apply this 
            return False #many questions consider this case True but the question i solved mentioned it to be false
        
        curr = head.next       #as the 
        while curr is not None and curr != head: #idea is if curr.next is heaad we know we looped
            curr = curr.next   
        return curr == head # Normal boolen comparison

#

        