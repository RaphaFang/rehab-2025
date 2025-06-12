import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int tribonacci(int n) {
        List<Integer> ll = new ArrayList<>(Collections.nCopies(n + 3, 0));
        ll.set(1, 1);
        ll.set(2, 1);
        for (int i = 3; i <= n; i++) {
            int sum = ll.get(i - 1) + ll.get(i - 2) + ll.get(i - 3);
            ll.set(i, sum);
        }
        return ll.get(n);
    }
}
