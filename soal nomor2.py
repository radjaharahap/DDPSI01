j = 0
for i in range (1,20,2):
    if i !=19:
        print(i, end="+")
    else:
        print(i, end="")
    j += i
    print("=",j)