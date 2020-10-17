def uniquePathsIII(grid) -> int:
    if not grid:
        return
    n = len(grid)
    if not grid[0]:
        return
    m = len(grid[0])
    cnt = 0
    cnt_0=0
    res_0=0
    visited = [[False] * m for _ in range(n)]
    direciton = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def isPath(i, j):
        if i < 0 or j < 0:
            return False
        if i >=n or j >= m:
            return False
        if visited[i][j]:
            return False
        if grid[i][j] == -1:
            return False
        return True

    def find_path(i, j):
        nonlocal cnt_0
        if grid[i][j] == 2 and cnt_0==res_0:
            nonlocal cnt
            cnt += 1
            return
        for d in direciton:
            if isPath(i + d[0], j + d[1]):
                visited[i + d[0]][j + d[1]] = True
                cnt_0+=1
                find_path(i + d[0], j + d[1])
                visited[i + d[0]][j + d[1]] = False
                cnt_0-=1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                row = i
                col = j
                res_0+=1
            if grid[i][j]==0:
                res_0+=1
    print(res_0)
    visited[row][col]=True
    find_path(row, col)
    return cnt

if __name__=='__main__':
    grid=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    cnt=uniquePathsIII(grid)
    print(cnt)