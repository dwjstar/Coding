# import sys
# num=list(map(int,input().split(' ')))
# n,m=num[0],num[1]
# weight=[]
# m_data=[]
# for i in range(n):
#     weight.append(int(input()))
# for i in range(m):
#     col=list(map(int,input().split(' ')))
#     if col[0]==1:
#         weight[col[1]-1]=col[2]
#     if col[0]==2:
#         print(sum(weight[col[1]-1:col[2]]))
#     if col[0] == 3:
#         print(max(weight[col[1] - 1:col[2]]))
# def move_(num):
#     dp=[0]*num
#     dp[1]=1
#     for i in range(2,num):
#         dp[i]=1+max(dp[i-1],dp[i-2])
#     return dp[num-1]
#
# n=int(input())
# for i in range(n):
#     m=int(input())
#     val=move_(m)
#     print(val)


