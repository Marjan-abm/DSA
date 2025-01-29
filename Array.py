''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''
student_pets_list = [0,1,0,2,1,1,4,0,0,0,3,2,1,3,0,2,2,4]
total_pets = 0
for student_pets in student_pets_list:
    total_pets += student_pets
average_pets = total_pets / len(student_pets_list)
print(f"The average number of pets each student has is {average_pets:.2f}")

seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

for i, row in enumerate(seating_chart):
    for j, student in enumerate(row):
        print(f"{student} is seated at table {i + 1}, seat {j + 1}")


# Tuple
def calculate_area_perimeter(side_length):
    area = side_length * side_length
    perimeter = side_length * 4
    result = (area, perimeter)
    return result

result = calculate_area_perimeter(5)
print(f"the area is {result[0]} and the perimeter is {result[1]}")

# search in array
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ITEM = 8

def search(item, list):
    for element in list:
        if element == item:
            return True
    return False

print(search(ITEM, my_list))

# search with index built-in function
index_item = my_list.index(ITEM)
print(index_item)

# Sorting
sample_list = [1,7,3]
sorted_list = sorted(sample_list)
print(sorted_list)
reversed_sample_list = sorted(sample_list, reverse=True)
print(reversed_sample_list)

students_grades = [("Alice", 68), ("Bob", 95), ("Charlie", 71)]
# sort based on the first element of the tuple
print(sorted(students_grades))
# sort based on the second element of the tuple in descending order
print(sorted(students_grades, key = lambda x:x[1], reverse=True))

# Challenge
def find_second_smallest(my_list):
    if len(my_list) >= 2:
        sorted_list = sorted(my_list)
        return sorted_list[1]
    return None

def find_second_smallest_v2(my_list): #more efficient
    if len(my_list) >= 2:
        smallest = float("inf")
        second_smallest = float("inf")
        for num in my_list:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest:
                second_smallest = num
        return second_smallest
    return None

print(find_second_smallest_v2([5, 8, 3, 2, 6]))