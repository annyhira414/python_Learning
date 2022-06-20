class pair:
    def __init__(self):
        self.min = 0
        self.max = 0


def getMinMax(arr: list, n: int) -> pair():
    minmax = pair()

    if n == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax

    if arr[0] > arr[1]:
        minmax.min = arr[1]
        minmax.max = arr[0]
    else:
        minmax.min = arr[0]
        minmax.max = arr[1]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax


if __name__ == "__main__":
    myArray = [100, 7, 899, 34, 89, 200, 50000]
    array_size = 7
    minmax = getMinMax(myArray, array_size)
    print("mim number", minmax.min)
    print("max number", minmax.max)
