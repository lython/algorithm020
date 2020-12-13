#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/jump-game-ii/


from typing import List


class Solution:
    """
    跳跃游戏，跳跃的步数最少
    """
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0

        jump_max = 0  # 每个下标位置能跳的最远距离
        steps = 0  # 步数
        end = 0
        length = len(nums)
        for i in range(length - 1):
            #
            if jump_max >= i:
                jump_max = max(jump_max, i + nums[i])
                # 到达边界
                if i == end:
                    end = jump_max
                    steps += 1
        return steps


if __name__ == '__main__':
    t = Solution()
    print(t.jump([1, 1, 1, 1, 1, 1]))
