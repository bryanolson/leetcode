class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []	
        operators = ['+','-','*','/']
        result = 0

        #Need a loop to go through every element in tokens
        for _ in tokens:
            if _ in operators:
                vara = int(stack.pop())
                varb = int(stack.pop())
                result = Solution.do_operation(vara,varb,_)
                stack.append(result)
            else:
                stack.append(_)
        return stack[0]

    @staticmethod
    def do_operation(vara, varb, operator):
        if operator == '+':
            return varb+vara
        if operator == '-':
            return varb-vara
        if operator == '*':
            return varb*vara
        if operator == '/':
            return int(varb/vara)

        
        
