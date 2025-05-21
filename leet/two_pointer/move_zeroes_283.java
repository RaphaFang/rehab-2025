import java.util.ArrayList;
import java.util.List;

class Solution {
    public void moveZeroes(int[] nums) {
        int dot = 0;
        for (int i : nums) {
            if (i != 0) {
                nums[dot] = i;
                dot++;
            }
        }
        while (dot < nums.length) {
            nums[dot] = 0;
            dot++;
        }
    }
}

// ----------------------------------------------------------------------
// !nums 這邊是primitive，所以clear()這函數不能用
// class Solution {
// public void moveZeroes(int[] nums) {
// List<Integer> zeroList = new ArrayList<>();
// List<Integer> cList = new ArrayList<>();

// for (int i = 0; i < nums.length; i++) {
// if (nums[i] == 0) {
// zeroList.add(0);
// } else {
// cList.add(nums[i]);
// }
// }
// ! nums.clear();
// cList.addAll(zeroList);
// nums.addAll(cList);
// }
// }