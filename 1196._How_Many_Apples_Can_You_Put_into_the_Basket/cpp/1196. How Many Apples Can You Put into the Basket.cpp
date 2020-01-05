/**
 * 题目：
You have some apples, where arr[i] is the weight of the i-th apple.  You also have a basket that can carry up to 5000 units of weight.

Return the maximum number of apples you can put in the basket.

 

Example 1:

Input: arr = [100,200,150,1000]
Output: 4
Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.

Example 2:

Input: arr = [900,950,800,1000,700,800]
Output: 5
Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.

*/


#include <vector>
#include <iostream>
#include <numeric>
#include <map>
#include <bits/stdc++.h>

using namespace std;

// 由于这道题没有做任何的限制，用贪心算法即可求解。
// 这道题的follow up，可以是一个背包问题。
class Solution {
public:
    int maxNumberOfApples(vector<int>& arr) {
        
        sort(arr.begin(), arr.end());
        
        int sum = 0, i = 0;
        for (; i<arr.size(); i++) {
            sum += arr[i];
            if (sum > 5000) {
                break;
            }
        }
        
        return i;
    }
};