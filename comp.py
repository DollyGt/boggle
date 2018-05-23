# example of list comprehension/ python comprehension challenges
# l = [1,3,5]

# p = []
# for n in l:
#     p.append(n*2)
#print([n*2 for n in l])
    
# print(p)

# l = [1,3,5]

# p = [n*2 for n in l]

# print(p)

# l = [0,2,4,6,8,10,12]
#print([i*2 for i in range(7)])

# List Comprehension Challenges
# Example:
# Question 
#                 range(10) 
#                 -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Answer
# [n * 2 for i in range(10)]
#1-------------------------------------------------------------------------------1
# range(5) 
# ["*", "*", "*", "*", "*"]
# print(["*" for i in range(5)])

#2-------------------------------------------------------------------------------2
# l = ["Hi", "There", "Everyone"] 
# [2, 5, 8]
# print ([len(i) for i in l])

#3-------------------------------------------------------------------------------3
# range(8) 
# [0, 1, 4, 9, 16, 25, 36, 49]
# print([i**2 for i in range(8)])

#4-------------------------------------------------------------------------------4
#range(5) 
# -> [(0,1), (1,2), (2,3), (3,4), (4,5)]
# print ([(i,i+1 for i in range(5)])

#5-------------------------------------------------------------------------------5
# word = 'woohoo' 
# ['w', 'o', 'o', 'h', 'o', 'o']
# print([i for i in word])

#6-------------------------------------------------------------------------------6
# words =['car', 'cat', 'maps', 'if', 'level'] 
# [('car', 3), ('cat', 3), ('maps', 4), ('if', 2), ('level', 5)]
# print([(i,len(i)) for i in words])

#7--------------------------------------------------------------------------------7
# values =  [(False, False), (False, True), (True, False), (True, True)]
# [False, False, False, True]
# print([(i and j) for i,j in values])

#8--------------------------------------------------------------------------------8
# values = [(False, False), (False, True), (True, False), (True, True)]
# [False, True, True, True]
# print([(i or j) for i,j in values])

