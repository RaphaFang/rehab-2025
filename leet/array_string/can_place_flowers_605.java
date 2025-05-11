class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        int i = 0;
        while (i < flowerbed.length) {
            if (flowerbed[i] == 0 &&
                    (i == 0 || flowerbed[i - 1] == 0) &&
                    (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                i += 2;
                count += 1;
            } else {
                i += 1;
            }
        }
        return count >= n;

    }
}

// int[] flowerbed
// 這類的 primitive 才能用

// get(int) 是 java.util.List 介面的成員方法，
// 只有 ArrayList<Integer>、LinkedList<Integer>