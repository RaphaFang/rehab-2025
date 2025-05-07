class Kata {
    public static String[] capMe(String[] strings) {
        String[] result = new String[strings.length];
        for (int i = 0; i < strings.length; i++) {
            result[i] = strings[i].isEmpty() ? ""
                    : strings[i].substring(0, 1).toUpperCase() + strings[i].substring(1).toLowerCase();
        }
        return result;
    }
}
// if (strings[i].isEmpty()) {
// result[i] = "";
// } else {
// result[i] = strings[i].substring(0, 1).toUpperCase() +
// strings[i].substring(1).toLowerCase();
// }