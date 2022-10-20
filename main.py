class Solution:
    def countSubarrays(self, nums, minK, maxK):
        def ct(minK, maxK):
            ans, c = 0, 0
            for k in nums:
                if k > maxK or k < minK:
                    ans += c * (c - 1) // 2 + c
                    c = 0
                else:
                    c += 1
            ans += c * (c - 1) // 2 + c
            return ans

        if minK > maxK:
            return 0

        ans = ct(minK, maxK)
        ans -= ct(minK + 1, maxK)

        if minK != maxK:
            ans -= ct(minK, maxK - 1)
            ans += ct(minK + 1, maxK - 1)

        return ans


s = Solution()
print(s.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
print(s.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))
