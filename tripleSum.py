

def tripleSum (arr, targetSum):

    alen = len(arr)
    arr.sort()
    res = []
    for i in range ( alen):
        start = i+1
        end = alen-1
        while start < end:
            currentSum = arr[i] + arr[start] + arr[end]
            if currentSum == targetSum:
                res.append([arr[i] , arr[start] , arr[end]])
                start +=1
                end   -=1
            elif currentSum < targetSum:
                start +=1
            else:
                end -= 1
    return res

def main():
    arr = [1, 9, 15, 4, 6, 5, 7, 8, 2, 3]
    targetSum = 18
    res = tripleSum(arr, targetSum)
    print (res)


if __name__ == "__main__":
    main()
