class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in complement_dict:
                return [complement_dict[complement], index] 
            else:
                complement_dict[value] = index
        return None