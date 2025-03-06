class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def print_forward(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def print_backward(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

dll = DoublyLinkedList()
while True:
    print("\nDoubly Linked List Operations:")
    print("1. Insert at Head")
    print("2. Insert at Tail")
    print("3. Print Forward")
    print("4. Print Backward")
    print("5. Exit")
        
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter value to insert at head: "))
        dll.insert_head(data)
    elif choice == '2':
        data = int(input("Enter value to insert at tail: "))
        dll.insert_tail(data)
    elif choice == '3':
        print("Forward Traversal:")
        dll.print_forward()
    elif choice == '4':
        print("Backward Traversal:")
        dll.print_backward()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
