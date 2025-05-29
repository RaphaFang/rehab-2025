class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int temp = 0;
        for (int n = 0; n < k; n++) {
            temp += nums[n];
        }
        int max = temp;

        for (int i = k; i < nums.length; i++) {
            temp = temp - nums[i - k] + nums[i];
            max = Math.max(max, temp);
        }
        return (double) max / k;
    }
}

// 3ms
// (double) max， 要在這邊加上double，讓整體變成小數