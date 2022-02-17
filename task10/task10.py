my_str = 'Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.'
words = my_str.split()
words.sort()
for word in words:  
   print(word)  