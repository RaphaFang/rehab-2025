class SpiralingBox {
  public static int[][] createBox(int width, int length) {
    int[][] result = new int[length][width];
    for (int x = 0; x < length; x++) {
      for (int y = 0; y < width; y++) {
        int min = Math.min(Math.min(y + 1, width - y), Math.min(x + 1, length - x));
        result[x][y] = min;
      }
    }
    return result;
  }
}

// ! Arrays.stream(arr).min().getAsInt()
// ! 這方式比Math.min慢10倍，並且比較位元也不多，用Math就好
// int left = y + 1;
// int right = width - y;
// int up = x + 1;
// int down = length - x;
// int[] arr = { left, right, up, down };
// int min = Arrays.stream(arr).min().getAsInt();
