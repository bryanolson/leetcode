class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for letter in moves:
            if letter == "R":
                x += 1
            elif letter == "L":
                x -= 1
            elif letter == "U":
                y += 1
            elif letter == "D":
                y -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False
