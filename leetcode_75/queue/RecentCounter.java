import java.util.ArrayDeque;
import java.util.Deque;

// 21ms 兩者的空間LinkedList作法多3mb
public class RecentCounter {
    private Deque<Integer> deque;

    public RecentCounter() {
        deque = new ArrayDeque<>();
    }

    public int ping(int t) {
        deque.addLast(t);
        while (deque.peekFirst() < t - 3000) {
            deque.removeFirst();
        }
        return deque.size();
        // while (!deque.isEmpty() && deque.peekFirst() < t - 3000) {
        // 這邊不用檢查為空，因為一定會有至少他自己在裡面
    }
}

// --------------------------------------------------------
// 361ms
// import java.util.Deque;
// import java.util.LinkedList;

// public class RecentCounter {
// private Deque<Integer> deque;

// public RecentCounter() {
// deque = new LinkedList<>();
// }

// public int ping(int t) {
// deque.addLast(t);
// deque.removeIf(time -> time < t - 3000);
// return deque.size();
// }
// }
// --------------------------------------------------------
// LinkedList，ArrayDeque
// 兩個速度這提差不多，但是ArrayDeque可以容納更高併發
// 但是兩個都不是thread safe，要透過其他LinkedBlockingDeque, ConcurrentLinkedDeque