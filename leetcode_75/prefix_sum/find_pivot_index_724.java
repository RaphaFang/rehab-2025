class find_pivot_index_724 {
    public int pivotIndex(int[] nums) {
        int right = 0;
        int left = 0;
        for (int i : nums) {
            right += i;
        }
        for (int i = 0; i < nums.length; i++) {
            left += (i != 0) ? nums[i - 1] : 0;
            right -= nums[i];
            if (left == right) {
                return i;
            }
        }
        return -1;
    }
}
// 1ms