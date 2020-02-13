class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        final_morse = []
        unique_morse = []
        
        if len(words) == 0:
            return 0
        
        for word in words:
          temp_str = ''
          for _ in range(len(word)):
            temp_str += (morse[(ord(word[_]) - 97)])
          final_morse.append(temp_str)
        
        unique_morse.append(final_morse[0])

        for code in final_morse:
          if code not in unique_morse:
            unique_morse.append(code)

        return len(unique_morse)
