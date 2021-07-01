# Given a array of numbers find the peak
# ex array 5,6,1,2,3,4,5,4,3,2,01,2,3,2,4
#peak 9 (1,2,3,4,5,4,3,2,0)

def mounainPeak(array):

    climbSteps = 0

    large =0
    downStep=0
    for idx in range (1,len(array)-1):
        #find the peak i.e prev is smaller and next is smaller
        
        if array[idx-1] < array[idx] and array[idx+1] < array[idx]:
            climbSteps = idx
            count = 0
            #print(array[idx])
            #go to the last smaller element
            while climbSteps >=1 and array[climbSteps-1] < array[idx]:
                print("Down")
                count+=1
                climbSteps-=1
            #travrse up untill less
            while downStep < len(array)-1 and array[idx] > array[idx+1]:
                print("Up")
                idx +=1
                count+=1

            large = max(large,count+1)


    return large

def main():
    arr = [5,6,1,2,3,4,5,4,3,2,0,1,2,3,2,4]
    #arr = [1,2,3,4,5,6,4,2,0,2,4]
    res = mounainPeak(arr)
    print (res)


if __name__ == "__main__":
    main()
