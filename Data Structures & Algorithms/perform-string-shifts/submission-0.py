class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for instruction in shift:
            print(f"instruction direction: {instruction[0]}")
            if instruction[0] == 0:
                # shift left
                for _ in range(instruction[1]):
                    temp = s[0]
                    s = s[1:]
                    s += temp
            else:
                # shift right
                for _ in range(instruction[1]):
                    temp = s[-1]
                    s = s[:len(s)-1]
                    s = temp + s

        return s