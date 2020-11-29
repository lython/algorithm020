#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 242. 有效的字母异位词
# https://leetcode-cn.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        table = {}
        for x in s:
            if x not in table:
                table[x] = 0
            table[x] += 1

        for y in t:
            if y not in table:
                return False
            table[y] -= 1
            if table[y] < 0:
                return False
        return True


if __name__ == '__main__':
    t = Solution()
    print(t.isAnagram("aacc", "ccac"))
