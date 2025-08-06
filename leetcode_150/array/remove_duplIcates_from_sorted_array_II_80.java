class Solution {
    public int removeDuplicates(int[] nums) {
        var k = 1;
        var c = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                nums[k] = nums[i];
                c = 1;
                k++;
            } else if (nums[i] == nums[i - 1]) {
                if (c < 2) {
                    nums[k] = nums[i];
                    c++;
                    k++;
                }

            }
        }
        return k;
    }
}