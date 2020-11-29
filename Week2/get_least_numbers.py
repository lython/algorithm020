#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
# 最小的 k 个数
# return sorted(arr)[:k]

import heapq


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(arr) < k:
            return []
        heapq.heapify(arr)
        arr_res = []
        for i in range(k):
            arr_res.append(heapq.heappop(arr))
        return arr_res

    def getLeastNumbers2(self, arr, k):
        return sorted(arr)[:k]
