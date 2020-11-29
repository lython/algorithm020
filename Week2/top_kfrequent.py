#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/top-k-frequent-elements/
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_dict = dict()
        for _ in nums:
            if _ not in my_dict:
                my_dict[_] = 0
            my_dict[_] += 1
        items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:k]
        result = [_[0] for _ in items]
        return result

    def topKFrequent2(self, nums, k):
        """
        方法2
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stat = Counter(nums)
        result = heapq.nlargest(k, stat.items(), key=lambda x: x[1])
        return [i for i, _, in result]


if __name__ == '__main__':
    t = Solution()
    z = t.topKFrequent([1,1,1,2,2,3], 2)
    print(z)