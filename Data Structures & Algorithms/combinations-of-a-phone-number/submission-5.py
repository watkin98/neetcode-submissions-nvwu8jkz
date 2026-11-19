class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {'2' : ['a','b','c'], '3' : ['d','e','f'], '4' : ['g','h','i'], 
                    '5' : ['j','k','l'], '6' : ['m','n','o'], '7' : ['p','q','r','s'], 
                    '8' : ['t','u','v'], '9' : ['w','x','y','z']}
        res = []

        def explore(i, comb):
            if i == len(digits):
                res.append(''.join(comb))
                return comb

            for char in mappings[digits[i]]:
                comb.append(char)
                comb = explore(i+1, comb)
                comb.pop()
            
            return comb

        call = explore(0, [])
        return res if res != [''] else []