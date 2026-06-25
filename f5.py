my_tuple = (10, "Python", 3.14, True, "AI")
print("a. Original tuple:", my_tuple)

first_element = my_tuple[0]
last_element = my_tuple[-1]
print(f"b. First element: {first_element}, Last element: {last_element}")

middle_three = my_tuple[1:4]
print("c. Middle 3 elements:", middle_three)

tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
combined_tuple = tuple_a + tuple_b
print("d. Concatenated tuple:", combined_tuple)

reversed_tuple = my_tuple[::-1]
print("e. Reversed tuple:", reversed_tuple)

test_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_twos = test_tuple.count(2)
print(f"f. The number 2 appears {count_of_twos} times in {test_tuple}")

fruit_tuple = ("apple", "banana", "cherry", "date")
cherry_index = fruit_tuple.index("cherry")
print(f"g. The index of 'cherry' is: {cherry_index}")

if "Python" in my_tuple:
    print("h. Yes, 'Python' exists in the tuple.")
else:
    print("h. No, 'Python' does not exist.")

color_list = ["red", "green", "blue"]
color_tuple = tuple(color_list)
print(f"i. Converted list to tuple: {color_tuple} (Type: {type(color_tuple).__name__})")

unsorted_tuple = (42, 12, 89, 5, 23)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("j. Sorted tuple:", sorted_tuple)

repeat_me = ("Hi",)
repeated_tuple = repeat_me * 3
print("k. Repeated tuple:", repeated_tuple)

print("l. Trying to modify the first element of my_tuple...")
try:
    my_tuple[0] = 99
except TypeError as error:
    print(f"   [Caught Expected Error] Success! Tuple is immutable.")
    print(f"   Error message: {error}")
