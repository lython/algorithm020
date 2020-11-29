#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 二叉树遍历
# 中序 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# 二叉树遍历

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    traversal_path = []

    def preorder(self, root: TreeNode):
        """
        前序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.traversal_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root: TreeNode):
        """
        中序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorder(root.left)
            self.traversal_path.append(root.val)
            self.inorder(root.right)

    def postorder(self, root: TreeNode):
        """
        后序遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traversal_path.append(root.val)



