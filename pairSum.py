#Pair Sum
#  Given an array of numbers find a pair in the array who's sum is the target
#
#  inputs array = [ 2, 45 , 3, 32 , 12 ] , targetSum = 34
#  output [2,32]
#
#  Created by Priyabrata Das on 07/06/21
#

def pairSum (arr, targetSum):
    res = []
    foundMap = {}
    for value in arr:
        diff = targetSum - value
        if diff in foundMap:
            return [value, diff]
        foundMap[value] = 1
        

def main():
    arr = [2, 45 , 3, 32 , 12 ]
    targetSum = 34
    res = pairSum(arr, targetSum)
    print (res)


if __name__ == "__main__":
    main()
