class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            hashmap[val] = i

        for i, val in enumerate(nums):
            diff= target - val
            if diff in nums and hashmap[diff] != i:
                return [i, hashmap[diff]]