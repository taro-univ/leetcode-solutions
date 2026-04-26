class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
                
            elif t == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
                
            elif t == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
                
            elif t == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
                
            else:
                stack.append(int(t))

        return stack.pop()