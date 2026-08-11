class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        for i, string in enumerate(strs):
            forward = string
            reverse = string[::-1]
            
            for j in range(0, len(string)):
                if forward[j] == reverse[j]:
                    continue
                elif forward[j] > reverse[j]:
                    strs[i] = forward
                    break
                else:
                    strs[i] = reverse
                    break

        res = "".join(strs)
        smallestChar = 26
        smallestCharIndex = 0

        for i, char in enumerate(res):
            charVal = ord(char) - ord('a')
            if charVal < smallestChar:
                smallestChar = ord(char) - ord('a')
                smallestCharIndex = i
        # print(f"sci: {smallestCharIndex}")
        # print(res)
        # print(1)
        # print(res[i+1:])
        # print(2)
        # print(res[:i+1])
        #print(smallestCharIndex)

        return res[smallestCharIndex+1:] + res[:smallestCharIndex+1]
