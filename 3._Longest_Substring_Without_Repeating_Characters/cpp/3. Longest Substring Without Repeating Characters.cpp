/**
 * 题目：
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

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
    int lengthOfLongestSubstring(string s) {
        map<char, int> hashMap;
        int optim = 0;
        int left = 0, right = 0;

        while (right < s.size()) {
            
            if (hashMap.count(s[right]) == 0) {
                hashMap[s[right]] = 1;
                optim = max(optim, right - left + 1);
            } else {
                // 已经存在
                // 左指针要移动了
                while (left < s.size()) {
                    if (s[left] != s[right]) {
                        hashMap.erase(s[left]);
                        left++;
                    } else {
                        left++;
                        break;
                    }
                }
            }
            right++;
        }

        return optim;
    }
};