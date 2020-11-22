#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        slow_index = 0
        for index, value in enumerate(nums, start=1):
            if nums[slow_index] != value:
                slow_index += 1
                nums[slow_index] = value
        return slow_index + 1


if __name__ == '__main__':
    t = Solution()
    aa = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    bb = t.removeDuplicates(aa)
    print(aa, bb)
