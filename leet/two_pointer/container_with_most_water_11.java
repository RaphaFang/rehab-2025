class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxAmount = 0;

        while (left < right) {
            int bottom = right - left;
            int tall = Math.min(height[left], height[right]);
            maxAmount = Math.max(maxAmount, bottom * tall);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxAmount;
    }
}