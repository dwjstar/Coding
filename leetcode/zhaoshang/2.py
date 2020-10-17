while True:
    try:
        n=int(input())
        if n<0:
            n=abs(n)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            if i%2==0:
                dp[i]=min(dp[i-1]+1, dp[int(i/2)]+1)
            else:
                dp[i]=min(dp[i-1]+1, dp[int((i+1)/2)]+2)
        print(dp[n])
    except:
        break