#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        sorted_nums = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [num for num, freq in sorted_nums[:k]]

# @lc code=end

