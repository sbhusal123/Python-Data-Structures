class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self,x):
        self.queue.append(x)

    def dequeue(self):
        if len(self.queue) >0:
            x = self.queue[0]
            del self.queue[0]
            return x
        else:
            print("Queue is empty")
            return None

    def __str__(self):
        return str(self.queue)
