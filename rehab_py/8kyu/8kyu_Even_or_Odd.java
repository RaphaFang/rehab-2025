public class Kata {
    public static String evenOrOdd(int number) {
        // return "Odd" if number&1 else "Even";
        return (number&1)==1 ? "Odd": "Even";
    }
}