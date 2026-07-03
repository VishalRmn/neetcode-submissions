class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init set for lookups
        charSet = set()

        # init res
        res = 0

        # init sliding window
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res


        