n = input("PLease enter a number for which u want a pattern[don't enter less then 3]: ")
n=int(n)
for i in range(1,n):
    for j in range(1,i):
        print("* ", end="")
    for k in range(i,n-1):
        print(end="    ")
    for j in range(1,i):
        print("* ",end="")
    print("\r")    