/**
 * 题目：
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.

Return 0 if S is odd, otherwise return 1.

 

Example 1:

Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation: 
The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.
Example 2:

Input: [99,77,33,66,55]
Output: 1
Explanation: 
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.
 

Note:

1. 1 <= A.length <= 100
2. 1 <= A[i].length <= 100
*/


// 这道题的核心就是提取整数的bit。
// 包装概念。

#include <vector>
#include <iostream>
#include <numeric>

using namespace std;



class Solution {
public:
    int sumOfDigits(vector<int>& A) {
        // 找出最小的数组中最小的元素
        int minElement = A[0];
        for (int i=1; i<A.size(); i++) {
            minElement = min(minElement, A[i]);
        }
        
        // 提取出这个数字的所有位
        vector<int> bitArr = extractBitsFromNumber(minElement);
        int result = accumulate(bitArr.begin(), bitArr.end(), 0);
        
        cout << result;
        // 对所有的位求和
        // 是否能被２整除
        if (result % 2 == 0) {
            return 1;
        }
        
        return 0;
    }
    
    // 提取一个正整数的所有位
    vector<int> extractBitsFromNumber(int number) {
        
        vector<int> bitArray;
        int temp = number, ret;
        
        for (; 1;) {
            ret = temp/10;
            bitArray.push_back(temp - ret*10);
            
            if (ret == 0) {
                break;
            }
            temp = ret;
        }
        
        return bitArray;
    }
};

