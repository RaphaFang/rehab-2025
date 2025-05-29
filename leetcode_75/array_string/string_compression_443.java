class Solution {
    public int compress(char[] chars) {
        int write = 0;
        int anchor = 0;

        for (int read = 0; read < chars.length; read++) {
            if (read + 1 == chars.length || chars[read] != chars[read + 1]) {
                chars[write++] = chars[anchor];

                int runLen = read - anchor + 1;
                if (runLen > 1) {
                    for (char d : String.valueOf(runLen).toCharArray()) {
                        chars[write++] = d;
                    }
                }
                anchor = read + 1;
            }
        }
        return write;
    }
}
// 這不是自己寫的，看不懂