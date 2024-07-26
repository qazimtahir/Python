"""
Substring Search

Task: Given the string s, use string methods to:
Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
s:str ="the quick brown fox jumps over the lazy dog"
Expected Output:
index of 'fox' is 16
'the' appears 2 times
  """
  
s:str = "the quick brown fox jumps over the lazy dog"

# Find the index of "fox"
index_fox = s.find("fox")

if index_fox == -1:
    print("Index of 'fox' is not found")
else:
    print(f"Index of 'fox' is {index_fox}")

# Count occurrences of "the"
count_the = s.count("the")
print(f"'the' appears {count_the} times")
