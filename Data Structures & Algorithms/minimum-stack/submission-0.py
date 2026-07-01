class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            curmin=self.stack[-1][1]
            self.stack.append((val,min(curmin,val)))
        

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
