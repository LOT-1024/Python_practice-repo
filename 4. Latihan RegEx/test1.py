import re

# # example
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

# # findall example
# txt = "The rain in Spain"

# [] -> A set of characters
# # Find all lower case characters alphabetically between "a" and "m":

# x = re.findall("[a-m]", txt)
# print(x)

# txt = "That will be 59 dollars"

# # \ -> Signals a special sequence (can also be used to escape special characters)
# #Find all digit characters:

# x = re.findall("\d", txt)
# print(x)

# txt = "hello planet"

# # .	-> Any character (except newline character)
# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

# x = re.findall("he..o", txt)
# print(x)

# txt = "hello planet"

# # ^	-> Starts with
# #Check if the string starts with 'hello':

# x = re.findall("^hello", txt)
# if x:
#   print("Yes, the string starts with 'hello'")
# else:
#   print("No match")

# txt = "hello planet"

# # $	-> Ends with
# #Check if the string ends with 'planet':

# x = re.findall("planet$", txt)
# if x:
#   print("Yes, the string ends with 'planet'")
# else:
#   print("No match")

# txt = "hello planet"

# # *	-> Zero or more occurrences
# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

# x = re.findall("he.*o", txt)

# print(x)

# txt = "hello planet"

# # +	-> One or more occurrences
# #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

# x = re.findall("he.+o", txt)

# print(x)

# txt = "hello planet"

# # ?	-> Zero or one occurrences
# #Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

# x = re.findall("he.?o", txt)

# print(x)

# #This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

# txt = "hello planet"

# # {} -> Exactly the specified number of occurrences
# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{2}o", txt)

# print(x)

txt = "The rain in Spain falls mainly in the plain!"

# |	-> Either or
#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

