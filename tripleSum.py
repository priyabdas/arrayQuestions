
 # triple Sum
 #  Given an array of numbers find a pair in the array who's sum is the target
 #
 #  inputs array = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 15 ] , targetSum = 18
 #  output
 #    [1, 2, 15 ]
 #    [3, 7, 8  ]
 #    [5, 6, 7  ]
 #
 #  Created by Priyabrata Das on 07/06/21
 #


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
