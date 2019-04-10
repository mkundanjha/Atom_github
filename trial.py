import math
# Getting the test case
T=int(input())
ls=[]

# Running for the test case
for i in range(0,T):
    (N, L) = map(int, input().split(' ')) # Stores the value of N and L in arr1
    arr2 = [int(i) for i in input().split()] # Stores the input L values in arr2
    if(len(arr2)>N):
        break;
    arr3=[]
    Gcd=math.gcd(arr2[0],arr2[1])
    arr3.append(int(arr2[0]/Gcd))
    arr3.append(Gcd)
    k=len(arr2)

    for i in range(1,k):
        Gcd=int(arr2[i]/Gcd)
        arr3.append(Gcd)

    arr4=[]
    for i in arr3:
        arr4.append(i)

    arr3.sort()

    arr3= list(dict.fromkeys(arr3))

    alphabet = []
    for letter in range(65,91):
        alphabet.append(chr(letter))


    w=''
    for element  in arr4:
        j=(alphabet[arr3.index(element)])
        w=w+j # Getting the string
    #print(w)
    ls.append(w)


for element in ls:
    print(element)
