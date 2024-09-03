class MinStack:

    def __init__(self):
        self.stack1=[]
        self.min_stack=[ ]
        

    def push(self, val: int) -> None:
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack1.append(val)

    def pop(self) -> None:
        if self.stack1:
            if self.stack1[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack1.pop()

    def top(self) -> int:
        if self.stack1:
            return self.stack1[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()