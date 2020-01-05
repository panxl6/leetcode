/**
 * 题目：
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

    If S[i] == "I", then A[i] < A[i+1]
    If S[i] == "D", then A[i] > A[i+1]

 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]

Example 2:

Input: "III"
Output: [0,1,2,3]

Example 3:

Input: "DDI"
Output: [3,2,0,1]

 

Note:

    1 <= S.length <= 10000
    S only contains characters "I" or "D".
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
    vector<int> diStringMatch(string S) {
        
        int left = 0, right = S.length();
        vector<int> list;
        
        for (int i=0; i<S.length(); i++) {
            if (S[i] == 'I') {
                list.push_back(left);
                left++;
            } else {
                list.push_back(right);
                right--;
            }
        }
        
        list.push_back(right);
        
        return list;
    }
};