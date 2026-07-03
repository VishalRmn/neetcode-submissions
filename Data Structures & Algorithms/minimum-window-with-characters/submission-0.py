class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle the empty string edge case first
        if len(t) == 0 or len(s) == 0:
            return ""

        # Since we need all chars of t in s including dupes, 
        # we keep the chars and freqs of t in a hashmap
        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        # For traversing through the main string, and maintaining the window, we need another hashmap.
        window = {}
        # init result and result length since we need to get min length. result will finally be the substring,
        # so we save first and last index and init with -1.
        # length of substring is kept float infinity so we know by comparing at the end if there is valid result, 
        # because for any valid result it will be less than this.
        res, resLen = [-1, -1] , float("infinity")

        # we also need 2 variables to check whether the substring condition is fulfilled or not
        have, need = 0, len(count_t)
        # lets traverse
        l = 0 #l = left pointer
        for r in range(len(s)): # r = right pointer
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # update have count
            if c in count_t and count_t[c] == window[c]:
                have += 1

            while have == need:
                # condition satisfied, update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # slide left side of window towards right to try to decrease substring length
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""


        
        
        







        