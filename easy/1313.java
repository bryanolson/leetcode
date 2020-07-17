class Solution {
    public int[] decompressRLElist(int[] nums) {
        ArrayList<Integer> solution = new ArrayList<Integer>();
        for (int i=0;i<(nums.length-1);i++) {
            if (i%2==0 || i==0) {
                int freq = nums[i];
                int val = nums[i+1];
                while (freq > 0) {
                    solution.add(val);
                    freq--;
                }
            }
        }
        int[] arrSolution = new int[solution.size()];
        for (int j=0; j<solution.size();j++) {
            arrSolution[j] = solution.get(j);
        }
        return arrSolution;
    }
}
