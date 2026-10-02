class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))