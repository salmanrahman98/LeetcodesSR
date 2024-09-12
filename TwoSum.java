import java.util.HashMap;
import java.util.Map;

class Solution {

    
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println("[" + result[0] + ", " + result[1] + "]");
    }

    public static int[] twoSum(int[] nums, int target) {
            Map<Integer,Integer> dict = new HashMap();

            for(int i=0;i<nums.length;i++){
                dict.put(nums[i],i);
            }

            int i=0;
            for (int val: nums){
                int lookingFor = target-val;
                if(dict.containsKey(lookingFor)){
                    int lookingForIndex = dict.get(lookingFor);
                    if(i != lookingForIndex){
                        return new int[]{i,lookingForIndex};
                    }
                }
                i++;
            }
            return null;
    }
}