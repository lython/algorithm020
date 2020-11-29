#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# N叉树的前序遍历


# Definition for a Node.
class NodeTree(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: NodeTree
        :rtype: List[int]
        """
        traversal_path = []

        def dfs(node):
            if node:
                traversal_path.append(node.val)
                if node.children:
                    for chi in node.children:
                        dfs(chi)

        dfs(root)
        return traversal_path
