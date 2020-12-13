#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/jump-game/

from typing import List


class Solution:
    """
    跳跃游戏
    """
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        length = len(nums)
        # 长度为1就甭跳了
        if length == 1:
            return True
        jump_index = 0  # 能跳的最远距离
        for i, v in enumerate(nums):
            if i > jump_index:
                return False
            # 当前可跳的最大举例，和上一个能跳的最大距离
            jump_index = max(i + v, jump_index)

            # 早日达到早日跳出
            if jump_index >= length - 1:
                return True

        return jump_index >= length - 1

    def canJump2(self, nums: List[int]) -> bool:
        if not nums:
            return False
        jump_index = 0
        for i, v in enumerate(nums):
            if i > jump_index:
                return False
            jump_index = max(i+v, jump_index)
        return True

    def canJump3(self, nums: List[int]) -> bool:
        """倒着走，看能不能走到 0"""
        if not nums:
            return False
        length = nums.__len__()
        index_end = length - 1
        for i in range(length - 1, -1, -1):
            if i + nums[i] > index_end:
                index_end = i
        return index_end == 0


if __name__ == '__main__':
    t = Solution()
    print(t.canJump2([]))
    print(t.canJump2([2, 0, 0, 0]))
    # print(t.canJump([3, 2, 1, 0, 4]))
    print(t.canJump2([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))

