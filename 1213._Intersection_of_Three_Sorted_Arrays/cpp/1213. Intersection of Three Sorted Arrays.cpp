/**
 * 题目：
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

 
Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000

*/


// 基础操作题。集合的操作(运算)，基本上要用到哈希表来实现。
// 频率统计、存在性检查、去重，基本上都是集合运用的场景。


class Solution {
public:
    vector<int> arraysIntersection(vector<int>& arr1, vector<int>& arr2, vector<int>& arr3) {
        
        // 使用c++ stl的hash_map?
        int hashmap[2001];
        memset(hashmap, 0, sizeof(hashmap));
        
        // 这两个for循环有没有继续优化的必要，为了提升可读性，再嵌套一层？
        for (int i=0; i<arr1.size(); i++) {
            hashmap[arr1[i]]++;
        }
        
        for (int i=0; i<arr2.size(); i++) {
            hashmap[arr2[i]]++;
        }
        
        vector<int> result;
        result.clear();
        for (int i=0; i<arr3.size(); i++) {
            if (hashmap[arr3[i]] == 2) {
                result.push_back(arr3[i]);
            }
        }
                
        return result;
    }
};