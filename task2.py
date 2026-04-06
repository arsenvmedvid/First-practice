numbers = [-42, 7, 0, -15, 88, -3, 12, -91, 54, -20, 0, 33, -67, 5, -11, 99, -4, 26, -8, 14]

even_nums = list(filter(lambda x: x % 2 == 0, numbers))
positive_even_nums = list(filter(lambda x: x % 2 == 0 and x > 0, numbers))
greater_than_50 = list(filter(lambda x: x > 50, numbers))

print(f"Парні: {even_nums}")
print(f"Парні додатні: {positive_even_nums}")
print(f"Більші за 50: {greater_than_50}")