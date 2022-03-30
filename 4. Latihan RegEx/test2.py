import re

# txt = "The rain in Spain"

# # \A -> Returns a match if the specified characters are at the beginning of the string
# #Check if the string starts with "The":

# x = re.findall("\AThe", txt)

# print(x)

# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")

# txt = "The rain in Spain"

# # \b -> Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# #Check if "ain" is present at the beginning of a WORD:

# x = re.findall(r"\bain", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# txt = "The rain in Spain"

# # \b -> Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# #Check if "ain" is present at the end of a WORD:

# x = re.findall(r"ain\b", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# txt = "The rain in Spain"

# # \d -> Returns a match where the string contains digits (numbers from 0-9)
# #Check if the string contains any digits (numbers from 0-9):

# x = re.findall("\d", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

