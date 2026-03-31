class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            delimitedStr = s + "*,"
            encodedString += delimitedStr

        return encodedString
    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        newStr = ""
        print(f"s: {s}")

        i = 0
        while i < len(s):
            print(f"i: {i}")
            if s[i] == '*':
                if s[i+1] == ',':
                    print(f"newStr: {newStr}")
                    decodedStrings.append(newStr)
                    newStr = ""
                    print(f"Remainder: {s[i:]}")
                    print(f"i b4: {i}")
                    i += 2
                    print(f"i aftr: {i}\nRemainder: {s[i:]}")
                    continue
                else:
                    newStr += s[i]
                    i += 1
                    continue
            else:
                print("000")
                newStr += s[i]

            i += 1

        return decodedStrings
