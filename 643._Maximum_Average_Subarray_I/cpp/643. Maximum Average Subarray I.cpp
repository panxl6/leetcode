/**
 * 题目：
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

*/


// 滑动窗口，固定窗口大小，从左滑向右。
// 滑动过程是单向的，求极值(特征值)。

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
        int kSum = 0;
        for (int i=0; i<k; i++) {
            kSum += nums[i];
        }
        
        int maxSum = kSum;
                
        for (int i=k; i<nums.size(); i++) {
            kSum += nums[i];
            kSum -= nums[i-k];
            maxSum = max(maxSum, kSum);
        }
        
        return maxSum / (k + 0.0);        
    }
};