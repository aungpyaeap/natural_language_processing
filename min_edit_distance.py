# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:19:52 2019

@author: TP052143
"""

# minimun edit distance

# insert single symbol
s = "Manhatan"
s = s[:5] + "t" + s[5:]
print(s)

# delete single symbol
s = "Mannhattan"
s = s[:2] + s[3:]
print(s)

# substitution of single symbol
s = "Manhatton"
s = s[:7] + "a" + s[8:]
print(s)


# Naive recursive solution
def editDistance(str1, str2, m , n): 
  
    # If first string is empty, the only option is to 
    # insert all characters of second string into first 
    if m==0: 
         return n 
  
    # If second string is empty, the only option is to 
    # remove all characters of first string 
    if n==0: 
        return m 
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[m-1]==str2[n-1]: 
        return editDistance(str1,str2,m-1,n-1) 
  
    # If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert 
                   editDistance(str1, str2, m-1, n),    # Remove 
                  
    editDistance(str1, str2, m-1, n-1))    # Replace 
 
str1 = "sunday"
str2 = "saturday"
print (editDistance(str1, str2, len(str1), len(str2)))