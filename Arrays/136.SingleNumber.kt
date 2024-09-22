//https://leetcode.com/problems/single-number/
class Solution {

    fun singleNumber(nums: IntArray): Int {

        val hashmap : HashMap<Int,Int> = HashMap()

        for(i in nums){
            hashmap[i] = hashmap.getOrDefault(i,0)+1
        }

        return hashmap.entries.first {it.value == 1}.key

    }
}