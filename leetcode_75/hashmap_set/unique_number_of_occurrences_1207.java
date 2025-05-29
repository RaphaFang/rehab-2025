import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public boolean uniqueOccurrences(int[] arr) {

        Map<Integer, Integer> tempMap = new HashMap<>();
        Set<Integer> tempSet = new HashSet<>();

        for (int i : arr) {
            tempMap.put(i, tempMap.getOrDefault(i, 0) + 1);
        }
        for (int v : tempMap.values()) {
            if (tempSet.contains(v)) {
                return false;
            }
            tempSet.add(v);
        }
        return true;
    }
}

// keypoint
// Map, Set
// getOrDefault(), contains()

// map 還有兩種可用
// map.containsKey("key");
// map.containsValue(5);