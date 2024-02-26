import random

# Generate 100 random numbers in the range 0 to 1000
random_numbers_100 = [random.randint(0, 1000) for _ in range(100)]

# Function to sort the list
def sort_list(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]  # Swap the elements to sort
    return lst

# Function to calculate the average of even and odd numbers
def avg_even_odd(lst):
    even_sum = 0
    even_count = 0
    odd_sum = 0
    odd_count = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
            even_count += 1
        else:
            odd_sum += i
            odd_count += 1
    # Calculate average for even and odd numbers
    even_avg = even_sum / even_count if even_count != 0 else 0
    odd_avg = odd_sum / odd_count if odd_count != 0 else 0
    return even_avg, odd_avg

# Sort the list
sorted_list = sort_list(random_numbers_100)

# Calculate average of even and odd numbers
even_avg, odd_avg = avg_even_odd(sorted_list)

# Print average of even and odd numbers
print("Average of even numbers:", even_avg)
print("Average of odd numbers:", odd_avg)