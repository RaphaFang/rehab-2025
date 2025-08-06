class Solution {
    public int removeDuplicates(int[] nums) {
        var k = 1;
        if (nums.length < 2) {
            return k;
        }
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
}