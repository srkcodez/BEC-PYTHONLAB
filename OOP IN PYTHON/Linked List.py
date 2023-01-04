class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def insertbegin(self, node):
        node.next = self.head.next
        self.head = node
        print(node.data, 'inserted successfully in the beginning')

    def insertpos(self, node, pos):
        temp = prev = self.head
        for i in range(1, pos):
            prev = temp
            temp = temp.next
        node.next = temp.next
        prev.next = node
        print(node.data, 'inserted successfully at %d posistion' % pos)

    def insertend(self, node):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        print(node.data, 'inserted successfully at the end')

    def display(self):
        temp = self.head
        if temp.next is None:
            print('List is empty')
        else:
            print()
            print(temp.data,'-->')
            while temp.next is not None:
                print(temp.data, "-->", end='')
                temp = temp.next
            print(temp.data)

n1=Node(20)
l1 = LinkedList(n1)
l1.display()
''' l1.insertbegin(Node(10))
l1.display()
l1.insertend(Node(30))
l1.display()
l1.insertpos(Node(40), 1)
l1.display()
'''