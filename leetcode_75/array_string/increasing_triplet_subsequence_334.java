class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE;
        int sec = Integer.MAX_VALUE;
        for (int i : nums) {
            if (i < first) {
                first = i;
            } else if (i < sec) {
                sec = i;
            } else {
                return true;
            }
        }
        return false;
    }
}