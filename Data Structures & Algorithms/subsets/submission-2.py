class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = []

        # Contract Helper: takes in index of the array and decides whether to include the item at that index in the subset
        #                  for the current call. Returns nothing.
        def dfs(i):
            if i >= len(nums):
                res.append(s.copy())
                return

            
            # print(f"i: {i}")
            # print(f"res: {res}")
            # print(f"s: {s}\n")
            s.append(nums[i])
            dfs(i+1)
            # print(f"i: {i}")
            # print(f"res: {res}")
            # print(f"s: {s}\n")

            s.pop()
            dfs(i+1)
            # print(f"i: {i}")
            # print(f"res: {res}")
            # print(f"s: {s}\n\n")

        dfs(0)
            
        return res