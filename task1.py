users = [
    ("Ivan", 25),
    ("Olena", 19),
    ("Petro", 30),
    ("Anna", 22)
]

sort_name = sorted(users, key=lambda x: x[0])
sort_age = sorted(users, key=lambda x: x[1])

print("Сортування за ім'ям:", sort_name)
print("Сортування за віком:", sort_age)

for name, age in sort_age:
    print(f"{name} - {age}")