def isValid( s):
    # write code here
    flag_dic = {']': '[', ')': '(', '}': '{'}
    stack = []
    stack2 = []
    for c in s:
        flag = False
        if c in flag_dic:
            while stack:
                c_ = stack.pop()
                if c_ == flag_dic[c]:
                    flag = True
                    break
                else:
                    stack2.append(c_)
            while stack2:
                stack.append(stack2.pop())
            if not flag:
                return False
        if not flag:
            stack.append(c)
    if stack:
        return False
    return True

if __name__=='__main__':
    s='([)]'
    a=[1,2,3,4,5,6,7]
    c,d=a
    print(c,d)