class Stack:

    def __init__(self, arr: list, size):
        self.arr = arr
        self.size = size

    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return len(self.arr) == self.size
    
    def push(self, value):
        if not self.is_full():
            self.arr.append(value)
        else:
            print("Stack is full")
    def pop(self):
        print(self.arr)
        if not self.is_empty():
            return self.arr.pop()


stack = Stack([], 10)
stack.push(1);  
stack.push(2);  
stack.push(3);  
stack.push(4);  
print(stack.pop())