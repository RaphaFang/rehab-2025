import java.util.ArrayList;
import java.util.List;

class Solution {
    public int largestAltitude(int[] gain) {
        List<Integer> temp = new ArrayList<>();
        int start = 0;
        temp.add(0); // 只能這樣後面加入進去
        for (int h : gain) {
            temp.add(start + h);
            start += h;
        }
        // return Collections.max(temp); // ! 這作法：1ms(j8)
        return temp.stream().max(Integer::compare).orElseThrow(); // ! 這作法：2ms(j21)
    }
}

// ! 這作法不只用primitive，同時不用處理max()函數
// class Solution {
// public int largestAltitude(int[] gain) {
// int altitude = 0;
// int max = 0;
// for (int g : gain) {
// altitude += g;
// if (altitude > max) {
// max = altitude;
// }
// }
// return max;
// }
// }
