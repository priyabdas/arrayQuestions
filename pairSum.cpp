/* Pair Sum
 *  Given an array of numbers find a pair in the array who's sum is the target
 *
 *  inputs array = [ 2, 45 , 3, 32 , 12 ] , targetSum = 34
 *  output [2,32]
 *
 *  Created by Priyabrata Das on 07/06/21
 */



#include <iostream>
#include <vector>
#include <unordered_map>
#include <utility>


using namespace std ;

vector <int > pairSum(vector <int> &arr , int targetSum){

    unordered_map <int,int> map ;
    int diff = 0 ;
    for (int i = 0 ; i < arr.size() ; i++){
        diff = targetSum - arr[i] ;
        //check if the difference in the hash map
        if (map.find(diff) != map.end()){
            //found the diff number in map untill map end
            return {arr[i], diff };
        } else {
            // insert the number into the array
            map[ arr[i] ] = i;
        }

    }
    return {} ; // else return empty pair

}


int main (){
    vector <int> arr = {2, 45 , 3, 32 , 12 };
    int targetSum = 34 ;


    vector <int> res = pairSum(arr, targetSum);

    for (auto x : res){
        cout << x << endl;
    }


}
