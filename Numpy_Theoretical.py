""" 
Question-
Difference between Python list and NumPy array:
1. Lists can contain items of completely different datatypes (heterogeneous), 
   while NumPy arrays must contain items of the same datatype (homogeneous).
2. NumPy arrays support element-wise vector operations (like a + b), whereas 
   adding two Python lists simply concatenates them.
3. NumPy arrays are much faster and consume significantly less memory.
"""

""" 
Question-
Difference between dtype and astype():
- 'dtype' is an ATTRIBUTE that reveals the current data type of the elements inside an array.
- 'astype()' is a METHOD (function) used to cast/convert an array copy to a specified new data type.
"""

"""
Question-
Can a 1D array be sliced like a[:,1]? Why or why not?
No, it cannot. The syntax `a[:, 1]` explicitly implies a two-dimensional structure where the 
colon `:` represents "all rows" and the `1` represents "the second column". 
Since a 1D array has only a single axis (axis 0), it lacks a second dimension entirely. 
Attempting this will throw an `IndexError: too many indices for array`. To get the second 
element of a 1D array, you simply use `a[1]`.
"""