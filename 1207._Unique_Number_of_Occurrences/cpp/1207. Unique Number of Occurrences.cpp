/**
 * 题目：
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
*/


// 典型的统计类题目。词频统计、去重，基本上用到字典(哈希表)。
// 包装概念。

#include <vector>
#include <iostream>
#include <memory.h>

using namespace std;


class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
        int wordHash[2002];
        memset(wordHash, 0, sizeof(wordHash));
        
        // 词频统计, 一阶导数
        for (int i=0; i<arr.size(); i++) {
            wordHash[arr[i] + 1000]++;
        }
        
        // 去重,　二阶导数
        int uniqueHash[1000];
        memset(uniqueHash, 0, sizeof(uniqueHash));
        for (int i=0; i<2002; i++) {
            
            if (wordHash[i] == 0) {
                continue;
            }
            
            if (uniqueHash[wordHash[i]] >= 1) {
                return false;
            }
            
            uniqueHash[wordHash[i]]++;
        }
        
        return true;
    }
};