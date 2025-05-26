class number_to_string {
    public static String numberToString(int num) {
        return String.valueOf(num);
        // Integer.toString(num)
    }
}

// ""+num
// 語法糖，但是效率更差，實際上是做了
// new StringBuilder().append("").append(num).toString();

// ----------------------------------------------------------------------------
// ! String.valueOf(num)
// ! Integer.toString(num)

// !StringBuilder
// 可以修改字串內容的物件，它內部用 char[] 陣列（字元陣列）儲存每個 char
// 並且是 mutable

// ! 為甚麼這邊return 不用寫new？
// return String.valueOf(num);
// return new StringBuilder(str).reverse().toString();
// 這幾個都是class，代是內部有不同的method，StringBuilder內部也有 static method
// 這例子中只是我剛好用到reverse()，他是instance method
// 所以要加上new。而上方的String 用到的static 不必寫new