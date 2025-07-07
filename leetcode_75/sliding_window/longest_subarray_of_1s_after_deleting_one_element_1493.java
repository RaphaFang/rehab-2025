class Solution {
    public int longestSubarray(int[] nums) {
        int left = 0, right = 0, r = 0;
        int zero_count = 0;

        while (right < nums.length) {
            if (nums[right] == 0) {
                zero_count++;
            }
            while (zero_count > 1) {
                if (nums[left] == 0) {
                    zero_count--;
                }
                left++;
            }
            r = Math.max(right - left, r);
            right++;
        }
        return r;
    }
}