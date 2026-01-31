def union_array(a, b):
    return list(set(a + b))

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

print("Union of arrays:", union_array(a, b))
