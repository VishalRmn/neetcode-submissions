class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize set for lookups - contains all chars in the current substring
        charSet = set()

        # init max length variable
        res = 0

        # init sliding window
        l = 0
        # right pointer starts at first position, goes all the way to the right of the string, one char at a time
        for r in range(len(s)):
            # if current char (s[r]) is already in the set, shrink the window from the left until the duplicate char has been removed
            # Also remove the characters in the set which are being removed from the substring
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            # add the current char to the set
            charSet.add(s[r])
            # after all duplicates have been removed from current substring, and new ones have been added to the substring,
            # check the current length against the max length so far
            res = max(res, r-l+1)
        return res 




        