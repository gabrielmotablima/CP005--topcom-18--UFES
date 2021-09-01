def inputs():
    N_M = list(map(int, input().split(" ")))
    values = list(map(int, input().split(" ")))
    sales = []
    for i in range(N_M[0]):
        sales.append(list(map(int, input().split(" "))))
    
    return N_M, values, sales
    
def comb(val):
    combin = 0
    for i in range(1, val+1):
        combin+=i
    return combin
    
def solve(N_M, values, sales):
    result = []
    for i in range(N_M[0]):
        combin = comb(sales[i][1])
        money = sales[i][0]
        for j in range(sales[i][1], N_M[1]):
            if money >= values[j]:
                money-=values[j]
                combin+=(j+1)
            else:
                break
        result.append(combin)
    
    return result

def outputs(N, result):
    string = ""
    for i in range(N):
        string += f"{result[i]} "
    print(string[:-1])
    

if __name__ == "__main__":
    N_M, values, sales = inputs()
    outputs(N_M[0] ,solve(N_M, values, sales))