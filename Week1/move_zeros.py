#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/move-zeroes/
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。


class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i, v in enumerate(nums):
            if v != 0:
                nums[i], nums[zero] = nums[zero], v
                zero += 1


if __name__ == '__main__':
    t = Solution()
    aa = [0, 1, 0, 3, 12, 0, 0]
    bb = t.moveZeroes(aa)
    print(aa)
