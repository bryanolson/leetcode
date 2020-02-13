class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fblist = []
        for num in range(1,n+1):

            if num % 3 ==0 and num % 5 ==0:
                fblist.append("FizzBuzz")
            elif num%3==0:
                fblist.append("Fizz")
            elif num%5==0:
                fblist.append("Buzz")
            elif num % 3 != 0:
                fblist.append(str(num))
        return fblist
