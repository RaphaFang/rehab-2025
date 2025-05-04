// class Positive {
//     public static int sum(int[] arr) {
//         int rn = 0;
//         for (int s : arr) {
//             if (s > 0) {
//                 rn += s;
//             }
//         }
//         return rn;
//     }
// }

class Positive {
    public static int sum(int[] arr) {
        int sum = 0;
        for (int num : arr)
            sum += num > 0 ? num : 0;
        return sum;
    }
}
// 兩者速度沒有差多少