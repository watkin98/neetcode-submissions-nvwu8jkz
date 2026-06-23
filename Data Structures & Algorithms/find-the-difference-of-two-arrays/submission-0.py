class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)

        distinctInts1 = []
        distinctInts2 = []

        for num in nums1Set:
            if num not in nums2Set:
                distinctInts1.append(num)

        for num in nums2Set:
            if num not in nums1Set:
                distinctInts2.append(num)


        return [distinctInts1, distinctInts2]