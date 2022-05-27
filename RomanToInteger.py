def romanToInt(self, s: str) -> int:
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    a = 0
    l = len(s)
    for i in range(l-1):
        if (val[s[i]] >= val[s[i+1]]):
            a = a + val[s[i]]
        elif (val[s[i]]<val[s[i+1]]):
            a = a - val[s[i]]
    a = a + val[s[l-1]]
    return a