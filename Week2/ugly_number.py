#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://leetcode-cn.com/problems/chou-shu-lcof/
# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        x, y, z = 0, 0, 0
        value = 1
        for i in range(1, n):
            n2, n3, n5 = ugly[x] * 2, ugly[y] * 3, ugly[z] * 5
            value = min(n2, n3, n5)
            ugly[i] = value
            if value == n2:
                x += 1
            if value == n3:
                y += 1
            if value == n5:
                z += 1
        return value

