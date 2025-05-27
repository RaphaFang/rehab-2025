class Kata {
    public static int[] monkeyCount(final int n) {
        int[] result = new int[n];
        for (int i = 1, j = 0; i <= n; i++, j++) {
            result[j] = i;
        }
        return result;
    }
}
// !下面IntStream 效率不高
// import java.util.stream.IntStream;
// class MonkeyCounterOptimized {
// public static int[] monkeyCount(final int n) {
// return IntStream.rangeClosed(1, n).toArray();
// }
// }

// Ori ver.: 51 ms
// IntStream ver.: 209 ms
// 真的差異很大

// ----------------------------------------------------------------------------
// !1. final，意味著資料不能被改變
// py沒有，MEMBER_ID，靠自己遵守，也不是強制
// 要在建立函數之前，就決定函數回傳資料型態，函數輸入資歷型態

// !2. java 資料型態
// Java 有兩大類型別：primitive 與 reference。
// primitive（如 int、double）不是物件；reference（如 Integer、String）是物件的參考。
// 效能與記憶體：primitive 直接存值 → 速度快、占用少；
// reference 需額外物件 header，透過指標尋址，較耗空間。
// Autoboxing / Unboxing：int 與 Integer 混用時，編譯器會自動裝箱／拆箱，可能帶來額外開銷。
// Null：reference 可為 null；primitive 不行。
// Generics：只能使用 reference type，例如 List<Integer>；List<int> 不合法。
// Wrapper 類別（Integer 等）提供許多方法，如 parseInt、compareTo 等。

// !3. <>generics, type parameter, <T> 只是佔位, 只能放 reference type
// class Box<T> { … } // 類別
// interface Pair<K,V> { … } // 介面
// <T> void print(T item) { … } // 方法

// !4. dead code elimination
// 如果沒有儲存特定的值，那麼會跳過執行，JVM 很聰明不會浪費效能
// int[] result1 = monkeyCountOriginal(n);
// 所以還是需要int[] result1 ，不能直接呼叫函數

// ! arr 兩個資料型態都有
// Object[] result = new Object[size];
// int[] arr = new int[10];
// ----------------------------------------------------------------------------
