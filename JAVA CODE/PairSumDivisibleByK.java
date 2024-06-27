import java.util.*;
public class PairSumDivisibleByK {
    public static void main(String[] args) {
        int[] arr = { 3, 1, 2, 6, 9, 4 };
        int k = 5;
        List<String> pairs = findPairs(arr, k);
        if (pairs.isEmpty()) {
            System.out.println("Pairs cannot be formed");
        } else {
            System.out.println("Pairs can be formed:");
            for (String pair : pairs) {
                System.out.println(pair);
            }
        }
    }
    public static List<String> findPairs(int[] arr, int k) {
        List<String> pairs = new ArrayList<>();
        Map<Integer, Integer> remainderCount = new HashMap<>();
        for (int num : arr) {
            int remainder = num % k;
            int complement = (k - remainder) % k;

            if (remainderCount.containsKey(complement) && remainderCount.get(complement) > 0) {
                pairs.add("(" + num + ", " + complement + ")");
                remainderCount.put(complement, remainderCount.get(complement) - 1);
            } else {
                remainderCount.put(remainder, remainderCount.getOrDefault(remainder, 0) + 1);
            }
        }
        return pairs;
    }
}