//https://leetcode.com/problems/merge-sorted-array/
package Arrays;

public class MergeSorted {

    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int m = 3;
        int[] nums2 = {2, 5, 6};
        int n = 3;

        merge(nums1, m, nums2, n);

        // Print the merged array
        for (int num : nums1) {
            System.out.print(num + " ");
        }
    }
        public static void merge(int[] nums1, int m, int[] nums2, int n) {
    
            int[] sorted_arr = new int[m + n];
            int l = 0, r = 0, k = 0;
            while (l<m && r<n) {
                
                if (nums1[l] <= nums2[r]) {
                    sorted_arr[k] = nums1[l];
                    l++;
                } else {
                    sorted_arr[k] = nums2[r];
                    r++;
                }
    
                k++;
            }
    
            while (l < m) {
                if (k < m + n) {
                    sorted_arr[k] = nums1[l];
                    k++;
                }
                l++;
            }
    
            while (r < n) {
                if (k < m + n) {
                    sorted_arr[k] = nums2[r];
                    k++;
                }
                r++;
            }
    
            for (int i = 0; i < m + n; i++) {
                nums1[i] = sorted_arr[i];
            }
        }
}
