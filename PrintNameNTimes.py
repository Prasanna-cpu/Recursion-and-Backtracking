


def PrintName(n,Name):

    i=n
    if i==0:
        return

    print(Name)
    PrintName(n-1,Name)

PrintName(5,"Kumar")



