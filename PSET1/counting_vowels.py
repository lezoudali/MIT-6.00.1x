
#Write a program that counts up the number of vowels contained in the string s.
s = "azcbobobegghakl"

count = i= 0
while i < len(s):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        count += 1
    i += 1
    
print "Number of vowels: " + str(count)