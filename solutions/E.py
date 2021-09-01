if __name__ == "__main__":
    row = input().split(" ")
    dict_v = {}
    for i in range(int(row[1])):
        value = input()
        dict_v[value] = 1
    
    result = 1
    
    for i in range(int(row[2])):
        value = input()
        if (result == 1) and (value in dict_v.keys()):
            result = 0
    
    print(result)