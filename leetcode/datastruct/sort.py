def select_sort(lis):
    len_lis = len(lis)
    if len_lis < 2:
        return lis
    for i in range(0,len_lis-1):
        min=lis[i]
        k=i
        for j in range(i+1,len_lis):
            if min>lis[j]:
                min=lis[j]
                k=j
        lis[i],lis[k]=lis[k],lis[i]
    return lis

def bub_sort(lis):
    '''
    冒泡排序
    :param lis:
    :return:
    '''
    len_lis=len(lis)
    if len_lis <2:
        return lis
    flag=1
    for i in range(1,len_lis):
        for j in range(len_lis-i):
            if lis[j]>lis[j+1]:
                tem=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=tem
                flag=0
        if flag==1:
            break
    return lis

def inser_sort(lis):
    '''
    插入排序
    :param lis:
    :return:
    '''
    len_lis = len(lis)
    if len_lis < 2:
        return lis
    for i in range(1,len_lis):
        tem=lis[i]
        j=i-1
        while j >=0 and tem<lis[j]:
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=tem

    return lis

def shell_sort(lis):
    len_lis = len(lis)
    if len_lis < 2:
        return lis
    step=int(len_lis/2)
    while step>0:
        for i in range(step,len_lis):
            j=i
            temp=lis[i]
            while j - step >= 0 and lis[j - step] > temp:
                lis[j] = lis[j - step]
                j -= step
            lis[j] = temp
        step=int(step/2)
    return lis



def quick_sort(lis,start,end):
    '''
    快排
    :param lis:
    :param start:
    :param end:
    :return:
    '''
    len_lis = len(lis)
    if len_lis < 2:
        return lis
    if start<end:
        m=patition_(lis,start,end)
        quick_sort(lis,start,m-1)
        quick_sort(lis,m+1,end)
    return lis

def quick_nonre(lis):
    len_lis=len(lis)
    if len_lis<2:
        return lis
    stack=[0,len_lis-1]
    while stack:
        r=stack.pop()
        l=stack.pop()
        mid=patition_(lis,l,r)

        if l<mid-1:
            stack.append(l)
            stack.append(mid-1)
        if r>mid+1:
            stack.append(mid+1)
            stack.append(r)
    return lis
def patition_(lis,start,end):
    key=lis[start]
    while start<end:
        while start<end and lis[end]>=key:
            end-=1
        lis[start]=lis[end]
        while start<end and lis[start]<=key:
            start+=1
        lis[end]=lis[start]
        lis[start]=key
    return start



if __name__=='__main__':
    lis=[7,4,1,3,2,6,5,3,3]
    lis2=[7,6,5,4,3,2,1]
    lis3=[1]
    li=[1332802,1177178,1514891,871248,753214,123866,1615405,328656,1540395,968891,1884022,252932,1034406,1455178,821713,486232,860175,1896237,852300,566715,1285209,1845742,883142,259266,520911,1844960,218188,1528217,332380,261485,1111670,16920,1249664,1199799,1959818,1546744,1904944,51047,1176397,190970,48715,349690,673887,1648782,1010556,1165786,937247,986578,798663]

    # print(bub_sort(lis2))
    # print(inser_sort(lis))
    # print(quick_sort(lis,0,len(lis)-1))
    # print(select_sort(lis))
    # print(shell_sort(lis2))
    print(quick_nonre(li))
    print(sorted(li))