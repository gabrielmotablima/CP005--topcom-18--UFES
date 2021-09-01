def main():
    numTeste = int(input())
    
    numCol = []
    for a in range(0, numTeste, 1):
        j = int(input())

        i = 1
        while (j > 0):
            j = j - i
            i = i + 1
        
        
        if (j == 0):
            numCol.append(i)
        else:
            numCol.append(i-1)
    
    for n in numCol:
        print(n)

if __name__ == '__main__':
    main()