/**
 * 题目：
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
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
    vector<int> findAnagrams(string s, string p) {
        vector<int>result;
        int left = 0, right = 0, hashMap[256];
        memset(hashMap, 0, sizeof(hashMap));
        
        // 初始化
        for (int i=0; i<p.size(); i++) {
            hashMap[p[i]]++;
        }

        while (right < s.size()) {
            hashMap[s[right]]--;
            while (hashMap[s[right]] < 0) {
                hashMap[s[left]]++;
                left++;
            }

            if ((right - left + 1) == p.size()) {
                result.push_back(left);
            }
            right++;
        }

        return result;
    }
};