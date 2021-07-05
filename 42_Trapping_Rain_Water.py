def trap_rain_water(array):
    #left = 0
    #right = len(array)-1
    maxLeft = array[0]
    maxRight = array[len(array)-1]
    res = 0

    leftArray = [array[0] for i in range(len(array))]
    rightArray = [array[len(array)-1] for i in range(len(array))]

    #build the left array heights
    for x in range(1,len(array)):
        if array[x] > maxLeft:
            maxLeft = array[x]
        leftArray[x] = maxLeft

    #build the right array heights
    for x in reversed(range(0,len(array)-1)):
        if array[x] > maxRight:
            maxRight = array[x]
        rightArray[x] = maxRight

    #print(leftArray)
    #print(rightArray)

    for idx in range (len(array)):
        res += min(leftArray[idx] ,rightArray[idx])-array[idx]

    return (res)

def main():
    #arr = [5,3,2,1,2,3,5 ]
    arr = [4,2,0,3,2,5]
    res = trap_rain_water(arr)
    print (res)


if __name__ == "__main__":
    main()
