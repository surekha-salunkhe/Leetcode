package arrays;

public class ReverseString {
    /*
     * Reverse a string without using StringBuilder.reverse()
     * Reverses a string using two-pointer technique.
     * Time Complexity: O(n)
     * Space Complexity: O(n) due to char array.
     */

    public static String reverseString(String s) {

        if (s == null || s.length() < 2) {
            return s;
        }

        char[] chars = s.toCharArray();

        int leftIndex = 0;
        int rightIndex = chars.length - 1;

        while (leftIndex < rightIndex) {
            char temp = chars[leftIndex];
            chars[leftIndex] = chars[rightIndex];
            chars[rightIndex] = temp;

            leftIndex++;
            rightIndex--;
        }

        return new String(chars);

        // with StringBuilder
        // return new StringBuilder(s).reverse().toString();

    }

    public static void main(String[] args) {
        String s = "abcde";

        String res = reverseString(s);

        System.out.println(res);
    }
}
