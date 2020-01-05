/**
题目：
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 

Note:

The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree. 
 
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        // 将原有的树变为数组
        vector<int> list;
        transferTreeToList(root, list);
                
        traverseTree(root, sumGreaterResult(list));
            
        // 逐个累加
        return root;
    }
    
    void traverseTree(TreeNode* root, map<int, int>resultMap) {
        if (root == NULL) {
            return;
        }
        
        root->val = resultMap[root->val];
        traverseTree(root->left, resultMap);
        traverseTree(root->right, resultMap);
    }
    
    void transferTreeToList(TreeNode* root, vector<int> &arr) {
        if (root == NULL) {
            return;
        }
        
        transferTreeToList(root->left, arr);
        arr.push_back(root->val);
        transferTreeToList(root->right, arr);
        
        return;
    }
    
    map<int, int> sumGreaterResult(vector<int> arr)     {
        map<int, int> result;
        
        int total = 0;
        for (int i=arr.size()-1; i>=0; --i)  {
            total += arr[i];
            result[arr[i]] = total;
        }
        
        return result;
    }
};