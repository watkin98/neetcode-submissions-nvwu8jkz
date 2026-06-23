class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for num1 in nums1:
            for i in range(len(nums2)):
                if nums2[i] == num1:
                    res.append(i)
                    break

        return res