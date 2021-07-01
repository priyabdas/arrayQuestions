

def tripleSum (arr, targetSum):
    alen = len(arr)
    arr.sort()
    for i in range (alen):
        start = i+1
        end = alen-1
        while start < end:
            currentSum = arr[i] + arr[start] + arr[end]
            if currentSum == targetSum:
                start +=1
                end   -=1
                print (arr[i] , arr[start] , arr[end])
            elif currentSum < targetSum:
                start +=1
            else:
                end -= 1


def main():
    arr = [1, 9, 15, 4, 6, 5, 7, 8, 2, 3]
    targetSum = 18
    tripleSum(arr, targetSum)

if __name__ == "__main__":
    main()
