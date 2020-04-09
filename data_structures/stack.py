class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def is_empty(self):
        return (self.top == 0)
            
    def push(self, x):
        if self.top < len(self.stack):
            self.stack[self.top] = x
        else: 
            self.stack.append(x)
        self.top += 1
  
    def pop(self):
        if self.is_empty():
            print("[!] Underflow")
        else:
            self.top -= 1
            return self.stack.pop(self.top)

    def __str__(self):
        return f"{self.stack}"

def main():
    stack = Stack()
    stack.push(8)
    stack.push(7)
    stack.push(6)
    stack.pop()
    stack.push(5)

    print(stack)

if __name__ == "__main__":
    main()
