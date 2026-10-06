class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack == [] or self.minstack[-1] > val:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])
         

    def pop(self) -> None:
        if not self.stack:
            return
        else:
            self.stack.pop()
            self.minstack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
