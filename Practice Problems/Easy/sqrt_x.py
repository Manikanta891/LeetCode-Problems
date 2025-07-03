# import math
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return math.floor(x**(1/2))

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         num=0
#         while num*num<=x:
#             num+=1
#         return num-1

# class Solution:
#     def binary_search(self,start: int, end: int, x: int) -> int:
#         mid=(start+end)//2
#         if start<end:
#             if mid==x//mid:
#                 return mid
#             elif mid*mid>x:
#                 return self.binary_search(start,mid-1,x)
#             else:
#                 return self.binary_search(mid+1,end,x)

#     def mySqrt(self, x: int) -> int:
#         return self.binary_search(1,x,x)


#For 8 it still move towards 2 and 3 but then start>end and returns end which is 2
class Solution:
    def binary_search(self, start, end, x):
        if start > end:
            return end  

        mid = (start + end) // 2

        if mid * mid == x:
            return mid
        elif mid * mid > x:
            return self.binary_search(start, mid - 1, x)
        else:
            return self.binary_search(mid + 1, end, x)

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # sqrt(0) = 0, sqrt(1) = 1
        return self.binary_search(1, x, x)
