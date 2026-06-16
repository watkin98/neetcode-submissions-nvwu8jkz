class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #mapping = defaultdict(list)
        res = []

        for num1 in nums1:
            for i, num2 in enumerate(nums2):
                # if num2 in mapping and i in mapping[num2]:
                #     print(2)
                #     mapping[num2].append(i)
                if num2 == num1:
                    #print(1)
                    res.append(i)
                    break

        # print(mapping.items())
        # res = []
        # for item in mapping.values():
        #     res = res + item
        #print(res)
        return res