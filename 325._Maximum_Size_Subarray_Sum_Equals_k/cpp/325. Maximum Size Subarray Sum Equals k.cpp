/**
 * 题目：
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?

*/

// 查找、求和、组合、子模式。
// 子数组、子串等都是滑动窗口类型的题。
// 求和操作存在冗余。子串有重叠的部分，这里就是冗余的地方。


#include <vector>
#include <iostream>
#include <numeric>
#include <map>
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        
        int maxLen = 0;
        int len = nums.size();
        
        for (int i=0; i<len; i++) {
            int tempSum = 0;
            for (int j=i; j<len; j++) {
                tempSum += nums[j];
                if (tempSum == k) {
                    maxLen = max(maxLen, j-i+1);
                }
            }
        }
        
        return maxLen;
    }
};