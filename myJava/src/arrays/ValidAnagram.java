package arrays;

import java.util.*;

/**
 * Given two strings s and t, return true if the two strings are anagrams of
 * each other, otherwise return false.
 * An anagram is a string that contains the exact same characters as another
 * string, but the order of the characters can be different.
 * Input: s = "racecar", t = "carrace"
 * Output: true
 * 
 * Input: s = "jar", t = "jam"
 * Output: false
 * 
 * Constraints:
 * s and t consist of lowercase English letters.
 **/

public class ValidAnagram {

    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> s_map = new HashMap<>();
        Map<Character, Integer> t_map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            s_map.put(s.charAt(i), s_map.getOrDefault(s.charAt(i), 0) + 1);
            t_map.put(t.charAt(i), t_map.getOrDefault(t.charAt(i), 0) + 1);
        }

        // return s_map.equals(t_map);

        // Iterate using Map.entrySet()
        for (Map.Entry<Character, Integer> entry : s_map.entrySet()) {
            char ch = entry.getKey();
            int v = entry.getValue();

            if (!t_map.containsKey(ch) || (!t_map.get(ch).equals(v))) {
                return false;
            }
        }
        return true;

    }

    public static void main(String[] args) {
        String s = "racecar";
        String t = "carrace";

        boolean res = isAnagram(s, t);
        System.out.println(res);

    }
}
