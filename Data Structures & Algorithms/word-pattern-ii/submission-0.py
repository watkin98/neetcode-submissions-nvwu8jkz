class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pd = {}
        md = {}
        for i, c in enumerate(pattern):
            # this is more efficient beacuse it doesnt require sorting and will not be changed
            pd.setdefault(c, []).append(i)

        def combinate(pattern: str, subcombination: str, minOrd: str):
            if len(set(pattern)) == 1:
                nsplice = len(pd[pattern[-1]])
                lsplice = len(subcombination) // nsplice
                t = 0
                comp = subcombination[t + lsplice]
                for i in range(1, nsplice):
                    if subcombination[t + i*lsplice:t+i*lsplice + 1] == comp:
                        return True
            for rp, rc in enumerate(s):
                for lp in range(len(s[0:rp]) - 1, -1, -1):
                    if s[lp:rp] in md:
                        md.setdefault(s[lp:rp], []).append(lp)
                        # if not the first character contained, wait. if not equal occurences of pattern A to counts of A, wait.
                        good = True
                        if 0 in md[s[lp:rp]] and len(md[s[lp:rp]]) == len(pd[minOrd]):
                            # now we check pattern ie is a->a or a->b
                            for idx, p_idx in enumerate(pd[minOrd]):
                                # if pattern no match.
                                if (idx + 1 < len(pd[minOrd]) 
                                    and ((pd[minOrd][idx] != pd[minOrd][idx + 1] - 1
                                    and md[s[lp:rp]][idx] == md[s[lp:rp]][idx + 1] - len(s[lp:rp]))
                                    or (pd[minOrd][idx] == pd[minOrd][idx + 1] - 1
                                    and md[s[lp:rp]][idx] != md[s[lp:rp]][idx + 1] - len(s[lp:rp])))):
                                    good = False
                            if good:
                                return combinate(pattern.replace(minOrd, ''), subcombination.replace(s[lp:rp], ''), chr(ord(minOrd)+ 1))         
                                
                    else:
                        md.setdefault(s[lp:rp], []).append(lp)
            return False

        return combinate(pattern, s, 'a')