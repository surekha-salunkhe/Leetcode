package Easy;

import java.util.*;

public class FindDuplicates {

    /**
     * Case 1: Check if any duplicate exists.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static boolean hasDuplicates(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Case 2: Return duplicate elements as an unmodifiable List.
     *
     * Why unmodifiable?
     * - Prevents callers from modifying internal data.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static List<Integer> findDuplicatesAsList(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        List<Integer> duplicates = new ArrayList<>();

        for (int num : nums) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }

        // Return read-only view
        return Collections.unmodifiableList(duplicates);
    }

    /**
     * Case 3: Return duplicate elements as an array.
     *
     * Why clone?
     * - Arrays are mutable.
     * - Returning a clone prevents external modification.
     *
     * Time Complexity: O(n)
     * Space Complexity: O(n)
     */
    public static int[] findDuplicatesAsArray(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        List<Integer> duplicates = new ArrayList<>();

        for (int num : nums) {
            if (!seen.add(num)) {
                duplicates.add(num);
            }
        }

        int[] result = new int[duplicates.size()];
        for (int i = 0; i < duplicates.size(); i++) {
            result[i] = duplicates.get(i);
        }

        return result.clone(); // defensive copy
    }

    public static void main(String[] args) {
        int[] input = { 1, 2, 3, 2, 4, 1, 5 };

        // Case 1
        boolean hasDup = hasDuplicates(input);
        System.out.println("Has duplicates: " + hasDup);

        // Case 2
        List<Integer> listResult = findDuplicatesAsList(input);
        System.out.println("Duplicates (List): " + listResult);

        // Case 3
        int[] arrayResult = findDuplicatesAsArray(input);
        System.out.println("Duplicates (Array): " + Arrays.toString(arrayResult));
    }

    // Best default choice:
    // API layer → List<Integer>
    // Performance-critical → int[]
    // Validation check → boolean
}