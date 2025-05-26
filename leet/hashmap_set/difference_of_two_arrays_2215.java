import java.util.*;

// ! 22ms
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>(Arrays.stream(nums1).boxed().toList());
        Set<Integer> set2 = new HashSet<>(Arrays.stream(nums2).boxed().toList());

        Set<Integer> diff1 = new HashSet<>(set1);
        diff1.removeAll(set2);

        Set<Integer> diff2 = new HashSet<>(set2);
        diff2.removeAll(set1);

        return List.of(new ArrayList<>(diff1), new ArrayList<>(diff2));
        // 因為這邊出來的東西要是List<List<Integer>>，所以要轉換hash
    }
}

//
// -----------------------------------------------------------------------------
// ! removeAll()
// removeAll() 的回傳值是 boolean → 表示「有沒有成功移除任何元素」
// 但重點不是這個回傳值，而是它的副作用（副作用 = 直接改變了 diff1 本身）

// -----------------------------------------------------------------------------
// ! Set.copyOf
// Set<Integer> set1 = Set.copyOf(Arrays.stream(nums1).boxed().toList());
// Set<Integer> set2 = Set.copyOf(Arrays.stream(nums2).boxed().toList());
// 這用意是不讓複製過來的東西可改動，可以用再回傳的api

// -----------------------------------------------------------------------------
// ! 14ms
// class Solution {
// public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
// Set<Integer> set1 = new HashSet<>();
// Set<Integer> set2 = new HashSet<>();

// for (int num : nums1) set1.add(num);
// for (int num : nums2) set2.add(num);

// Set<Integer> diff1 = new HashSet<>(set1);
// diff1.removeAll(set2);

// Set<Integer> diff2 = new HashSet<>(set2);
// diff2.removeAll(set1);

// return List.of(new ArrayList<>(diff1), new ArrayList<>(diff2));
// }
// }
