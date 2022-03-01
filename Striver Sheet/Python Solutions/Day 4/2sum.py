# question_link -> https://leetcode.com/problems/two-sum/

# The famous 2sum problem with a solution , T.C.->O(N) AND S.C.-> O(N)
def solution(nums, target):
    d = dict()
    for i in range(len(nums)):
        val = target - nums[i]
        if nums[i] in d:
            return [d[nums[i]], i]
        else:
            d[val] = i
            

# taking the nums and  target as input.
#main function  
def main():
    nums = list(map(int, input().split()))
    target = int(input())
    solution(nums, target)
