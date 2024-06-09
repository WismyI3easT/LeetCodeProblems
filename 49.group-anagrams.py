#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self) -> None:
        self.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = [[]]

        for i, s in enumerate(strs, 0):
            if i == 0:
                groups[0].append(strs[0])
                continue

            for g in groups:
                added = False
                if self.isAnagram(s, g[0]):
                    g.append(s)
                    added = True
                    break
                else:
                    continue
            if added == False:
                groups.append([s])

        return groups

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
# @lc code=end
