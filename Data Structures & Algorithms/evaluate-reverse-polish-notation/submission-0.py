class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+": 0, "-": 1, "*": 2, "/": 3}

        def operate(x, y, key):
            if key == 0:
                return x+y 
            elif key == 1:
                return x-y
            elif key == 2:
                return x*y
            elif key == 3:
                return int(x/y)

        stack=[]

        for t in tokens:
            if t in operators:
                y = stack.pop()
                x = stack.pop()
                z = operate(x, y, operators[t])
                stack.append(z)

            else:
                stack.append(int(t))

        return stack[-1]