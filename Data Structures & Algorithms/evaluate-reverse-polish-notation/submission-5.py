class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(i)
            else:
                r2 = int(stack.pop())
                r1 = int(stack.pop())
                if i == "+":
                    stack.append(str(r1 + r2))
                if i == "*":
                    stack.append(str(r1 * r2))
                if i == "-":
                    stack.append(str(r1-r2))
                if i == "/":
                    stack.append(str(int(r1/r2)))

        return int(stack[0])