from typing import List
import random

class Solution:
    # 88. Merge Sorted Array
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # pointers
        p1, p2, p = m-1, n-1, m+n-1

        # initial merge
        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -=1
            else:
                nums1[p] = nums2[p2]
                p2 -=1
            p -=1
        
        # dump remaining p2
        while p2>=0:
            nums1[p] = nums2[p2]
            p2 -=1
            p -=1
    

    # 27. Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        startLength = len(nums)
        for i in range(len(nums)):
            while(nums[i] == val):
                nums.pop(i)
                nums.append('a')
                startLength -= 1
        return startLength
    
    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: List[int]) -> int:
        startLength = len(nums)
        for i in range(startLength-1):
            while (nums[i]==nums[i+1]):
                nums.pop(i)
                nums.append(random.random())
                startLength -=1
        return startLength
    
    # 169. Majority Element
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        max_num = 0
        max_count = 0
        for i in nums:
            hash[i] = hash.get(i,0) + 1
            if hash[i] > max_count:
                max_num = i
                max_count = hash[i]
        
        return max_num
    
    # 189. Rotate Array
    def rotate(self, nums: List[int], k: int) -> None:
        end = len(nums)-1
        while k>0:
            # rotate
            nums.insert(0,nums.pop(end))
            k -=1
        
    # 121. Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = prices[0]
        profit = 0
        for todays_price in prices:
            if todays_price > max_price:
                max_price = todays_price
                profit = max(profit, max_price - min_price)
            elif todays_price < min_price:
                min_price = todays_price
                max_price = todays_price
        return profit
    
    # 122. Best Time to Buy and Sell Stock II
    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0    
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit