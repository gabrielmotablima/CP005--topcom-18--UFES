def inputs():
    n = int(input())
    len_values = []
    values = []
    for i in range(n):
        value = list(map(int, input().split()))
        len_values.append(value[0])
        values.append(value[1:])
        
    return values, len_values

def solve(values, len_values):
    minimum = len_values.index(min(len_values))
    count = 0
    tmp = 0
    for i in values[minimum]:
        for j in range(len(values)):
            if i in values[j]:
                count += 1
        if count == len(values):
            tmp += 1
        count = 0
            
    return tmp

if __name__ == "__main__":
    values, len_values = inputs()
    result = solve(values, len_values)
    if result != 0:
        print(str(solve(values, len_values)) + " amigos em comum!")
    else:
        print("IMPOSSIVEL!")
    