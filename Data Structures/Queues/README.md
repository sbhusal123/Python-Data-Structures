# Queues
* First In First Out (FIFO) data structure.

## Use cases:
* Good for modelling anything you wait in line for.
* Ex. Bank Tellers, Placing an order, e.t.c.

## Operations
* **Enqueue:** Add an item to the end of line.
* **Dequque:** Remove an item from the front of line.

## Queue Implementation in Python

```python
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

```




