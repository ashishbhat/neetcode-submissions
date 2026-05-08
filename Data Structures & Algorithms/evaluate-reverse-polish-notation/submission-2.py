class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','/','*']
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                operator = token
                second = int(stack.pop())
                first = int(stack.pop())
                if operator == '+':
                    stack.append(first + second)
                elif operator == '-':
                    stack.append(first - second)
                elif operator == '*':
                    stack.append(first*second)
                else:
                    stack.append(first/second)
        return int(stack.pop())



            
