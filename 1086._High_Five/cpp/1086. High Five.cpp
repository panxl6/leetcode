/**
 * 题目：
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

 

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

 

Note:

    1 <= items.length <= 1000
    items[i].length == 2
    The IDs of the students is between 1 to 1000
    The score of the students is between 1 to 100
    For each student, there are at least 5 scores

*/

// 这道题考察基础只是。哈希表的应用，排序、求和。如果一边遍历、一遍排序、一遍求和，会快速一点。但是可读性不太好。


#include <vector>
#include <iostream>
#include <numeric>
#include <map>
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        
        vector<vector<int>> ret;
        map<int, vector<int>> tempMap;
        
        for (int i=0; i<items.size(); i++) {
            if (tempMap.find(items[i][0]) == tempMap.end()) {
                vector<int> list;
                list.push_back(items[i][1]);
                tempMap[items[i][0]] = list;
            } else {
                tempMap[items[i][0]].push_back(items[i][1]);
            }
        }
        
        for (map<int, vector<int>>::iterator itr=tempMap.begin(); itr!=tempMap.end(); ++itr) {
            vector<int> pair;
            pair.push_back(itr->first);
            
            sort(itr->second.begin(), itr->second.end(), greater<int>());
            
            int sum = 0;
            int i = 0;
            for (; i<5 && i<itr->second.size(); i++) {
                sum += itr->second[i];
            }
            pair.push_back(sum/i);
            ret.push_back(pair);
            
        }
        
        return ret;
    }
};