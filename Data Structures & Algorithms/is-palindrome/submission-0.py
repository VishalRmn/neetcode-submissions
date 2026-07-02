class Solution:
    def isPalindrome(self, s: str) -> bool:

        #remove all unnecessary characters
        s_clean = "".join(char.lower() for char in s if char.isalnum())
        print(s_clean)
        
        s_list = list(s_clean)
        l = 0
        r = len(s_list) - 1
        while l<r:
            if s_list[l] != s_list[r]:
                return False
            else:
                l += 1
                r -= 1
        return True