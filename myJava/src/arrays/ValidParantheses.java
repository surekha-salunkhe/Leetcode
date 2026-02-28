package arrays;

import java.util.*;

public class ValidParantheses {

    /*
     * You are given a string s consisting of the following characters: '(', ')',
     * '{', '}', '[' and ']'.
     * 
     * The input string s is valid if and only if:
     * Every open bracket is closed by the same type of close bracket.
     * Open brackets are closed in the correct order.
     * Every close bracket has a corresponding open bracket of the same type.
     * Return true if s is a valid string, and false otherwise.
     * 
     * Example 1:
     * Input: s = "[]"
     * Output: true
     * 
     * Example 2:
     * Input: s = "([{}])"
     * Output: true
     * 
     * Example 3:
     * Input: s = "[(])"
     * Output: false
     * Explanation: The brackets are not closed in the correct order.
     * 
     * Constraints:
     * 1 <= s.length <= 1000
     */
    public static boolean isValidParantheses(String s) {

        Map<Character, Character> brackets = new HashMap<>();
        Deque<Character> stack = new ArrayDeque<>();

        brackets.put(')', '(');
        brackets.put(']', '[');
        brackets.put('}', '{');

        for (char c : s.toCharArray()) {
            if (brackets.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == brackets.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String s = "([({})])";
        boolean res = isValidParantheses(s);

        System.out.println(res);
    }
}
