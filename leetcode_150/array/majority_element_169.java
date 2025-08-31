class Solution {
    public int majorityElement(int[] nums) {
        var holder = 0;
        var candidate = 0;
        for (int n : nums) {
            if (holder == 0) {
                candidate = n;
            }
            holder += (n == candidate ? 1 : -1);
        }
        return candidate;
    }
}