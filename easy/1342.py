class Solution:
    def numberOfSteps (self, num: int) -> int:
        num_steps = 0
        
        while num != 0:
            if num % 2 == 0:
                num = num/2
                num_steps += 1
            elif num % 2 != 0:
                num -= 1
                num_steps += 1
        
        return num_steps