

class Queue:
    def __init__(self,max):
        self.q=list()
        self.max=max

    def enque(self,ele):
        if(len(self.q)>= self.max):
            print("queue is full no more element insertion")
        else:
            self.q.append(ele)
            print(f"{ele} inserted successfully")

    def deque(self):
        if(len(self.q)<=0):
            print("no element to delete in queue")
        else:
            ele=self.q.pop(0)
            print(f"{ele} deleted successfully")

    def display(self):
        if (len(self.q) <= 0):
            print("no element to delete in queue")
        else:
            for i in self.q:
                print(i,end=" ")



q1=Queue(5)

q1.display()
q1.enque(25)
q1.display()
q1.enque("dairy milk")
q1.display()
q1.enque(4.5)
q1.enque('a')
q1.enque('jail')
q1.enque('warden')
q1.display()