class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            # self.mins.append(min(val, self.mins[-1]))
            # while the above line is interpretable and precise, there is more overhead
            # when calling min() or max() because the interpreter must first look up the function
            # then push it onto the call stack and execute then pop from call stack -- slower than if
            # statement comparison
            if val < self.mins[-1]:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]