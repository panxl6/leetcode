/**
 * 题目：
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

 

Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 

Note:

1 <= N <= 10^8
*/


// 典型的自定义概念题型、操作实现题型
// 同时，这也是一道典型的概念迁移、变形题。大整数运算，要把输入的字符串逐位提取，然后逐位计算后相加。
// 这道题的核心就是提取整数的bit。

#include <cmath>

using namespace std;

class Solution {
    
    static const int MAX_SIZE = 10;
    
public:
    bool isArmstrong(int N) {
        // 求出当前是几位数
        // 执行表达式求和，判断等价性
        
        int numbers[MAX_SIZE];
        int count = 1, temp = N, ret;
        
        for (; 1;) {
            ret = temp/10;
            numbers[count] = temp - ret*10;
            if (ret == 0) {
                break;
            }
            temp = ret;
            
            count++;
        }
        
        ret = 0;
        for (int i=1; i<=count; i++) {
            ret += pow(numbers[i], count);
        }       
        
        return ret == N;
    }
};