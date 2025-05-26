class Kata {
    public static int makeNegative(final int x) {
        return (x > 0) ? 0 - x : x;
    }
}

// !使用abs()，速度比原先慢了20倍
// Ori ver.: 0.001269 ms ms
// optimized ver.: 0.026335 ms ms