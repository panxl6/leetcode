/**
 * 题目：
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
 

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'

*/


// 这是一道典型的新概念题、基础概念变形题
// 平衡，其实就是对称，或者说字符串是闭合的、匹配的。
// 跟括号匹配是同一个本质。那么用栈来记忆，或者说实现匹配。
// 这也是一道典型的双指针题。

class Solution {
public:
    int balancedStringSplit(string s) {
        int left = 0, right = 0, count = 0;
        
        for (int i=0; i<s.length(); i++) {
            if (s[i] == 'R') {
                right++;
            } else {
                left++;
            }
            
            
            // 识别到了一个对称体，重置(刷新)用于记忆状态的指针
            if (left == right) {
                count++;
                left = right = 0;
            }
        }
        
        return count;
        
    }
};