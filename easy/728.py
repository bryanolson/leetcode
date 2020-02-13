class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:            
        result = []        
        remove = []
        for num in range(left,right+1):
          bool_arr = []
          divisors = []  
          for _ in str(num):
            if int(_) not in divisors and int(_) != 0:    
              divisors.append(int(_))
              print(num, divisors)
          for divisor in divisors:
            if num % divisor == 0:
              bool_arr.append(True)
            else:
              bool_arr.append(False)
          if False in bool_arr:
            continue
          else:
            result.append(num)

        for num in result:
          for _ in str(num):
            if int(_) == 0:
              remove.append(num)

        for num in remove:
          if num in result:
            result.remove(num)
            
        return(result)
