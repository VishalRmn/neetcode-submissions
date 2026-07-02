class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for index, val in enumerate(nums):
            complement = target - val
            if complement in hashMap.keys():
                return [hashMap[complement], index]
            else:
                hashMap[val] = index

              
        