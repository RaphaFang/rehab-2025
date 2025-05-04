class Kata {
    public static String solution(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}

// StringBuilder
// 這函數變形後的 str 會是 StringBuilder格式，所以需要透過 toString轉換
// 整個函數回傳就需要改成StringBuilder類別 public static StringBuilder solution

// ----------------------------------------------------------------------------
// ! StringBuffer() 在多現程時使用
// public class Kata {
// public static String solution(String str) {
// return new StringBuffer(str).reverse().toString();
// }
// }

// ! char 基本行
// public class Kata {
// public static String solution(String str) {
// StringBuilder res = new StringBuilder(str.length());
// for (int i = (str.length() - 1); i >= 0; i--){
// res.append(str.charAt(i));
// }
// return res.toString();
// }

// ! 不是全部的type轉換都會涉及boxing
// str 是reference，但是得到的str.charAt(i)，會是pri
// res是 StringBuilder，但是res.append()，append可以加上char，且不涉及boxing
// 因為StringBuilder內部有寫好func可以調用pri