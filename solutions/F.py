def main():
    counter = int(input())
    results = []
    for expressionInput in range(counter):
        expressionInput = input()
        expressionInputList = expressionInput.split()
        indexes = []
        for index in range(len(expressionInputList)):
            if expressionInputList[index] == 'not':
                indexes.append(index)
        for index in indexes:
            expressionInputList[index+1] = "~" + str(expressionInputList[index+1])
        if (expressionInputList.__contains__("A") and expressionInputList.__contains__("~A")) or (expressionInputList.__contains__("B") and expressionInputList.__contains__("~B")) or (expressionInputList.__contains__("C") and expressionInputList.__contains__("~C")) or (expressionInputList.__contains__("D") and expressionInputList.__contains__("~D")) or (expressionInputList.__contains__("E") and expressionInputList.__contains__("~E")) or (expressionInputList.__contains__("F") and expressionInputList.__contains__("~F")) or (expressionInputList.__contains__("G") and expressionInputList.__contains__("~G")) or (expressionInputList.__contains__("H") and expressionInputList.__contains__("~H")):
            results.append("trivialmente falsa")
        else:
            results.append("nem trivialmente verdadeira, nem trivialmente falsa")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()