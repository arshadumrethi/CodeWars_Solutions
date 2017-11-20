#Get the count of vowels in a given string

## My Solution ##
def getCount(inputStr):
    num_vowels = 0
    for char in "aeiou":
        num_vowels = num_vowels + 1
    return num_vowels

getCount("abracadabra")

######### Best Solution ##########

# def getCount(inputStr):
#     print sum(letter in 'aeiou' for letter in inputStr)
#
# getCount(raw_input())

######### Other Solutions I tried ##########
#1.
# def vowels(s):
#     ourvowels = 'aeiou'
#     if s == '':
#         return 0
#     elif s[0] in ourvowels:
#         return 1 + vowels(s[1:])
#     else:
#         return vowels(s[1:])
#
# print vowels("abracadabra")

#2.
# while True:
#     if "s" in s:
#         count = count + 1
#         print count
#         break

# var = s.split(" ")
#
# count = []
#
# def isit(n):
#     vowels = ("a", "e", "i", "o", "u")
#     while vowels in var:
#         print vowels
#         count.append(vowels)
#         print sum(count)
#         #print count
#
# isit(s)
