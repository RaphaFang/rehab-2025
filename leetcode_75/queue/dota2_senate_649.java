import java.util.*;

class Solution {
    public String predictPartyVictory(String senate) {
        int n = senate.length();
        var qD = new ArrayDeque<Integer>();
        var qR = new ArrayDeque<Integer>();

        for (int i = 0; i < n; i++) {
            if (senate.charAt(i) == 'D') {
                qD.addLast(i);
            } else {
                qR.addLast(i);
            }
        }

        while (!qD.isEmpty() && !qR.isEmpty()) {
            var d = qD.pollFirst();
            var r = qR.pollFirst();

            if (d < r) {
                qD.addLast(d + n);
            } else {
                qR.addLast(r + n);
            }
        }

        return qD.isEmpty() ? "Radiant" : "Dire";
    }
}
