/**
 * 题目：
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 

Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.

Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.

 

Note:

    1 <= A.length <= 2000
    0 <= A[i] <= 1000


*/


/**
 * 这道题并没有说清楚Ａ的排列(可以变为组合)是否允许重复选择。
 * 自定义概念的理解，操作的实现。
 * 底层的思想和堆栈的左右两个指针一样。
 * 
*/

#include <vector>
#include <iostream>
#include <numeric>

using namespace std;

class Solution {
public:
    int largestUniqueNumber(vector<int>& A) {
        int hash[1001];
        memset(hash, 0, sizeof(hash));
        
        for (int i=0; i<A.size(); i++) {
            hash[A[i]]++;
        }
        
        int maxNum = -1;
        for (int i=0; i<1001; i++) {
            if (hash[i] == 1) {
                maxNum = max(i, maxNum);
            }
        }
        
        return maxNum;        
    }
};