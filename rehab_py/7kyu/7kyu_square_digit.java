import java.util.ArrayList;
import java.util.List;

class SquareDigit {
    public static int squareDigits(int n) {
        char[] digits = String.valueOf(n).toCharArray();
        String[] arr = new String[digits.length];
        for (int i = 0; i < digits.length; i++) {
            int num = digits[i] - '0';
            arr[i] = String.valueOf(num * num);
        }
        return Integer.parseInt(String.join("", arr));
    }

    public static int optimized_1(int n) {
        if (n == 0)
            return 0;
        List<String> list = new ArrayList<>();

        while (n > 0) {
            int num = n % 10;
            list.add(0, String.valueOf(num * num)); // 倒著，加到最前面
            n /= 10; // 這是砍掉一個位數
        }
        return Integer.parseInt(String.join("", list));
    }
}

// 兩者差異不代，幾乎沒差可以通用
// Ori ver.: 0.050687 ms
// Opt_1 ver.: 0.059204 ms
// -------------------------------------
// ! String.valueOf(int)
// 相比於 Integer.toString(int);更加通用
// Integer.parseInt(String)

// ! - '0';
// str轉換成數字，可以透過砍位元數，讓他強制變成num
// 這只能用在 char

// ! StringBuilder[] sb = new StringBuilder[digits.length];
// 這建立出來會是「只能」塞StringBuilder物件的list
// 沒辦法 sb.append(num * num)

// StringBuilder 是用來「頻繁修改字串」時的最佳解
// 常見用途（效能導向）：
// 場景 為什麼用 StringBuilder？
// 頻繁 append 多段文字 不會產生太多中間 String 物件（效能優）
// 字串拼接迴圈（ex: for 中組字串） + 每次都會建立新 String，很慢
// Web Log、HTML 組合 大量字串拼接，不適合用 +