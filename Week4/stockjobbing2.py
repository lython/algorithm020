#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from typing import List


class Solution:
    """
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
    买卖股票的最佳时机2，可以卖卖多次
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        如果今天第 k 天卖，那么就应该在[0:k]之间的最小值的时候买
        :param prices:
        :return:
        """
        total = 0
        length = len(prices)
        for i in range(length - 1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total
