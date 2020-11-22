#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    hmap = {}

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            diff = target - v
            if diff in self.hmap:
                return [self.hmap[diff], i]
            self.hmap[v] = i
        return []


def test1():
    t = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    ret = t.twoSum(nums, target)
    print(ret)


if __name__ == '__main__':
    test1()
