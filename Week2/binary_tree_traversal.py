#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# 二叉树中序遍历

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    traversal_path = []

    def inorderTraversal(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderTraversal(root.left)
            if root.val:
                self.traversal_path.append(root.val)
            self.inorderTraversal(root.left)

