class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','/','*']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operator = token
                second = stack.pop()
                first = stack.pop()
                if operator == '+':
                    stack.append(first + second)
                elif operator == '-':
                    stack.append(first - second)
                elif operator == '*':
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
        return stack.pop()



            
