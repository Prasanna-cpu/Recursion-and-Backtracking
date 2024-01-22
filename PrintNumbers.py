

def PrintNumbers(N):
    if N==0:
        return
    print(f'Value:{N}')
    PrintNumbers(N-1)


PrintNumbers(10)