def partition(s: str) :
    len_s = len(s)
    res = []

    def is_H(str_):
        len_ = len(str_)
        if len_ == 1:
            return True
        l, r = 0, len_ - 1
        while l < r:
            if str_[l] != str_[r]:
                return False
            l += 1
            r -= 1
        return True

    def back(start, temp_str):
        if start == len_s:
            res.append(temp_str)
            return
        for i in range(start, len_s):
            if is_H(s[start:i + 1]):
                back(i + 1, temp_str + [s[start:i + 1]])

    back(0, [])
    return res

if __name__=='__main__':
    s='aab'
    res=partition(s)
    print(res)