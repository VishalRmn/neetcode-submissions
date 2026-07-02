class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #sort the array
        nums_sorted = sorted(nums)

        # initialize result array
        res = []

        #iterate to find triplets
        for i, num in enumerate(nums_sorted):
            if i > 0 and num == nums_sorted[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sums = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]
                if sums > 0:
                    k -= 1
                elif sums < 0:
                    j += 1
                else:
                    res.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    j+=1
                    while nums_sorted[j] == nums_sorted[j-1] and j < k:
                        j+=1
        return res
            
