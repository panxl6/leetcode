/**
 * 题目：
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

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
    int findMaxConsecutiveOnes(vector<int>& arr) {
        int optim = 0, left = 0, right = 0, zeroNum = 1;

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