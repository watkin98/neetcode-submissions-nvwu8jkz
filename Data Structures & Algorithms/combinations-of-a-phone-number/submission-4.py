class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {'2' : ['a','b','c'], '3' : ['d','e','f'], '4' : ['g','h','i'], 
                    '5' : ['j','k','l'], '6' : ['m','n','o'], '7' : ['p','q','r','s'], 
                    '8' : ['t','u','v'], '9' : ['w','x','y','z']}
        res = []
        comb = []

        # Recursive Contract: takes in an index (i) in the string and explores including it and not
        #                     including it in the candidate combination. Returns when the index is greater
        #                     than the string bounds (Null return)
        def explore(i):
            if i == len(digits):
                if comb != []:
                    res.append(''.join(comb))
                return

            
            for char in mappings[digits[i]]:
                comb.append(char)
                explore(i+1)
                comb.pop()

        explore(0)
        return res