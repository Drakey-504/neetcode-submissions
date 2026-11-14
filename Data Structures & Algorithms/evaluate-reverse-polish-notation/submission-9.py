class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        op_stack = []
        
        for s in tokens:
            if s == "+":
                a = op_stack.pop()
                b = op_stack.pop()

                op_stack.append((b+a))

            elif s == "-":
                a = op_stack.pop()
                b = op_stack.pop()

                op_stack.append((b-a))
            elif s == "*":
                a = op_stack.pop()
                b = op_stack.pop()

                op_stack.append((b*a))
            elif s == "/":
                a = op_stack.pop()
                b = op_stack.pop()

                op_stack.append(int(float(b)/a))
            else:
                op_stack.append(int(s))               

        return op_stack[-1]        