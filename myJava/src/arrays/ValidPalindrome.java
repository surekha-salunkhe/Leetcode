package arrays;

// import java.util.*;

public class ValidPalindrome {

    // Check palindrome by converting str to charArray, two pointer, fails as
    // lowercase is not considered
    public static boolean isPalindromeCharArray(String str) {
        if (str == null || str.isEmpty())
            return true;

        char[] chars = str.toCharArray();
        int left = 0, right = chars.length - 1;

        while (left < right) {
            if (chars[left] != chars[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static boolean isPalindromeStringLower(String str) {
        if (str == null || str.isEmpty())
            return true;

        str = str.toLowerCase().replaceAll("[^a-z0-9]", "");
        int left = 0, right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;

    }
    // O(n) time, O(n) space since new str created

    public static boolean isPalindromeInPlace(String s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            while (left < right && !alphaNum(s.charAt(left))) {
                left++;
            }
            while (left < right && !alphaNum(s.charAt(right))) {
                right--;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static boolean alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }

    public static void main(String[] args) {
        String s = "Madam";
        boolean res = isPalindromeCharArray(s);
        System.out.println("By char array without lowercase: " + res);

        boolean res1 = isPalindromeStringLower(s);
        System.out.println("By String loop with lowercase: " + res1);

        boolean res2 = isPalindromeInPlace(s);
        System.out.println("In-place palindrome check : " + res2);

    }
}
