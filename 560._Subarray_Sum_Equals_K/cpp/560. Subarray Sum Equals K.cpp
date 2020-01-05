/**
 * 题目：
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

*/


// 滑动窗口，固定窗口大小，从左滑向右。
// 滑动过程是单向的，统计符合特征的元素个数。

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        int len = nums.size();
        
        for (int i=0; i<len; i++) {
            int tempSum = 0;
            for (int j=i; j<len; j++) {
                tempSum += nums[j];
                if (tempSum == k) {
                    count++;
                }
            }
        }
        
        return count;
    }
};
