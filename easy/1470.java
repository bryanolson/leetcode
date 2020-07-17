class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] outputArray = new int[nums.length];
        int iter = 0;        
        for (int i=0; i<nums.length-1; i=i+2) {
            outputArray[i] = nums[iter];
            outputArray[i+1] = nums[iter+n];
            iter++;
        }        
        return outputArray;
    }
}
