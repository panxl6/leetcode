/**
 * 题目：
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

 
https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png

 

We should return its max depth, which is 3.

 

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

*/


// 典型的基础知识题
// 二叉树是教科书的基础内容。二多叉树的操作，考察的是如何讲二叉树的用法扩展到多叉树。
// 树的递归操作，用栈遍历、在没有指针的动态语言中如何操作，这些都要熟练默写出来。
// 二叉查找树的，前序、中序、后序遍历也要熟练默写。

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    int maxDepth(Node* root) {
        if (root == NULL) {
            return 0;
        }
        
        return findMaxDepthOfTree(root, 0, 0);
    }
    
    int findMaxDepthOfTree(Node *root, int maxDepth, int currentDepth) {
        
        currentDepth += 1;
                
        if (root == NULL || root->children.size() == 0) {
            return max(maxDepth, currentDepth);
        }
                       
        for (int i=0; i<root->children.size(); i++) {
            int depth = findMaxDepthOfTree(root->children[i], maxDepth, currentDepth);
            maxDepth = max(maxDepth, depth);
        }        
        
        return maxDepth;
    }
};