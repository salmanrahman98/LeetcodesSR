//https://leetcode.com/problems/search-insert-position/
package Arrays;

public class SearchInsert {
    public static void main(String[] args) {
        int[] nums = { 1, 3, 5, 6 };
        int target1 = 5;
        int target2 = 2;

        System.out.println(searchInsert(nums, target1));
        System.out.println(searchInsert(nums, target2));
    }

    public static int searchInsert(int[] nums, int target) {

        int low = 0;
        int high = nums.length - 1;
        int m = low + high / 2;

        while (low <= high) {
            m = low + (high - low) / 2;

            if (nums[m] > target) {
                high = m - 1;
            } else if (nums[m] < target) {
                low = m + 1;
            } else {
                break;
            }
        }

        if (target == nums[m]) {
            return m;
        } else if (high != -1 && target > nums[high]) {
            return high + 1;
        } else if (target < nums[low]) {
            return low;
        }

        return m;

    }
}
