from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            cnt = ''.join(sorted(word))
            if cnt in map.keys():
                map[cnt].append(word)
            else:
                map[cnt] = [word]
        #print(map)
        return map.values()
        