/**
 * 题目：
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

    a, b are from arr
    a < b
    b - a equals to the minimum absolute difference of any two elements in arr

 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

 

Constraints:

    2 <= arr.length <= 10^5
    -10^6 <= arr[i] <= 10^6


*/


// 这道题的核心就是提取整数的bit。
// 包装概念。

#include <vector>
#include <iostream>
#include <numeric>
#include <algorithm>    // std::sort

using namespace std;

class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        
        sort(arr.begin(), arr.end());
        
        int diff = 0;
        int minDiff = arr[1] - arr[0];
        vector<int> diffValue;
        for (int i=1; i<arr.size(); i++) {
            diff = arr[i] - arr[i-1];
            minDiff = min(minDiff, diff);
            diffValue.push_back(diff);
        }
        
        vector<vector<int>> result;
        for (int i=0; i<diffValue.size(); i++) {
            if (diffValue[i] == minDiff) {
                vector<int> pair{arr[i], arr[i+1]};
                
                result.push_back(pair);
            }
        }
        
        return result;
        
    }
};