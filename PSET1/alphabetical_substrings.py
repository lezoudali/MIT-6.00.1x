'''
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
'''

s = 'fvgswoemdtuiwa'
    
string1 = string2 = ''

i = 0

while i < len(s)-1:
    if s[i] <= s[i+1]:
        string1 = string1 + s[i]    
    elif len(string1) >= len(string2):
        string2 = string1 + s[i]
        string1 = ''      
    elif len(string1) < len(string2):
        string1 = ''     
    i = i + 1

if len(string1) >= len(string2):
    string1 = string1 + s[i]
    print 'Longest substring in alphabetical order is: ' + str(string1)
else: 
    print 'Longest substring in alphabetical order is: ' + str(string2)

