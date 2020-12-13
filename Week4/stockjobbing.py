#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from typing import List


class Solution:
    """
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
    买卖股票的最佳时机, 只允许买卖一次
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        如果今天第 k 天卖，那么就应该在[0:k]之间的最小值的时候买
        :param prices:
        :return:
        """
        min_buy = 4294967296  # 最小买入，默认设一个很大的值
        max_sell = 0  # 最大卖出
        for p in prices:
            min_buy = min(p, min_buy)
            max_sell = max(p - min_buy, max_sell)
        return max_sell
