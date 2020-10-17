
def longestCommonPrefix( strs) :
    strs_len = len(strs)
    if strs_len == 1:
        return strs[0]
    if strs_len == 0:
        return ""
    max_substr = ""
    min_len = len(strs[0])
    min_str = strs[0]
    for str_ in strs:
        if len(str_) < min_len:
            min_len = len(str_)
            min_str = str_
    strs.remove(min_str)
    flag = 1
    for i in range(min_len):
        for str_ in strs:
            if str_[i] != min_str[i]:
                flag = 0
                break
        if flag == 0:
            break
        j=i
    return min_str[:j+1]

if __name__=='__main__':
    strs=["flower","flow","flight"]
    print(longestCommonPrefix(strs))