class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L, R = 0, 1
        numSet = set()
        numSet.add(nums[L])

        while R < len(nums):
            if R - L > k:
                numSet.remove(nums[L])
                L += 1
            if nums[R] in numSet:
                return True
            numSet.add(nums[R])
            R += 1

        return False