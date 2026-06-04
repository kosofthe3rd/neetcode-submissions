class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        temp = s[0]
        count = 1

        while r < len(s):
            if s[r] not in temp:
                temp += s[r]
                count = max(count, len(temp))
            else:
                while s[r] in temp:
                    l += 1
                    temp = temp[1:]
                    print(temp)
                temp += s[r]
            r += 1
        return count


        