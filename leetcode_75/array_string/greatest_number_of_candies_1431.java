import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> ll = new ArrayList<>(candies.length);
        int max = Arrays.stream(candies).max().orElseThrow();
        for (int i : candies) {
            if (i + extraCandies >= max) {
                ll.add(true);
            } else {
                ll.add(false);
            }
        }
        return ll;
    }
}

// 7kyu_high_and_low
// 可以參考