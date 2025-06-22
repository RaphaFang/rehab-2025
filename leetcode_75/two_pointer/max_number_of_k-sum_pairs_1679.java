import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        int res = 0;

        for (int num : nums) {
            int complement = k - num;
            if (freq.getOrDefault(complement, 0) > 0) {
                freq.put(complement, freq.get(complement) - 1);
                res++;
            } else {
                freq.put(num, freq.getOrDefault(num, 0) + 1);
            }
        }
        return res;
    }
}