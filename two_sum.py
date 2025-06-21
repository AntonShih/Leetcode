# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # 建立一個字典來存放數字與其索引

        for i, num in enumerate(nums):  # 逐一走訪 nums 中的元素
            complement = target - num  # 計算目標補數（要找的另一個數）
            if complement in num_to_index:
                # 如果補數已經出現在字典中 → 找到答案
                return [num_to_index[complement], i]
            # 否則把當前數字和索引加入字典中
            num_to_index[num] = i
            # 資料庫["商品名稱"] = "價格"只要一執行，Python 就幫你把這筆資料記起來了。



        return []  # 理論上不會進到這行，因為題目保證一定有解
