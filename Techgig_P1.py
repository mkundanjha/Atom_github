T=int(input())
min=100001
diff=[]
for testcase in range(T):
    N=int(input())
    arrV=[int(i) for i in input().split()] # Strenghth of Villan
    arrP=[int(i) for i in input().split()] # Engergy of Player
    for i in range(len(arrP)):
        for j in range(len(arrV)):
            sub=arrP[i]-arrV[j]
            if(sub>0 and sub<min):
                min=sub
                ind=j
        diff.append(arrV[ind])
        
        arrV.remove(arrV[ind])
    answ=[]
    for i in range(len(arrP)):
        sub=arrP[i]-diff[i]
        answ.append(sub)

    c=0
    for i in answ:
        if i<0:
            c=c+1
    if c>0:
        print("LOSE")
    else:
        print("WIN")
    min=100001
    diff=[]



