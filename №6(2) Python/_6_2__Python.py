
def sum(): 
    a = list(map(int, input('Enter your numbers: ').split()))
    print("Начальний список: ", a)

    s = 0

    for i in range(len(a)): 
        s += a[i]

    print("Сума: ",s)
sum()
