class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []

        for num1 in nums1:
            for i, num2 in enumerate(nums2):
                if num2 == num1:
                    mapping.append(i)
                    break
                
        return mapping
        