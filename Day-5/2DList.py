# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # convert 2D list to 1D list
# flat_list = [item for sublist in matrix for item in sublist]
# print(flat_list)
# # Output:
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # convert in transposed matrix
# transpose = [[row[i] for row in matrix] for i in range(3)]
# print(transpose)
# Output:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# create a list using list comprehension
# list = [expression for item in iterable]
# # Example:
# [[0,1,2],[3,4,5],[6,7,8]]
a=[[k for k in range(3) if i!=k ] for i in range(4)]
print(a)
# Output:
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
