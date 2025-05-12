import math
import random

# This file is a LeetCode practice.
# It is algorithm problems easy.

# 1
# ======================================
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.
# Solution: -------------------
# class Solution(object):
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     index_1 = 0
#     index_2 = 0
#     i = 0
#     j = 0
#     for i in range(len(nums)):
#         for j in range(len(nums)-1):
#             if nums[j] == target - nums[i]:
#                 index_1 = i
#                 index_2 = j
#                 if index_1 == index_2:
#                     index_2 -= 1
#             j += 1
#         i += 1
#     result = [index_2, index_1]
#     return result
 
# '''Test'''    
# test_1 = [2, 7,11,15] # target=9
# test_2 = [3, 2, 4] # target=6
# test_3 = [3, 3] # target=6
# test_4 = [1, 2, 3, 4, 5, 6, 7] # target=10
# test_5 = [2, 5, 5, 11] # target=10
# print(twoSum(test_1, 9))
# print(twoSum(test_2, 6))
# print(twoSum(test_3, 6))
# print(twoSum(test_4, 10))
# print(twoSum(test_5, 10))
# ===================================================

# 2 
# ======================================================
# Given an integer x, return true if x is a 
# palindrome, and false otherwise.
# Solution: ------------------------------
# def isPalindrome(x):
#     """
#     :type x: int
#     :rtype: bool
#     """
#     num_string = str(x)
    
#     num_list = []
#     for char in num_string:
#         num_list.append(char)
   
#     compare_list = []
#     i = len(num_list) - 1
#     while i >= 0:
#         compare_list.append(num_list[i])
#         i -= 1
          
#     if num_list == compare_list:
#         return True
#     else:
#         return False
 
# '''TEST'''
# nums = [
#     12345,
#     12321,
#     11111,
#     1234567,
#     145707541
# ]  
# for num in nums:
#     print(isPalindrome(num)) 
#
# Solution 2 : --------
# def isPalindrome(x):
#     """
#     :type x: int
#     :rtype: bool
#     """
#     num_string = str(x)

#     compare_string = ""
#     i = len(num_string) - 1
#     while i >= 0:
#         compare_string += num_string[i]
#         i -= 1
          
#     if num_string == compare_string:
#         return True
#     else:
#         return False
 
# '''TEST'''
# nums = [
#     12345,
#     12321,
#     11111,
#     1234567,
#     145707541
# ]  
# for num in nums:
#     print(isPalindrome(num)) 
# ===========================================

# 3
# ===========================================
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Solution: -------------
# def romanToInt(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     result = 0
#     i = 0
#     for i in range(len(s)):
#         if s[i] == 'I' and (s[i + 1] != 'V' or s[i + 1] != 'X'):
#             result += 1
#         elif s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
#             result -= 1
#         if s[i] == 'V' and (s[i + 1] != 'X' or s[i + 1] != 'L'):
#             result += 1
#         elif s[i] == 'V' and (s[i + 1] == 'X' or s[i + 1] == 'L'):
#             result -= 1
#     return result
     

# print(romanToInt("VIII"))
# print(romanToInt("IV"))

#        '''FINISH ME'''
# ==================================================================      

# 4
# ================================================================
# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
# Solution: -------------------
# def plusOne(digits):
#     """
#     :type digits: List[int]
#     :rtype: List[int]
#     """
#     digits_int = 0
#     power = 10 ** (len(digits)-1)
#     for num in digits:
#         digits_int += num * power
#         power /= 10
#     target_string = str(int(digits_int) + 1)
#     result =  []
#     for digit in target_string:
#         result.append(int(digit))
#     return result

# '''TEST'''
# print(plusOne([1,2,3,4]))    
# ========================================================