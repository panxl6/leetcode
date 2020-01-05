/**
 * 题目：
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1

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
    int longestOnes(vector<int>& arr, int zeroNum) {
        int optim = 0, left = 0, right = 0;

        while (right < arr.size()) {
            if (arr[right] == 0) {
                zeroNum--;
            }
            
            if (zeroNum >= 0) {
                optim = max(optim, right - left + 1);
            } else {
                // 左指针移动
                while (left < arr.size()) {
                    if (arr[left] == 0) {
                        zeroNum++;
                    }

                    left++;
                    if (zeroNum >= 0) {
                        break;
                    }
                }
            }
            right++;
        }

        return optim;
    }
};