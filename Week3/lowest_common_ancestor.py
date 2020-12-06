#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 二叉树的最近公共祖先


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not root:
            return
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        return root
