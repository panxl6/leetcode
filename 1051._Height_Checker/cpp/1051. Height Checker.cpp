/**
 * 题目：
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

 

Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.

 

Note:

    1 <= heights.length <= 100
    1 <= heights[i] <= 100

*/


#include <vector>
#include <iostream>
#include <numeric>
#include <map>
#include <bits/stdc++.h>

using namespace std;

// 基础概念考察题。
/**
　需要移动的元素个数，其实就是机选无序的元素的个数。利用跟有序元素的差分比较即可。
 这道题的一个follow up是，求移动次数。也即是逆序数。
*/

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        
        vector<int> copy = heights;
        sort(heights.begin(), heights.end());
        
        int diffCount = 0;
        for (int i=0; i<heights.size(); i++) {
            if (copy[i] != heights[i]) {
                diffCount++;
            }
        }
        
        return diffCount;        
    }
};