
class FIFO:
    def __init__(self,max):
        self.queue=list()
        self.max=max
        self.front=0
        self.rear=-1

    def insert(self,v):
        if(self.rear<=self.max):
            self.rear+=1
            self.queue.insert(self.rear,v)
        else:
            print("queue is full")

    def disp(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=' ')
q1=FIFO(10)


q1.insert(10)
q1.insert(20)
q1.disp()

