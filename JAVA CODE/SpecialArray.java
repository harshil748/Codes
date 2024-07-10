import java.util.Arrays;

class Solution {
    public int specialArray(int[] nums) {
        Arrays.sort(nums); // Sorting the array
        int N = nums.length; // Length of the array
        for (int x = 1; x <= N; x++) { // Looping through the array
            int count = 0; // Initializing count to 0
            for (int num : nums) { // iterating through each element int the array
                if (num >= x) { // Checking if the element is greater than or equal to x
                    count++; // Incrementing the count
                }
            }
            if (count == x) { // Checking if the count is equal to x
                return x; // Returning x
            }
        }
        return -1; // Returning -1 if no such x exists
    }
}