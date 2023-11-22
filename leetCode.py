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