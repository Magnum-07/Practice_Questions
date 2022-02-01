def longestPalin(self, S):
    # code here
    res = ""
    resLen = 0
    length = len(S)
    for i in range(length):
        # odd length check
        l,r = i,i
        while l >= 0 and r < length and S[l] == S[r]:
            if r - l + 1 > resLen:
                res = S[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
        
        # even length check
        l,r = i, i + 1
        while l >= 0 and r < length and S[l] == S[r]:
            if r - l + 1 > resLen:
                res = S[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res