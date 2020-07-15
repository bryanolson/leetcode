class Solution {
    public int[] runningSum(int[] nums) {
        int numlen = nums.length;
        int[] numSums = new int[numlen];
        int[] finSum = new int[numlen];
        for (int i=0;i<numlen;i++) {
            numSums[i] = nums[i];
            Solution tempSolution = new Solution();
            finSum[i] = tempSolution.calcSum(numSums);
        }
        return finSum;
    }
    public int calcSum(int[] findSum) {
        int len = findSum.length;
        int calcdSum = 0;
        for (int i=0;i<len;i++) {
            calcdSum += findSum[i];
        }
        return calcdSum;
    }
}
