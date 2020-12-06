#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        count = len(digits)
        result = []
        diff = []  # 不同的组合

        def backtrack(index: int):
            if index == count:
                result.append("".join(diff))
            else:
                number = digits[index]
                for letter in phone_dict[number]:
                    diff.append(letter)
                    print(diff)
                    backtrack(index + 1)
                    diff.pop()

        backtrack(0)
        return result


if __name__ == '__main__':
    t = Solution()
    aa = t.letterCombinations("23")
    print(aa)


