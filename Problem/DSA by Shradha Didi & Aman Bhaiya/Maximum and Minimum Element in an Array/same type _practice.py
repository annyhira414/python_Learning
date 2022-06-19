class pair:
    def __int__(self):
        self.min = 0
        self.max = 0


def getMinMax(arr: list, n: int) -> pair():
    minmax = pair()

    if n == 1:
        minmax.min = arr[0]  # dekha lagse aage code
        minmax.max = arr[0]
        # return minmax

    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]  # dekha lagse ami ai line tai dey nai . mone chilo na
    else:
        minmax.min = arr[0]
        minmax.max = arr[1]

    # return minmax

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax  # aita vul korchilam tai amr max number 200 dekhytechilo cz loop ta kaj kore nai .


if __name__ == "__main__":
    arr = [200, 6, 1, 5000]
    arr_Size = 4
    minmax = getMinMax(arr, arr_Size)  # dekha lagse aage code
    print("the min number", minmax.min)
    print("then max number", minmax.max)
