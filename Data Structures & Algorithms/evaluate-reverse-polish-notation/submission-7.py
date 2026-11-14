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
                
                div_res = 0
                if a == 0:
                    div_res = 0
                elif (a > 0 and b > 0) or (a < 0 and b < 0):
                    div_res = b//a
                else:
                    div_res = -(-b//a)
                op_stack.append(div_res)
            else:
                op_stack.append(int(s))               

        return op_stack[-1]        