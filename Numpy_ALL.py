import numpy as np

a=np.array([
    [11,22,33],
    [44,55,66],
    [77,88,99]
])
print("Question-1")
print("First column:\n", a[:, 0])
print("Last row:\n", a[2, :])
print("Extracted block [[22, 33], [55, 66]]:\n", a[0:2, 1:3]) 
print()

a = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print("Question-2")
print("First row:\n", a[0, :])
print("Second column:\n", a[:, 1])
print("Element 50:\n", a[1, 1])
print()

print("Question-3")
b=np.arange(1,13)
print("Reshaped to (3,4):\n", b.reshape(3, 4))
print("Reshaped to (2,6):\n", b.reshape(2, 6))
print("Reshaped to (2,3,2):\n", b.reshape(2, 3, 2))
print()

a = np.array([1,2,3])
b = np.array([4,5,6])
print("Question-4")
print("Addition: ", a+b)
print("Subtraction: ", a-b)
print("Multiplication: ", a*b)    
print("Division: ", a/b)
print("Power of 3: ", a**3)
print("Square: ", a**2)
print("Mean of a: ", a.mean(), "| Mean of b: ", b.mean())
print()

print("Question-5")
rand_1d=np.random.randint(1,11,10)
rand_2d=np.random.randint(1,10, size=(3,3))
print("1D Random Array:\n", rand_1d)
print("2D Random Array (3x3):\n", rand_2d)
print()

print("Question-6")
a_rand = np.random.rand(2, 5)
print("Random array (2,5):\n", a_rand)
print()

print("Question-8")
a=np.array([1, 2, 3, 4])
a=a.astype(float)  
print("Converted to float:", a)
print()

print("Question-10")
a=np.array([[1, 2, 3], [4, 5, 6]])
print("Shape: ", a.shape)
print("Size: ", a.size)
print("Dimensions(ndim): ", a.ndim)
print("Original dtype: ", a.dtype)
a=a.astype(float)  # Reassigning to save changes!
print("New dtype after change: ", a.dtype)
print()