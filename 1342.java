class Solution {
    public int numberOfSteps (int num) {
        int numSteps = 0;
        while (num !=0) {
            int switchNum = (num%2);
            switch (switchNum) {
                case 0:
                    num = (num/2);
                    numSteps += 1;
                    break;
                case 1:
                    num -= 1;
                    numSteps += 1;
                    break;
            }
        }
        return numSteps;
    }
}
