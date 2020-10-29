def partitionLabels(S):
    apha = {}
    res = []
    s_len = len(S)
    for i in range(s_len):
        if S[i] not in apha:
            apha[S[i]] = []
        apha[S[i]].append(i)
    l = 0
    j = 0
    while l < s_len:
        r = apha[S[l]][-1]
        j = l + 1
        while j < r:
            if apha[S[j]][-1] > r:
                r = apha[S[j]][-1]
            j += 1
        cnt = len(S[l:r + 1])
        res.append(cnt)
        l = r + 1
    return res


if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    res = partitionLabels(s)
    print(res)
