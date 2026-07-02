class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str_ in strs:
            sorted_str_ = "".join(sorted(str_))
            if sorted_str_ in groups:
                groups[sorted_str_].append(str_)
            else:
                groups[sorted_str_] = [str_]
        return list(groups.values())
