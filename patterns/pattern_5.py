n = input("PLease enter a number for which u want a pattern[don't enter less then 3]: ")
n=int(n)
for i in range(1,n):
    for k in range(1,i):
        print(end="  ")
    for j in range(i,n):
        print("* ",end="")
    for j in range(i+1,n):
        print("* ",end="")
    print("\r")     
    