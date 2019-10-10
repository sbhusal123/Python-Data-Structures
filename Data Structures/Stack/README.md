# Stack
* Last In First Out(LIFO) data structure.

**Operations:**
* **Push:** Inserting an item into stack.
* **Pop:** Takes out one item(removes) from stack.
* **Peek:** Get item on top of stack without removing it.
* **Clear:** Clears all the items from stack.

**Stack use case:**
* Track which command has been executed. Pop last command off command stack to undo it.

# Stack using Python List
* Use append() to push an item onto the stack.
* Use pop() to remove an item.

## 1. Pushing item into stack
```python
my_stack = []
my_stack.append(0)
my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
print(my_stack)
```
**Output:** ``[0, 1, 2, 3]`` 

## 2. Pop item from stack
```python
my_stack.pop()
print(my_stack)
``` 
**Output:** ``[0, 1, 2]``. Item inserted at last i.e 3 is removed

## 3. Stack Implementation Using Class

```python
class Stack:
    def __init__(self):
        self.stack = list()


    def push(self,item):
        self.stack.append(item)


    def pop(self):
        if len(self.stack) > 0:
           return self.stack.pop()
        else:
            print("Stack underflow")
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)
        
  
```




