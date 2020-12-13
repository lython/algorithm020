#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    def mySqrt(self, x: int) -> int:
        """二分查找"""
        if x <= 0:
            return 0
        if x == 1:
            return 1

        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2  # 2left + right - left
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def mySqrt2(self, x: int) -> int:
        """牛顿迭代法"""
        if x < 0:
            raise Exception("not minus")
        if x == 0 or x == 1:
            return x

        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-10:
                return cur

    def mySqrt3(self, x: int) -> int:
        """牛顿迭代法"""
        if x < 0:
            raise Exception("not minus")
        if x == 0 or x == 1:
            return x

        r = x
        while r > x / r:  # 就是 r * r > x, 对于 C 这种严格 int 和 long，这样写能防止溢出
            r = (r + x / r) / 2
        return r


if __name__ == '__main__':
    t = Solution()
    print(t.mySqrt3(2))
