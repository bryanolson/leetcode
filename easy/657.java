class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;
        for (int i=0;i<moves.length();i++) {
            char move = moves.charAt(i);
            switch (move) {
                case 'U':
                    x += 1;
                    break;
                case 'D':
                    x -= 1;
                    break;
                case 'L':
                    y -= 1;
                    break;
                case 'R':
                    y += 1;
                    break;
            }
        }
        if (x ==0 && y==0) {
            return true;
        } else {
            return false;
        }
     }
}
