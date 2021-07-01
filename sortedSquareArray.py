# Given an array of sorted intergers
# print the result array of their squares

def sortedSquaredArray(array):

    res = [0 for i in range (len(array))]

    left = 0
    right = len(array)-1
    for idx in reversed(range(len(array))):
        small = array[left]
        big   = array[right]


        if (abs(small) > abs(big)):
            res[idx] = small*small
            left += 1
        else:
            res[idx] = big*big
            right -=1


    return res

def main():
    arr = [-10,-7,1, 2, 3, 5, 6, 8, 9]
    res = sortedSquaredArray(arr)
    print (res)


if __name__ == "__main__":
    main()
