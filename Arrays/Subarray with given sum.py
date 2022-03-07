#User function Template for python3
#G4G Link: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1#

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
      currSum=arr[0]
      start=0
      end=0
      lst=[]
      while(start<n):
            if currSum<s and end<n:
                end+=1
                currSum+=arr[end]
            elif currSum>s:
                currSum=currSum-arr[start]
                start+=1
                
            elif currSum == s:
                lst.append(start+1)
                lst.append(end+1)
                return lst
      return -1
                
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
