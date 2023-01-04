class Queue:
    def __init__(self, max):
        self.q = list()
        self.max = max

    def enque (self, ele):
        if len(self.q) >= self.max:
            print("queue is full")
        else:
            self.q.append(ele)
            print("element inserted successful")

    def deque(self):
        if len(self.q) == 0:
            print(" no elements to delete")
        else:
            ele = self.q.pop(0)
            print(f"{ele} deleted successfully")

    def display(self):
        if len(self.q) == 0:
            print(" no elements to delete")
        else:
            for i in self.q:
                print(i, " ", end=' ')


q1 = Queue(5)

q1.enque(1)
q1.enque(2)
q1.deque()
q1.enque(3)
q1.enque(4)
q1.enque(5)
q1.enque(6)
q1.display()
