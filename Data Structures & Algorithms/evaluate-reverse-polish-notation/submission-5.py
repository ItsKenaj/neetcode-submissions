class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                a = numStack.pop()
                b = numStack.pop()
                numStack.append(a + b)
            elif tokens[i] == '-':
                a = numStack.pop()
                b = numStack.pop()
                numStack.append(b - a) 
            elif tokens[i] == '*':
                a = numStack.pop()
                b = numStack.pop()
                numStack.append(a * b)
            elif tokens[i] == '/':
                a = numStack.pop()
                b = numStack.pop()
                numStack.append(int(b / a))
            else:
                numStack.append(int(tokens[i]))

        if len(numStack) == 1:
            return numStack[0]
        