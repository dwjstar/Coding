import copy
def solveNQueens(n):
    res=[]
    queens=[['.']*n for i in range(n)]
    def NQueens(x):
        if x==n:
            mymatrix=copy.deepcopy(queens)
            mymatrix=[''.join(i) for i in mymatrix]
            res.append(mymatrix)
            return
        for i in range(n):
            if _place(x,i):
                queens[x][i]='Q'
                NQueens(x+1)
                queens[x][i]='.'
        return



    def _place(row,col):

        for i in range(row):
            if queens[i][col]=='Q':
                return False
        i,j=row-1,col-1
        while i>=0 and j>=0:
            if queens[i][j]=='Q':
                return False
            i,j=i-1,j-1
        i,j=row-1,col+1
        while i>=0 and j<n:
            if queens[i][j]=='Q':
                return False
            i,j=i-1,j+1
        return True

    NQueens(0)
    return res
if __name__=='__main__':
    res=solveNQueens(4)
    print(res)