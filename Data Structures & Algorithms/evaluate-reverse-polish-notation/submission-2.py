class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper={'+','-','*','/'}
        stack = []
        for token in tokens:
            if token in oper:
                ans = 0
                op2 = stack.pop()
                op1 = stack.pop()
                if token == "+":
                    ans = op1+op2
                if token == "-":
                    ans = op1-op2
                if token == "*":
                    ans = op1*op2
                if token == "/":
                    ans = int(op1 / op2)
                stack.append(ans)
            else:    
                stack.append(int(token))
        return stack[-1]
        

