class Solution {
    public void moveZeroes(int[] nums) {
        int dot = 0;
        for (int i : nums) {
            if (i != 0) {
                nums[dot] = i;
                dot++;
            }
        } // 這邊的機制真的太聰明，0開頭，或是非0開頭都可以處理
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