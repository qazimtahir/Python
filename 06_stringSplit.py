"""
String Splitting and Joining

Task: Given the string s, use string methods to:
Split into a list: break the string into a list of substrings based on the delimiter ,.
Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
s:str ="apple,banana,cherry,dates"
Expected Output:
["apple", "banana", "cherry", "dates"]
apple banana cherry dates
  """

s = "apple,banana,cherry,dates"

# Split the string into a list based on the delimiter ","
list_of_fruits = s.split(',')

# Join the list into a single string with each element separated by a space
joined_string = ' '.join(list_of_fruits)

# Print the results
print(list_of_fruits)
print(joined_string)
