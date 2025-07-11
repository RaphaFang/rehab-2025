package leetcode_75.hashmap_set;

import java.util.*;

class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        int counter = 0;
        Map<List<Integer>, Integer> colMap = new HashMap<>();

        for (int c = 0; c < n; c++) {
            List<Integer> colList = new ArrayList<>();
            for (int r = 0; r < n; r++) {
                colList.add(grid[r][c]);
            }
            colMap.put(colList, colMap.getOrDefault(colList, 0) + 1);
        }

        for (int r = 0; r < n; r++) {
            List<Integer> rowList = new ArrayList<>();
            for (int c = 0; c < n; c++) {
                rowList.add(grid[r][c]);
            }
            counter += colMap.getOrDefault(rowList, 0);
            // 這邊可以查找多次，因為邊是rowList一直刷新，然後丟進具比對，所以可以不會因為重複就沒有加上次數
        }

        return counter;
    }
}
