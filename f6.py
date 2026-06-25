numbers_list = [23, 89, 12, 56, 78, 5, 89]
largest_num = max(numbers_list)
print(f"a. The largest number in {numbers_list} is: {largest_num}")

unique_list = list(set(numbers_list))
print(f"b. List after removing duplicates: {unique_list}")

even_count = len([num for num in numbers_list if num % 2 == 0])
print(f"c. Number of even numbers in the list: {even_count}")

user_list = []
print("\nd. Please enter 5 numbers:")
for i in range(5):
    num = float(input(f"   Enter number {i+1}: "))
    user_list.append(num)
print(f"   Your entered list is: {user_list}\n")

def calculate_average(lst):
    if not lst: 
        return 0
    return sum(lst) / len(lst)

sample_list = [10, 20, 30, 40, 50]
avg = calculate_average(sample_list)
print(f"e. The average of {sample_list} is: {avg}")

sample_string = "Python"
char_list = list(sample_string)
print(f"f. String '{sample_string}' converted to list: {char_list}")

word_list = ["Coding", "is", "fun"]
joined_string = " ".join(word_list)
print(f"g. List {word_list} joined into a string: '{joined_string}'")
