
#Write a program that prints the number of times the string 'bob' occurs in s.

s = 'bboboboboooobobkobooobobobbobcbobboboboi'
count = i = 0
while i < len(s)-2:
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count += 1
    i += 1
    
print "Number of times bob occurs is: " + str(count)