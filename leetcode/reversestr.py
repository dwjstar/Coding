def reverseString(s):
    if not s or len(s)==1:

        return
    s[0],s[-1]=s[-1],s[0]
    return reverseString()

if __name__=='__main__':
    s=["h","e","l","l","o"]
    reverseString(s)
    print(s)