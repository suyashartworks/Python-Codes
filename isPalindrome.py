def isPalindrome(self, x: int) -> bool:
    s = str(x)
    l = len(s)
    ind = l-1 
    le = int(l / 2)
    
    for i in range(le):
        if (s[i]!=s[ind]):
            return 0
        ind=ind-1
    return 1