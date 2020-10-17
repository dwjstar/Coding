def isMatch(s,p):
    if not p:
        return not s
    match=bool(s and (p[0]==s[0] or p[0]=='.'))
    if len(p)>1 and p[1]=='*':
        return isMatch(s,p[2:]) or match and isMatch(s[1:],p)
    else:
        return match and isMatch(s[1:],p[1:])

def isMatch_(s,p):
    s_len=len(s)
    p_len=len(p)
    dp=[[False]*s_len for _ in range(p_len)]
    
    for i in range(s_len):
        for j in range(p_len):
            if s[0]==p[0] or p[0]=='.':
                dp[0][0]=True
                dp[i][j]=dp[i-1][j-1]

