#Linked List
#DeletionAtBeginning
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class singleLinkedList:
    def __init__ (self):
        self.head=None
    def delete_At_Beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def display(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,end="-->")
                temp=temp.next

l= singleLinkedList()
n = Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
l.display()
print()
l.delete_At_Beginning()
print()
l.display()

