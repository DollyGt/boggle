example:
[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

l = [(i,j) for i in range(3) for j in range(3)]
print(l) 

Dictionary Comprehension Challenges
Example:
Question

# range(5) 
# { 0: "", 1:"*", 2:"**", 3:"***", 4:"****" }
# d = { i:"*" * i for i in range(5)}
# print(d) 
                
# 1. ['Hi', 'There', 'Everyone'] 
# -> {'Hi':2, 'There':5, 'Everyone':8}



#2
# word = 'code'
# -> {'c': 99, 'e': 101, 'd': 100, 'o': 111}
d = ({i:ord(i)for i in word})
print(d)





# 3. ['car', 'cat', 'maps', 'if', 'level'] 
# -> {'car':False, 'pop':True, 'maps':False, 'if':False, 'level':True}





