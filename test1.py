T=int(input())
list=[]
for i in range(0,T):
    arr=[int(i) for i in input().split()]
    sum=arr[0]+arr[1]
    list.append(sum)
for i in list:
    print(i)
print("hello")
