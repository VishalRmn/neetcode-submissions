class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #sort the array
        nums_sorted = sorted(nums)
        #print(nums_sorted)
        
        #initialize empty array to keep triplets
        res = []

        # run loop to find triplets
        for index, num in enumerate(nums_sorted):
            if index > 0 and num == nums_sorted[index - 1]:
                continue
            j = index + 1
            k = len(nums_sorted) - 1
            while j < k:
                if -num < (nums_sorted[j] + nums_sorted[k]):
                    k -= 1
                elif -num > (nums_sorted[j] + nums_sorted[k]):
                    j += 1
                else:
                    res.append([num, nums_sorted[j], nums_sorted[k]])
                    j += 1
                    while j < k and nums_sorted[j] == nums_sorted[j - 1]:
                        j += 1
        
        return res
