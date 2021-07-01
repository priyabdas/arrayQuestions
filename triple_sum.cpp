/*  triple Sum
 *  Given an array of numbers find a pair in the array who's sum is the target
 *
 *  inputs array = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 15 ] , targetSum = 18
 *  output
    [1, 2, 15 ]
    [3, 7, 8  ]
    [5, 6, 7  ]
 *
 *  Created by Priyabrata Das on 07/06/21
 */



#include <iostream>
#include <vector>

using namespace std ;

void tripleSum(vector <int> &arr, int targetSum){
    sort(arr.begin(), arr.end());

    for (int i = 0 ; i < arr.size()-3 ; i++){
        int start = i+1;
        int end = arr.size()-1;

        while (start < end){
            int currentSum = arr[i] + arr[start] + arr[end];

            if (currentSum == targetSum ){
                cout << arr[i] << " " << arr[start] << " " << arr[end] << endl;
                start += 1;
                end -= 1;
            } else if (currentSum < targetSum){
                start += 1;
            } else {
                end -= 1;
            }
        }
    }
}



int main (){
    vector <int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 15 };
    int targetSum = 18 ;


    tripleSum(arr, targetSum);

}
