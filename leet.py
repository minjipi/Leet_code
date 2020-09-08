# 1480. Running Sum of 1d Array
# resultArray = []
#
# arr = [1, 2, 3, 4]
#
# for i in range(len(arr)):
#     sum = 0
#
#     for j in range(i + 1):
#         sum += arr[j]
#
#     resultArray.append(sum)
# print(resultArray)

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         resultArray = []
#
#         nums = [1, 2, 3, 4]
#
#         for i in range(len(nums)):
#             sum = 0
#
#             for j in range(i + 1):
#                 sum += nums[j]
#
#             resultArray.append(sum)
#         return resultArray


# 1431. Kids With the Greatest Number of Candies
# candies = [2, 3, 5, 1, 3]
# extraCandies = 3
#
# maxValue = candies[0]
#
# for i in candies:
#     if maxValue < i:
#         maxValue = i
#
# kidsWithCandies=[]
#
# for i in candies:
#     if i+extraCandies >= maxValue:
#         kidsWithCandies.append(True)
#
#     else:kidsWithCandies.append(False)
# print(kidsWithCandies)


# 1470. Shuffle the Array
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         resultArray=[]
#
#         for i in range(n):
#             resultArray.append(i)
#             resultArray.append(n+i)
#
#         return resultArray

# n = 2
# arr = [1, 2, 3, 4]
# resultArray = []
#
# for i in range(n):
#     resultArray.append(arr[i])
#     resultArray.append(arr[n + i])
#
# resultArray


# 1512. Number of Good Pairs
# nums = [1, 2, 3, 1, 1, 3]
# count=0
#
# for i in range(len(nums)):
#
#     for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 count+=1
#
# print(count)


# 1108. Defanging an IP Address

# import math
# from dataclasses import replace
# address = "1.1.1.1"
# a = address.replace(".", "[.]")
# print(a)


# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         Output = address.replace(".", "[.]")
#         return Output


# # 771. Jewels and Stones
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         count = 0
#
#         for i in J:
#             for j in S:
#                 if i == j:
#                     count += 1
#
#         return (count)

# J = "aA"
# S = "aAAbbbb"
# count = 0
#
# for i in J:
#     for j in S:
#         if i==j:
#             count += 1
#
# print(count)


# 1342. Number of Steps to Reduce a Number to Zero
# from math import ceil
#
# num = 14
# count = 0
#
# while num != 0:
#
#     sub = ceil(num % 2)
#     num = ceil(num / 2)
#
#     count += 1
#
#     if sub == 1:
#         count += 1
#         num = num - 1
#
#         if num == 0:
#             count -= 1
#
# print(count)

# 1281. Subtract the Product and Sum of Digits of an Integer
# import math
#
#
# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         Input: n = 234
#
#         product_dig = 1
#         sum_dig = 0
#         nlist = 0
#         while n > 0:
#             mod = math.floor(n % 10)
#             n = math.floor(n / 10)
#             product_dig *= mod
#             sum_dig += mod
#
#         result = product_dig - sum_dig
#         return result


# 1313. Decompress Run-Length Encoded List
# nums = [1, 2, 3, 4]
# output = []
#
# for i in range(len(nums) // 2):
#     for j in range(nums[2 * i]):
#         output.append(nums[2 * i + 1])
# print(output)


# 1389. Create Target Array in the Given Order
# nums = [0, 1, 2, 3, 4]
# index = [0, 1, 2, 2, 1]
#
#
# target = [0] * (len(nums))
# for i in range(len(nums)):
#     for j in reversed(range(index[i], len(nums))):
#         target[j] = target[j - 1]
#     target[index[i]] = nums[i]
# print(target)


# 938. Range Sum of BST

# root = [10, 5, 15, 3, 7, None, 18]
# L = 7
# R = 15
# output = 0

# for i in root:
#     if i != None and i >= L and i <= R:
#         output = output + i
#
# print(output)

# class Solution:
#
#     def visit(self, node: TreeNode, L: int, R: int) -> int:
#         if node is None:
#             return 0
#         output = 0
#
#         if node.val >= L and node.val <= R:
#             output += node.val
#             output += visit(node.left, L, R)
#             output += visit(node.right, L, R)
#         return output
#
#
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         output = 0
#
#         return visit(root, L, R)


# 1295. Find Numbers with Even Number of Digits

# nums = [12, 345, 2, 6, 7896]
# cnt = 0
#
# for i in nums:
#     save = str(i)
#     if len(save) % 2 == 0:
#         cnt += 1
#
# print(cnt)


# 1290. Convert Binary Number in a Linked List to Integer

# head = [1, 0, 1]
# answer = 0
#
# while True:
#
#     answer = 2 * answer
#     answer += head.val
#
#     if head.next == None:
#         break
#
#     head = head.next
#
# print(answer)


# 1534. Count Good Triplets


# count = 0
# arr = [3, 0, 1, 1, 9, 7]
# a = 7
# b = 2
# c = 3
#
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if abs(arr[i] - arr[j]) <= a:
#             for k in range(j + 1, len(arr)):
#                 if abs(arr[j] - arr[k]) <= b:
#                     if abs(arr[i] - arr[k]) <= c:
#                         count += 1
#
# print(count)


# from _ast import List
#
# count = 0
#
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if abs(arr[i] - arr[j]) <= a:
#             for k in range(j + 1, len(arr)):
#                 if abs(arr[j] - arr[k]) <= b:
#                     if abs(arr[i] - arr[k]) <= c:
#                         count += 1
# print(count)

# 1266. Minimum Time Visiting All Points
# points = [[1, 1], [3, 4], [-1, 0]]
# dist = 0
#
# # for i in range(len(points)):  -> 이렇게 하면 안되서 아래로 바꿔줌
# for i in range(len(points) - 1):
#     cur = points[i]
#     next = points[i + 1]
#
#     xDiff = abs(cur[0] - next[0])
#     yDiff = abs(cur[1] - next[1])
#
#     dist += max(xDiff, yDiff)
#
# print(dist)


# 1572. Matrix Diagonal Sum
# # xy = 0
# # xy2 = 0
#
# summ = 0
#
# mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
#
# for i in range(0, len(mat)):
#     x = i
#     y = i
#     summ += (mat[x][y])
#
#     x2 = len(mat) - i - 1
#     y2 = i
#     summ += (mat[x2][y2])
#
# if len(mat) % 2 != 0:
#     mid = int(len(mat) / 2)
#
#     midd = (mat[mid][mid])
#
#     print(summ - midd)
# else:
#     print(summ)


# 1021. Remove Outermost Parentheses

# left = 0
# right = 0
#
# Input = "(()())(())"
# tempstr = ""
# Output = ""
#
# for c in Input:
#
#     tempstr += c
#
#     if c == "(":
#         left = left + 1
#
#     else:
#         left = left - 1
#         if left == 0:
#             # len = len(tempstr)
#             tempstr = tempstr[1:len(tempstr) - 1]
#             Output += tempstr
#
#             # print(tempstr)
#
#             tempstr = ""
# print(Output)
