class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter_s1, counter_s2 = [0]*26, [0]*26

        for i in range(len(s1)):
            counter_s1[ord(s1[i]) - ord('a')] += 1
            counter_s2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if counter_s1[i] == counter_s2[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            counter_s2[index] += 1
            if counter_s1[index] == counter_s2[index]:
                matches += 1
            elif counter_s1[index] + 1 == counter_s2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            counter_s2[index] -= 1
            if counter_s1[index] == counter_s2[index]:
                matches += 1
            elif counter_s1[index] - 1 == counter_s2[index]:
                matches -= 1
            l += 1
        return matches == 26
            


        