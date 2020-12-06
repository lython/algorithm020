#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def DFS(queens: List[int], xy_dif: List[int], xy_sum: List[int]):
            """
            :param queens: 皇后的列下标
            :param xy_dif: 列下标的左上右下，差相等，也就是斜率一样
            :param xy_sum: 列下标的左下右上，合相等
            :return:
            """

            y = len(queens)
            if y == n:
                result.append(queens)
                return

            for x in range(n):
                if x not in queens and y-x not in xy_dif and y+x not in xy_sum:
                    DFS(queens + [x], xy_dif + [y - x], xy_sum + [y + x])

        DFS([], [], [])

        print(result)

        return [["*" * i + "Q" + "*" * (n - i - 1) for i in sol] for sol in result]


if __name__ == '__main__':
    t = Solution()
    aa = t.solveNQueens(4)
    print(len(aa))
    print(aa)
