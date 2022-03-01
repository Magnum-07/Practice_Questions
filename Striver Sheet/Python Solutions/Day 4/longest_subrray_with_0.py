# question link -> https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

# T.C.-> O(N) AND S.C.-> O(N)
def solution(arr, n):
    
    # using Hashmap 
    max_len = 0
    d = dict()
    c_sum = 0
    for i in range(len(arr)):
        
        c_sum += arr[i]
        
        if arr[i] is 0 and max_len is 0:
            max_len = 1
        
        if c_sum is 0:
            max_len = i + 1
        
        if c_sum in d:
            max_len = max(max_len, i - d[c_sum])
        else:
            d[c_sum] = i
    
    return max_len

# main function 
def main():
    # take arr as an input
    arr = list(map(int, input().split()))
    n = len(arr)
    print(solution(arr,n))

main()