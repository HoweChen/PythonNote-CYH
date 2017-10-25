import createRandomNumberList

randomNumberList = createRandomNumberList.main()


def selectionSort(randomNumberList):
    minNumber = randomNumberList[0]
    result = []
    while len(randomNumberList) != 0:
        minNumberIndex = 0
        for i in range(len(randomNumberList)):
            if randomNumberList[i] < minNumber:
                minNumber = randomNumberList[i]
                minNumberIndex = i
        result.append(randomNumberList.pop(minNumberIndex))

    return result


def main():
    result = selectionSort(randomNumberList)
    print(result)


if __name__ == '__main__':
    main()
