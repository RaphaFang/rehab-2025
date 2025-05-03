import java.util.ArrayList;
import java.util.List;

class Kata_original {
    public static Object[] removeEveryOther(Object[] arr) {
        List<Object> result = new ArrayList<>();
        for (int i = 0; i < arr.length; i += 2) {
            result.add(arr[i]);
        }
        return result.toArray();
    }
}

class Kata_optimized {
    public static Object[] removeEveryOther(Object[] arr) {
        int size = (arr.length + 1) / 2;
        Object[] result = new Object[size];

        for (int i = 0, j = 0; i < arr.length; i += 2, j += 1) {
            result[j] = arr[i];
        }
        return result;
    }
}

// !1. optimized
// 要基於java的資料結構
// Object[] 比 List<Object> 快，但是必須一次性寫死[]內部有的元件數量，會變null存在裡面
// List 可以用 .add()
// Object[] 只能用 arr[i]= x
// 但是List底層仍然是Object，List會設定一個政列數量，不夠用時會自動複製